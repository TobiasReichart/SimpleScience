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
def func(t):
    return -0.2*(t - 5)**2 + 5

def lin(t, p1, p2):
    a = (p2[1] - p1[1]) / (p2[0] - p1[0])
    b = p1[1] - p1[0] * a
    return a * t + b

ps = PlotStyle(background_color="#ffffff")
ps.set_font(family="sans", size=12)

t = np.linspace(-0.2, 5.2, 101)
points = [(1, func(1)), (3, func(3))]

fig, ax = plt.subplots(1, 1, figsize=(5.2, 3))

ax.plot(t, func(t), linewidth=2, color=ps.colors["blue"], zorder=3)
ax.plot(t, lin(t, *points), linewidth=1.5, color=ps.colors["orange"], zorder=3)

for p in points:
    ax.scatter(*p, color=ps.colors["purple"], s=30, zorder=3)
    ax.annotate(
        rf"$x(t={p[0]:.1f}$ s) = {p[1]:.1f} m".replace(".", ","),
        xy=p,
        xytext=(5, -10),
        textcoords="offset points",
        ha="left",
        va="top",
        color=ps.colors["purple"],
    )


ps.origin_axes(fig, ax)
ax.set_ylim(-0.4, 6.2)
ax.set_xlim(-0.2, 5.2)
ax.set_xlabel(r"$t$ [s]")
ax.set_ylabel(r"$x(t)$ [m]")
ax.set_title("Durchschnittsgeschwindigkeit")

fig.tight_layout()


fig.savefig(PNG_PATH, dpi=300)
plt.close(fig)
#plt.show()
