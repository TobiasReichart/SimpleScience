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
FIG_DIR = SOURCE_DIR / "_static" / "plots" / "analysis" / "variationsrechnung" / "einfuehrung"
FIG_DIR.mkdir(parents=True, exist_ok=True)

HERE = Path(__file__).resolve()
PNG_PATH = FIG_DIR / (HERE.stem + ".png")

# -- Plot ----------------------------------------------------------------------

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots(figsize=(7, 2.8))

ps = PlotStyle(background_color="#ffffff")
ps.set_font(family="sans", size=12)

# Block
ax.add_patch(Rectangle((2.0, 0.9), 2.8, 1.2, fill=False, linewidth=2, color=ps.colors["black"]))

# Pfeile
ax.annotate("", xy=(2.0, 1.5), xytext=(0.7, 1.5),
            arrowprops=dict(arrowstyle="->", lw=2))
ax.annotate("", xy=(6.0, 1.5), xytext=(4.8, 1.5),
            arrowprops=dict(arrowstyle="->", lw=2))

# Texte
ax.text(0.7, 1.5, "Zahl", fontsize=15, va="center", ha="right")
ax.text(3.4, 1.5, "Funktion", fontsize=15, ha="center", va="center")
ax.text(6.0, 1.5, "Zahl", fontsize=15, va="center", ha="left")

# Alles Unsichtbare entfernen
ax.set_xlim(-0.5, 6.6)
ax.set_ylim(0.7, 2.3)
ax.axis("off")

fig.savefig(PNG_PATH, dpi=300)
plt.close(fig)
# plt.show()