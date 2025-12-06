import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pathlib import Path
import sys

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
FIG_DIR = SOURCE_DIR / "_static" / "plots" / "python" / "plotly"
FIG_DIR.mkdir(parents=True, exist_ok=True)

HERE = Path(__file__).resolve()
PNG_PATH = FIG_DIR / (HERE.stem + ".png")

# -- Plot ----------------------------------------------------------------------
ps = PlotStyle()
ps.set_font(family="sans", size=12)
fig, ax = plt.subplots(figsize=(5.2, 5.2))

# --- Rechteck in Achsenkoordinaten definieren ---
# Wir nehmen einen Rahmen von 0.2 bis 0.8 in x- und y-Richtung
x0, y0 = 0.2, 0.2
width, height = 0.6, 0.6

rect = Rectangle(
    (x0, y0),
    width,
    height,
    fill=False,
    linewidth=2,
    edgecolor="black",
    transform=ax.transAxes,  # sehr wichtig: Koordinaten in [0,1] des Axes
)
ax.add_patch(rect)

# --- Roter Punkt in der Mitte des Rechtecks ---
cx = x0 + width / 2
cy = y0 + height / 2

ax.plot(
    cx,
    cy,
    marker="o",
    color="red",
    markersize=8,
    transform=ax.transAxes,
    zorder=5,
)

ax.text(
    cx,
    cy - 0.05,           # leicht unterhalb des Punktes
    "(center, middle)",
    ha="center",
    va="top",
    transform=ax.transAxes,
)

# --- Beschriftungen oben: left, center, right ---
ax.text(
    x0,
    y0 + height + 0.05,
    "left",
    ha="center",
    va="bottom",
    transform=ax.transAxes,
)
ax.text(
    x0 + width / 2,
    y0 + height + 0.05,
    "center",
    ha="center",
    va="bottom",
    transform=ax.transAxes,
)
ax.text(
    x0 + width,
    y0 + height + 0.05,
    "right",
    ha="center",
    va="bottom",
    transform=ax.transAxes,
)

# --- Beschriftungen links: bottom, middle, top ---
ax.text(
    x0 - 0.05,
    y0,
    "bottom",
    ha="right",
    va="center",
    transform=ax.transAxes,
)
ax.text(
    x0 - 0.05,
    y0 + height / 2,
    "middle",
    ha="right",
    va="center",
    transform=ax.transAxes,
)
ax.text(
    x0 - 0.05,
    y0 + height,
    "top",
    ha="right",
    va="center",
    transform=ax.transAxes,
)

ps.beauty(fig, ax)
ax.set_title("Illustration von Ankerpunkten\n(xanchor / yanchor)")
ax.set_axis_off()

plt.tight_layout()

fig.savefig(PNG_PATH, dpi=150)
plt.close(fig)
#plt.show()