import numpy as np
from scipy.io import wavfile

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
    if peak < 1e-12:                             # Stille → direkt Nullen
        return np.zeros_like(x, dtype=np.int16)
    scale = (32767.0 * 10**(headroom_db/20.0)) / peak  # auf 16-bit skalieren
    y = np.clip(x * scale, -32768, 32767)        # Sicherheits-Clip
    return y.astype(np.int16)                    # Quantisierung

def make_tone_wav(
        freq_hz: float,
        duration_s: float,
        sr: int,
        amp: float,
        filename: str
) -> None:
    """Erzeugt einen Sinuston und speichert als 16-bit PCM WAV."""
    N = int(sr * duration_s)                     # Samples
    t = np.arange(N) / sr                        # Zeitachse [s]
    x = amp * np.sin(2 * np.pi * freq_hz * t)    # Sinus

    # kurze Fades (~10 ms) gegen Klicks
    fadelen = max(int(0.01 * sr), 1)
    x[:fadelen] *= np.linspace(0, 1, fadelen)    # Fade-In
    x[-fadelen:] *= np.linspace(1, 0, fadelen)   # Fade-Out

    wavfile.write(filename, sr, to_int16(x))     # schreiben

if __name__ == "__main__":
    # Demo 1: A4 440 Hz, 1 s
    make_tone_wav(
        freq_hz=440.0, duration_s=1.0,
        sr=44100, amp=0.9, filename="tone_A4_440Hz.wav")

    # Demo 2: C5 ca. 523.25 Hz, 0.8 s
    make_tone_wav(
        freq_hz=523.251, duration_s=0.8,
        sr=44100, amp=0.9, filename="tone_C5_523Hz.wav")