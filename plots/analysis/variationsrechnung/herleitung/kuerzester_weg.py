from pathlib import Path
import sys

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
FIG_DIR = SOURCE_DIR / "_static" / "plots" / "analysis" / "variationsrechnung" / "herleitung"
FIG_DIR.mkdir(parents=True, exist_ok=True)

HERE = Path(__file__).resolve()
PNG_PATH = FIG_DIR / (HERE.stem + ".png")

# -- Plot ----------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

def setup_qualitative_axes(ax, xlim, ylim, xlabel="x", ylabel="y"):
    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)

    # x-Achse
    ax.annotate(
        "",
        xy=(xlim[1], 0),
        xytext=(xlim[0], 0),
        arrowprops=dict(arrowstyle="->", lw=2)
    )

    # y-Achse
    ax.annotate(
        "",
        xy=(0, ylim[1]),
        xytext=(0, ylim[0]),
        arrowprops=dict(arrowstyle="->", lw=2)
    )

    # Achsenbeschriftungen
    ax.text(xlim[1], -0.06, xlabel, va="top", ha="right", fontsize=16)
    ax.text(-0.10, ylim[1], ylabel, va="top", ha="right", fontsize=16)

# Punkte P1 und P2
x1, y1 = 1.0, 1.0
x2, y2 = 5.0, 3.0

t = np.linspace(0, 1, 400)


x = x1 + (x2 - x1) * t
y = y1 + (y2 - y1) * (1 - (1 - t)**2) + 0.1*np.sin(5*t*np.pi)


ps = PlotStyle(background_color="#ffffff")
ps.set_font(family="sans", size=12)

fig, ax = plt.subplots(figsize=(10, 6))

setup_qualitative_axes(ax, xlim=(-0.2, 6.3), ylim=(-0.2, 3.6), xlabel=r"$x$", ylabel=r"$y$")

# Hilfslinien
ax.plot([-0.1, x1], [y1, y1], "--", lw=1.5, color=ps.colors["gray"])
ax.plot([-0.1, x2], [y2, y2], "--", lw=1.5, color=ps.colors["gray"])
ax.plot([x1, x1], [-0.1, y1], "--", lw=1.5, color=ps.colors["gray"])
ax.plot([x2, x2], [-0.1, y2], "--", lw=1.5, color=ps.colors["gray"])

# Beschriftung x1, x2, y1, y2
ax.text(x1, -0.12, r"$x_1$", ha="center", va="top",    fontsize=13, color=ps.colors["gray"])
ax.text(x2, -0.12, r"$x_2$", ha="center", va="top",    fontsize=13, color=ps.colors["gray"])
ax.text(-0.12, y1, r"$y_1$", ha="right",  va="center", fontsize=13, color=ps.colors["gray"])
ax.text(-0.12, y2, r"$y_2$", ha="right",  va="center", fontsize=13, color=ps.colors["gray"])

# Punkte P1 und P2
ax.plot(x1, y1, "o", ms=6, color=ps.colors["blue"], zorder=3)
ax.plot(x2, y2, "o", ms=6, color=ps.colors["blue"], zorder=3)

ax.text(x1 - 0.25, y1 - 0.18, r"$P_1$", fontsize=16, color=ps.colors["blue"])
ax.text(x2 + 0.12, y2 + 0.02, r"$P_2$", fontsize=16, color=ps.colors["blue"])

# zwei Möglichkeiten
ax.plot(x, y, lw=2, label=r"$y(x)$", color=ps.colors["orange"])

# "Legende" als freie Beschriftung rechts
ax.text(2.3, 1.8, r"$y(x)$",   fontsize=16, color=ps.colors["orange"])

fig.savefig(PNG_PATH, dpi=300)
plt.close(fig)
# plt.show()