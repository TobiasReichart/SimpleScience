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
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

ps = PlotStyle(background_color="#ffffff")
ps.set_font(family="sans", size=12)

fig, ax = plt.subplots(figsize=(6, 6))

# Kreis (gestrichelt)
R = 2.2
circle = plt.Circle((0, 0), R, fill=False, linestyle=(0, (6, 6)), linewidth=1.8, edgecolor=ps.colors["gray"])
ax.add_patch(circle)

# Schräge Gerade s(x)
m = 1.0  # Steigung
b = 0.0  # Achsenabschnitt

x = np.linspace(-R/np.sqrt(2), R/np.sqrt(2), 3)
y = m * x + b
ax.plot(x, y, linewidth=2.2, color=ps.colors["green"])

# Punkt auf der Geraden
x0 = -1
y0 = m * x0 + b

# kleine Verschiebung entlang der x-Richtung
dx = 2
dy = m * dx

# zweiter Punkt auf der Geraden
x1 = x0 + dx
y1 = y0 + dy

# Rechtwinkliges Dreieck
ax.plot([x0, x0], [y0, y1], linewidth=2, color=ps.colors["black"])  # Vertikale Strecke (dy)
ax.plot([x0, x1], [y1, y1], linewidth=2, color=ps.colors["black"])  # Horizontale Strecke (dx)
ax.plot([x0, x1], [y0, y1], linewidth=2, color=ps.colors["red"])    # Hypotenuse (ds) liegt auf der Geraden

# rechter Winkel
right_angle = Wedge((x0, y1), 0.5, -90, 0, fill=False, linewidth=1.0, edgecolor=ps.colors["black"])
ax.add_patch(right_angle)
ax.plot(x0+0.2, y1-0.2, "o", ms=3, color=ps.colors["black"])

# Beschriftungen
ax.text(1.6, m * 1.4 + b + 0.15, r"$f_{II}(x)$", va="bottom", ha="left", fontsize=20, color=ps.colors["green"])
ax.text(x0 - 0.4, (y0 + y1) / 2, r"$\mathrm{d} y$", fontsize=18, color=ps.colors["black"])
ax.text((x0 + x1) / 2 - 0.05, y1 + 0.12, r"$\mathrm{d} x$", fontsize=18, color=ps.colors["black"])
ax.text((x0 + x1) / 2 + 0.05, (y0 + y1) / 2 - 0.15, r"$\mathrm{d} S$", fontsize=18, color=ps.colors["red"])

# Plot optisch bereinigen
ax.set_aspect("equal", adjustable="box")
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)

for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_xticks([])
ax.set_yticks([])

fig.savefig(PNG_PATH, dpi=300)
plt.close(fig)
# plt.show()