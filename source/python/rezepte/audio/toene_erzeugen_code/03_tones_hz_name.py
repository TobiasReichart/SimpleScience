from typing import Union
import numpy as np
from scipy.io import wavfile
import re

_NOTE_RE = re.compile(r"^([A-Ga-g])([#b]?)(-?\d+)$")
_SEMITONES = {
    "C": -9, "C#": -8, "Db": -8, "D": -7, "D#": -6, "Eb": -6, "E": -5,
    "F": -4, "F#": -3, "Gb": -3, "G": -2, "G#": -1, "Ab": -1, "A": 0,
    "A#": 1, "Bb": 1, "B": 2
}

def note_to_freq(note: str, A4: float = 440.0) -> float:
    """Gleichstufige Stimmung. Notation: A4, C#5, Db3, …"""
    m = _NOTE_RE.match(note)                # Regex-Match auf den ganzen String
    if not m:
        raise ValueError(...)
    name = m.group(1).upper()               # Grundton (A..G), auf Großbuchstabe normiert
    accidental = m.group(2)                 # '' oder '#' oder 'b'
    octave = int(m.group(3))                # Oktavzahl als int
    key = name + accidental                 # z. B. "C#", "Bb", "A"
    if key not in _SEMITONES:
        raise ValueError(...)
    n = _SEMITONES[key] + 12 * (octave - 4) # Halbtöne relativ zu A4
    return A4 * (2.0 ** (n / 12.0))         # Gleichstufige Stimmung

def to_int16(
    x: np.ndarray,
    headroom_db: float = 0.0
) -> np.ndarray:
    """
    Skaliert Float-Signal x in int16 ohne Clipping.
    headroom_db < 0 lässt Headroom (z.B. -1.0 dB).
    """
    x = np.asarray(x, dtype=np.float64)          # stabile Rechnung
    peak = np.max(np.abs(x))                     # größter Betrag
    if peak < 1e-12:                             # Stille -> direkt Nullen
        return np.zeros_like(x, dtype=np.int16)
    scale = (32767.0 * 10**(headroom_db/20.0)) / peak  # auf 16-bit skalieren
    y = np.clip(x * scale, -32768, 32767)        # Sicherheits-Clip
    return y.astype(np.int16)                    # Quantisierung

def make_tone_wav(
    note_or_freq: Union[str, float, int],
    duration_s: float,
    sr: int,
    amp: float,
    filename: str,
    A4: float = 440.0,
) -> None:
    """Erzeugt einen Sinuston und speichert als 16-bit PCM WAV."""
    f = _to_freq(note_or_freq, A4=A4)
    N = int(sr * duration_s)                   # Samples
    t = np.arange(N) / sr                      # Zeitachse [s]
    x = amp * np.sin(2 * np.pi * f * t)        # Sinus

    # kurze Fades (~10 ms) gegen Klicks
    fadelen = max(int(0.01 * sr), 1)
    x[:fadelen] *= np.linspace(0, 1, fadelen)  # Fade-In
    x[-fadelen:] *= np.linspace(1, 0, fadelen) # Fade-Out

    wavfile.write(filename, sr, to_int16(x))   # schreiben

# -- Hilfsfunktionen ---------------------------------------
def _to_freq(note_or_freq: Union[str, float, int], A4: float = 440.0) -> float:
    """Hilfsfunktion: nimmt 'A4' oder 440.0 und gibt Hz zurück."""
    if isinstance(note_or_freq, (int, float)):
        return float(note_or_freq)
    return note_to_freq(str(note_or_freq), A4=A4)

if __name__ == "__main__":
    # Hz-Eingabe
    make_tone_wav(440.0, duration_s=1.0, sr=44100, amp=0.9, filename="tone_A4_440Hz.wav")

    # Noten-Eingabe
    make_tone_wav("C5",   duration_s=0.8, sr=44100, amp=0.9, filename="tone_C5.wav")
    make_tone_wav("F#4",  duration_s=0.8, sr=44100, amp=0.9, filename="tone_Fis4.wav")

    # Optional: anderer Kammerton (historisch / Orchester)
    make_tone_wav("A4", duration_s=1.0, sr=44100, amp=0.9, filename="tone_A4_442Hz.wav", A4=442.0)