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
FIG_DIR = SOURCE_DIR / "_static" / "plots" / "python" / "plotly"
FIG_DIR.mkdir(parents=True, exist_ok=True)

HERE = Path(__file__).resolve()
PNG_PATH = FIG_DIR / (HERE.stem + ".png")

# -- Plot ----------------------------------------------------------------------
ps = PlotStyle()
ps.set_font(family="sans", size=12)
fig, ax = plt.subplots(figsize=(5.2, 5.2))


# Achsen & Layout
ax.set_title("Koordinaten einer Plotly Figure")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect("equal")

ps.origin_axes(fig, ax, hide_zero_tick=False)
ax.spines["bottom"].set_position(("data", 1.0))
ax.xaxis.tick_top()
ax.xaxis.set_label_position("top")

ax.set_ylabel("y-Achse")
ax.set_xlabel("x-Achse")

fig.tight_layout()

fig.savefig(PNG_PATH, dpi=150)
plt.close(fig)
#plt.show()