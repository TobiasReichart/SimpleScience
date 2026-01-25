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

from plot.beautyplot import PlotStyle

# Ausgabe-Verzeichnis für Plots relativ zu source/
FIG_DIR = SOURCE_DIR / "_static" / "plots" / "mechanik" / "kinematik"
FIG_DIR.mkdir(parents=True, exist_ok=True)

HERE = Path(__file__).resolve()
PNG_PATH = FIG_DIR / (HERE.stem + ".png")

# -- Plot ----------------------------------------------------------------------
ps = PlotStyle(background_color="#ffffff")
ps.set_font(family="sans", size=12)

fig, ax = plt.subplots(figsize=(6, 1.6))

# 1D-Punkte auf der Zeitachse
x = np.array([0.0, 5.0])
y = np.zeros_like(x)

ax.scatter(x, y, color=ps.colors["blue"], s=100, zorder=3)

# Text über die Punkte
for i, xi in enumerate(x):
    ax.annotate(
        rf"$t$ = {i:.0f} s",
        xy=(xi, 0),
        xytext=(0, 10),           # 10 pt nach oben
        textcoords="offset points",
        ha="center",
        va="bottom",
    )

ps.origin_axes(fig, ax, hide_zero_tick=False)
ax.set_ylim(-0.5, 0.5)
ax.set_yticks([])
ax.spines["left"].set_visible(False)

ax.set_xlabel(r"$x$ [m]")

# Optional: etwas „Luft“ links/rechts
ax.set_xlim(-1.1, 6.1)
ax.grid(False)

fig.tight_layout()

fig.savefig(PNG_PATH, dpi=300)
plt.close(fig)
#plt.show()
