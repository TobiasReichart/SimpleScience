from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt

# --- Hilfsfunktion: source-Verzeichnis finden -----------------
def _find_source_dir(start: Path | None = None) -> Path:
    """Geht vom Skript nach oben und gibt den Ordner 'source' zurück."""
    here = (start or Path(__file__).resolve())
    for p in [here] + list(here.parents):
        if p.name == "source":
            return p
    raise RuntimeError("Kein 'source'-Ordner in den übergeordneten Pfaden gefunden.")

# --- source auf sys.path + Pfade ableiten ---------------------
SOURCE_DIR = _find_source_dir()
sys.path.insert(0, str(SOURCE_DIR))

from plot.beautyplot import PlotStyle  # jetzt sicher importierbar

# Ausgabe-Verzeichnis für Plots relativ zu source/
FIG_DIR = SOURCE_DIR / "_static" / "plots" / "python" / "rezepte" / "audio"
FIG_DIR.mkdir(parents=True, exist_ok=True)

HERE = Path(__file__).resolve()
PNG_PATH = FIG_DIR / (HERE.stem + ".png")

# -- Parameter ---
sr = 44100   # Abtastrate
freq = 440.0 # Kammerton A4
dur = 0.005  # nur 5 ms anzeigen
amp = 1.0

# -- Signal erzeugen ---
t = np.arange(int(sr * dur)) / sr
x = amp * np.sin(2 * np.pi * freq * t)
ymin, ymax = -1.15 * amp, 1.15 * amp

# -- Plot ---
ps = PlotStyle()
ps.set_font(family="sans", size=12)
fig, ax = plt.subplots(1, 1, figsize=(8, 3.5))
ax.plot(t * 1000, x, linewidth=2, color=ps.colors["blue"])
ax.set(title="Kammerton A4 (440 Hz) – Zeitbereich", xlabel="Zeit [ms]", ylabel="Amplitude")
ax.set_ylim(ymin, ymax)
ax.set_xlim(0., 5.)

ps.style_axes(fig, ax, comma_axis="y", decimals=1)

fig.tight_layout()

fig.savefig(PNG_PATH, dpi=150)
plt.close(fig)
