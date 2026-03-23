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

epsilon = np.linspace(-2.5, 2.5, 400)
J = epsilon**2 + 1

ps = PlotStyle(background_color="#ffffff")
ps.set_font(family="sans", size=12)

fig, ax = plt.subplots(figsize=(10, 6))

setup_qualitative_axes(ax, xlim=(min(epsilon), max(epsilon)), ylim=(-0.1, 5), xlabel=r"$\varepsilon$", ylabel=r"$J$")

ax.plot(epsilon, J, lw=2, label=r"$J(\varepsilon)$", color=ps.colors["purple"])
ax.text(1, 1.7, r"$\Phi(\varepsilon)$",   fontsize=16, color=ps.colors["purple"])

tief_x = 0
tief_y = 1
ax.plot(tief_x, tief_y, "o", markersize=6, color=ps.colors["red"])
ax.hlines(tief_y, xmin=-1, xmax=1, linewidth=1, color=ps.colors["red"])
ax.text(
    tief_x+0.2, tief_y - 0.1,
    "Tiefpunkt",
    fontsize=14,
    va="top",
    ha="left",
    color=ps.colors["red"]
)

fig.savefig(PNG_PATH, dpi=300)
plt.close(fig)
# plt.show()