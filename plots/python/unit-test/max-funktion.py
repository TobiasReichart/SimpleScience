from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt

def find_project_root(start: Path | None = None) -> Path:
    """
    Findet den Projektroot, indem nach einem Ordner gesucht wird,
    der sowohl 'source' als auch 'plots' enthält.
    """
    here = (start or Path(__file__).resolve())
    for p in [here] + list(here.parents):
        if (p / "source").is_dir() and (p / "plots").is_dir():
            return p
    raise RuntimeError(
        "Projektroot nicht gefunden. Erwartet Ordnerstruktur mit 'source/' und 'plots/' im selben Verzeichnis."
    )

PROJECT_ROOT = find_project_root()
SOURCE_DIR = PROJECT_ROOT / "source"
PLOTS_DIR = PROJECT_ROOT / "plots"

# beautyplot.py importierbar machen
if str(PLOTS_DIR) not in sys.path:
    sys.path.insert(0, str(PLOTS_DIR))

from beautyplot import PlotStyle

# --- Ausgabe-Verzeichnis für Plots relativ zu source/_static/ ---
FIG_DIR = SOURCE_DIR / "_static" / "plots" / "python" / "unit-tests"
FIG_DIR.mkdir(parents=True, exist_ok=True)

HERE = Path(__file__).resolve()
PNG_PATH = FIG_DIR / (HERE.stem + ".png")

# -- Plot ----------------------------------------------------------------------
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch

ps = PlotStyle(background_color="#ffffff")
ps.set_font(family="sans", size=12)

# --- Figure / Layout ---
fig, ax = plt.subplots(1, 1, figsize=(7, 2))

a = (-2, 1)
b = (6, 1)

# Punkte + Strecke
ax.scatter(*a, color=ps.colors["blue"], s=50, zorder=3)
ax.scatter(*b, color=ps.colors["blue"], s=50, zorder=3)
ax.plot([a[0], b[0]], [a[1], b[1]], color="black", linewidth=2)

# Dreieck
coords = [[1.5, 0.5], [2.5, 0.5], [2, 1]]
triangle = patches.Polygon(coords, closed=True, fill=False, edgecolor="black", linewidth=1)
ax.add_patch(triangle)

# ---- 1) Beschriftung a=-2, b=6 ----
ax.annotate(
    rf"$a={a[0]}$",
    xy=a, xytext=(0, 10),
    textcoords="offset points",
    ha="center", va="bottom",
)

ax.annotate(
    rf"$b={b[0]}$",
    xy=b, xytext=(0, 10),
    textcoords="offset points",
    ha="center", va="bottom",
)

# ---- 2) Pfeil zum Dreieck + arithm. Mittel ----
mid_x = (a[0] + b[0]) / 2
mid_pt = (mid_x, 1)

ax.annotate(
    rf"$\frac{{a+b}}{{2}}={mid_x:g}$",
    xy=(2, 1),              # Spitze des Dreiecks
    xytext=(3.6, 1.55),     # Textposition
    arrowprops=dict(arrowstyle="->", lw=1.8),
    ha="left", va="bottom",
)

# ---- 3) Bereich vom Dreieck (x=2) bis b (x=6) bemaßen ----
x0 = 2.0
x1 = b[0]
y_dim = 0.25  # Höhe der Bemaßung unterhalb der Achse

# "Messklammer" (Bracket) von x0 bis x1
bracket = FancyArrowPatch(
    (x0, y_dim), (x1, y_dim),
    arrowstyle="]-[",      # bracket ends
    mutation_scale=6,      # Größe der Klammerenden
    lw=1,
    color="black",
)
ax.add_patch(bracket)

# Text mittig unter die Klammer
dx = x1 - x0
ax.text(
    x0 + dx / 2, y_dim + 0.08,
    rf"$\frac{{|a-b|}}{{2}}={dx:g}$",
    ha="center", va="bottom",
)

ps.origin_axes(fig, ax, hide_zero_tick=False)
ax.set_ylim(-0.5, 2)
ax.set_yticks([])
ax.spines["left"].set_visible(False)
ax.set_xlim(-4.1, 8.1)
ax.grid(False)

fig.tight_layout()

#fig.savefig(PNG_PATH, dpi=300)
#plt.close(fig)
plt.show()