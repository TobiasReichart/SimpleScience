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

ps = PlotStyle(background_color="#ffffff")
ps.set_font(family="sans", size=12)

x = np.linspace(-0.5, 6.5, 600)

def f(x):
    return -0.08 * (x - 0.2) * (x - 2.1)**3 * (x - 5.3) + 1.2

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(x, f(x), linewidth=2.5, color=ps.colors["blue"])

# Achsenbereich
x_min, x_max = -0.5, 6.0
y_min, y_max = -0.5, 5.5
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

# Keine Ticks / keine Skalierung
ax.set_xticks([])
ax.set_yticks([])

# Standardrahmen entfernen
for spine in ax.spines.values():
    spine.set_visible(False)

# Achsen mit Pfeilen
ax.annotate(
    "",
    xy=(x_max, 0),
    xytext=(x_min, 0),
    arrowprops=dict(arrowstyle="->", lw=2)
)

ax.annotate(
    "",
    xy=(0, y_max),
    xytext=(0, x_min),
    arrowprops=dict(arrowstyle="->", lw=2)
)

# Achsenbeschriftung
ax.text(x_max, -0.12, "x", fontsize=16)
ax.text(-0.15, y_max, "y", fontsize=16)

tief_x = 0.640505
tief_y = f(tief_x)
ax.plot(tief_x, tief_y, "o", markersize=6, color=ps.colors["red"])
ax.hlines(tief_y, xmin=-0.4, xmax=1.8, linewidth=1.5, color=ps.colors["red"])
ax.text(
    tief_x+0.2, tief_y - 0.15,
    "Tiefpunkt\n(lokales Minimum)",
    fontsize=13,
    va="top",
    ha="center",
    color=ps.colors["red"]
)

sattel_x = 2.1
sattel_y = f(sattel_x)
ax.plot(sattel_x, sattel_y, "o", markersize=6, color=ps.colors["green"])
ax.hlines(sattel_y, xmin=0.8, xmax=3.4, linewidth=1.5, color=ps.colors["green"])
ax.text(
    sattel_x, sattel_y + 0.15,
    "Sattelpunkt",
    fontsize=13,
    va="bottom",
    ha="center",
    color=ps.colors["green"]
)

hoch_x = 4.59949
hoch_y = f(hoch_x)
ax.plot(hoch_x, hoch_y, "o", markersize=6, color=ps.colors["red"])
ax.hlines(hoch_y, xmin=3.5, xmax=5.8, linewidth=1.5, color=ps.colors["red"])
ax.text(
    hoch_x, hoch_y + 0.15,
    "Hochpunkt\n(lokales Maximum)",
    fontsize=13,
    va="bottom",
    ha="center",
    color=ps.colors["red"]
)

fig.savefig(PNG_PATH, dpi=300)
plt.close(fig)
#plt.show()