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

t = np.linspace(-0.2, 10.2, 101)

fig, axes = plt.subplots(1, 3, figsize=(8, 3))


axes[0].plot(t, np.ones_like(t), linewidth=2, color=ps.colors["blue"], zorder=3)
axes[0].set_title("konstant\n(ruhend)", fontsize=12)

axes[1].plot(t, t*0.1+0.5, linewidth=2, color=ps.colors["blue"], zorder=3)
axes[1].set_title("linear\n(gleichförmig)", fontsize=12)

axes[2].plot(t, np.cos(t)+1, linewidth=2, color=ps.colors["blue"], zorder=3)
axes[2].set_title("gekrümmt\n(beschleunigt)", fontsize=12)

for ax in axes:
    ps.origin_axes(fig, ax)
    ax.set_ylim(-0.2, 2.2)
    ax.set_xlim(-0.2, 10.2)
    ax.set_xlabel(r"$t$ [s]")
    ax.set_ylabel(r"$x(t)$ [m]")

fig.tight_layout()


fig.savefig(PNG_PATH, dpi=300)
plt.close(fig)
#plt.show()
