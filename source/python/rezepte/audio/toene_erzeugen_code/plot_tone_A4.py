from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from beautyplot import PlotStyle

# -- Projekt-Root finden (Marker) ----------
def find_project_root(start: Path | None = None) -> Path:
    """Geht vom Skriptort nach oben und sucht Marker des Projekt-Roots."""
    here = (start or Path(__file__).resolve()).parent
    markers = {".git", "requirements.txt"}
    for p in [here, *here.parents]:
        if any((p / m).exists() for m in markers):
            return p
    return here  # Fallback: Skriptordner

# -- Ausgabe-Pfad ----------
HERE = Path(__file__).resolve()
ROOT = find_project_root()
FIG_DIR = ROOT / "source" / "_static" / "plots" / "python" / "rezepte" / "audio"
FIG_DIR.mkdir(parents=True, exist_ok=True)  # legt 'assets' und 'figures' an, falls nötig
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
