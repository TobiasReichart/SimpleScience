from typing import Union, Sequence
import numpy as np
from scipy.io import wavfile
import re

# -- Töne ----------------------------------------------------------------------
_NOTE_RE = re.compile(r"^([A-Ga-g])([#b]?)(-?\d+)$") # Regex Muster
_SEMITONES = {
    "C": -9, "C#": -8, "Db": -8, "D": -7, "D#": -6, "Eb": -6, "E": -5,
    "F": -4, "F#": -3, "Gb": -3, "G": -2, "G#": -1, "Ab": -1, "A": 0,
    "A#": 1, "Bb": 1, "B": 2
}

# -- Akkordqualität ------------------------------------------------------------
_CHORD_RE = re.compile(r"^\s*([A-Ga-g][#b]?-?\d+)\s*[-\s_]+\s*([A-Za-zäöüÄÖÜ]+[24]?)\s*$") # Regex Muster
QUALITY_INTERVALS = {
    "major":      [0, 4, 7], "dur":  [0, 4, 7], "maj":          [0, 4, 7],
    "minor":      [0, 3, 7], "moll": [0, 3, 7], "min":          [0, 3, 7],
    "diminished": [0, 3, 6], "dim":  [0, 3, 6], "vermindert":   [0, 3, 6],
    "augmented":  [0, 4, 8], "aug":  [0, 4, 8], "uebermaessig": [0, 4, 8], "übermäßig": [0, 4, 8],
    "sus2":       [0, 2, 7],
    "sus4":       [0, 5, 7],
}

# -- Einzelnoten erzeugen ------------------------------------------------------
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

# -- Akorde erzeugen -----------------------------------------------------------
def parse_chord_name(chord: str) -> tuple[str, str]:
    """Parser, der Grundton und Akkordqualität aus natürlicher Sprache zurück gibt."""
    m = _CHORD_RE.match(chord) # Regex-Match auf Eingabe
    if not m:
        raise ValueError(f"Ungültiges Akkordformat: {chord!r} (erwartet z.B. 'D4-Major' oder 'A3-dur')")

    root = m.group(1)             # Grundton mit Oktave
    qual_raw = m.group(2).lower() # Qualitätsstring in Kleinbuchstaben

    # Umlaute/ß vereinheitlichen
    qual_norm = (qual_raw
                 .replace("ä", "ae")
                 .replace("ö", "oe")
                 .replace("ü", "ue")
                 .replace("ß", "ss"))

    return root, qual_norm # (Grundton, normalisierte Qualität)

def chord_frequencies(root_note: str, quality: str, A4: float = 440.0) -> list[float]:
    """Berechnet die Frequenzen aller Töne eines Akkords."""
    if quality not in QUALITY_INTERVALS:
        raise ValueError(f"Unbekannte Qualität {quality!r}. Erlaubt: {sorted(set(QUALITY_INTERVALS))}")

    f0 = note_to_freq(root_note, A4=A4)    # Grundfrequenz des Root-Notes berechnen
    intervals = QUALITY_INTERVALS[quality] # Halbton-Intervalle für die Akkordqualität

    return [f0 * (2.0 ** (k / 12.0)) for k in intervals] # Frequenzen aus Halbtonabständen berechnen

def make_chord_wav(
    notes_or_freqs: Sequence[Union[str, float, int]],
    duration_s: float,
    sr: int,
    amp: float,
    filename: str,
    A4: float = 440.0,
    headroom_db: float = 0.0,
) -> None:
    """Speichert einen mehrstimmigen Akkord als 16-bit-WAV."""
    # Frequenzen ermitteln (Notennamen → Hz; Zahlen → float) 
    freqs = [(_to_freq(nf, A4=A4) if not isinstance(nf, (int, float)) else float(nf))  # Name zu Hz oder casten
             for nf in notes_or_freqs]

    # Zeitachse & Mixpuffer
    N = int(sr * duration_s)            # Anzahl Samples
    t = np.arange(N) / sr               # Zeitvektor in s
    mix = np.zeros(N, dtype=np.float64) # Akkumulator für Summensignal

    # Pegel pro Stimme (einfaches Anti-Clipping)
    per = amp / max(len(freqs), 1)      # gleichmäßig verteilen

    # Stimmen addieren (Sinusschwingungen)
    for f in freqs:
        mix += per * np.sin(2 * np.pi * f * t)  # Summe der Sinustöne

    # kurze Fades (~10 ms) gegen Klicks am Anfang/Ende
    fadelen = max(int(0.01 * sr), 1)
    mix[:fadelen] *= np.linspace(0, 1, fadelen)    # Fade-in
    mix[-fadelen:] *= np.linspace(1, 0, fadelen)   # Fade-out

    # In int16 wandeln und schreiben
    x16 = to_int16(mix, headroom_db=headroom_db)   # Normalisierung/Headroom + Quantisierung
    wavfile.write(filename, sr, x16)               # WAV speichern

def make_named_chord_wav(
    chord_name: str,
    duration_s: float,
    sr: int,
    amp: float,
    filename: str,
    A4: float = 440.0,
    headroom_db: float = 0.0,
) -> None:
    """Erzeugt direkt aus einem Akkordnamen eine WAV-Datei."""
    root, qual = parse_chord_name(chord_name)    # Name -> (Grundton, Qualität)
    freqs = chord_frequencies(root, qual, A4=A4) # Akkordton-Frequenzen berechnen

    # WAV rendern und speichern
    make_chord_wav(freqs, duration_s, sr, amp, filename, A4=A4, headroom_db=headroom_db)


# -- Hilfsfunktionen -----------------------------------------------------------
def _to_freq(note_or_freq: Union[str, float, int], A4: float = 440.0) -> float:
    """Hilfsfunktion: nimmt 'A4' oder 440.0 und gibt Hz zurück."""
    if isinstance(note_or_freq, (int, float)):
        return float(note_or_freq)
    return note_to_freq(str(note_or_freq), A4=A4)

if __name__ == "__main__":
    # A-Dur (A4–C#5–E5)
    make_named_chord_wav("A4-Major", 1.5, 44100, 0.9, "chord_A_major.wav")
    # A-Moll (A4–C5–E5)
    make_named_chord_wav("A4-minor", 1.5, 44100, 0.9, "chord_A_minor.wav")
    # D-Dur (D4–F#4–A4), deutscher Alias „dur“ funktioniert ebenfalls:
    make_named_chord_wav("D4-dur",   1.2, 44100, 0.9, "chord_D_major.wav")
    # Sus-Beispiele:
    make_named_chord_wav("D4-sus2",  1.2, 44100, 0.9, "chord_D_sus2.wav")
    make_named_chord_wav("D4-sus4",  1.2, 44100, 0.9, "chord_D_sus4.wav")