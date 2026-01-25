import numpy as np           # Arrays und Mathe
from scipy.io import wavfile # WAV-Dateien schreiben

sr = 44100   # Abtastrate (Samples pro Sekunde)
dur = 1.0    # Dauer in Sekunden
freq = 440.0 # Frequenz in Hz (A4)
amp = 0.9    # Amplitude (0..1)

N = int(sr * dur)                      # Anzahl Samples
t = np.arange(N) / sr                  # Zeitachse in Sekunden
x = amp * np.sin(2 * np.pi * freq * t) # reiner Sinus

# kurze Ein-/Ausblendung gegen Klicks -> linear (10 ms)
fade = int(0.01 * sr)
x[:fade] *= np.linspace(0, 1, fade)
x[-fade:] *= np.linspace(1, 0, fade)

# Peak suchen (größter Betrag); Sonderfall Stille behandeln
peak = np.max(np.abs(x))
if peak < 1e-12:
    x16 = np.zeros_like(x, dtype=np.int16)
else:
    scale = 32767.0 / peak                # 16-bit Skala: +32767 ist Maximalwert
    y = x * scale
    y = np.clip(y, -32768, 32767)         # gegen Rundungs-Überläufe absichern
    x16 = y.astype(np.int16)

# Schreiben
wavfile.write(filename="tone_A4_440Hz.wav", rate=sr, data=x16)