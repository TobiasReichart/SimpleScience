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
FIG_DIR = SOURCE_DIR / "_static" / "plots" / "analysis" / "transformationen" / "fourier-reihe"
FIG_DIR.mkdir(parents=True, exist_ok=True)

HERE = Path(__file__).resolve()
PNG_PATH = FIG_DIR / (HERE.stem + ".png")

# -- Plot ----------------------------------------------------------------------
# Einheitskreis
phi_full = np.linspace(0, 2*np.pi, 400)

# Winkel und Punkt auf dem Kreis
phi = np.deg2rad(45)
px = np.cos(phi)
py = np.sin(phi)

# Winkelbogen für ω t
phi_arc = np.linspace(0, phi, 50)
radius_arc = 0.35

ps = PlotStyle(background_color="#ffffff")
ps.set_font(family="sans", size=12)
fig, ax = plt.subplots(figsize=(5.2, 5.2))

ax.plot(np.cos(phi_full), np.sin(phi_full), linewidth=2, color=ps.colors["blue"])

# Radiusvektor r
ax.annotate(
    "", xy=(px, py), xytext=(0, 0),
    arrowprops=dict(
        arrowstyle="->",
        lw=2,
        color=ps.colors["orange"],
        shrinkA=0,
        shrinkB=0
        )
)
ax.text(
    0.5*px, 0.5*py,
    r"$r = 1$", rotation=45,
    ha="center", va="bottom", color=ps.colors["orange"]
)

# kleiner Pfeil am Ende des Winkelbogens
ax.annotate(
    "",
    xy=(radius_arc*np.cos(phi), radius_arc*np.sin(phi)),
    xytext=(radius_arc, 0.),
    arrowprops=dict(
        arrowstyle="->",
        lw=1.5,
        color=ps.colors["purple"],
        connectionstyle="arc3,rad=0.2",
        shrinkA=0,
        shrinkB=0
        )
)
# Label ω t am Winkelbogen
mid_phi = phi / 2
ax.text(
    0.7*radius_arc*np.cos(mid_phi),
    0.7*radius_arc*np.sin(mid_phi),
    r"$\omega_{\mathrm{t}}$",
    color=ps.colors["purple"],
    ha="center", va="center"
)

# Hilfslinien zu den Achsen
ax.vlines(px, 0, 1.1, linestyles="dashed", colors="gray", linewidth=1)
ax.hlines(py, 0, 1.2, linestyles="dashed", colors="gray", linewidth=1)

ax.annotate(
    "",
    xy=(1.15, 0),
    xytext=(1.15, py),
    arrowprops=dict(
        arrowstyle="<->",
        lw=1.5,
        color=ps.colors["red"],
        shrinkA=0,
        shrinkB=0
    )
)
ax.text(
    1.13,
    py/2,
    r"$y(t) = \sin(\omega_{\mathrm{t}} t)$",
    ha="right", va="center",
    color=ps.colors["red"],
    rotation=90,
)

ax.annotate(
    "",
    xy=(0, 1.05),
    xytext=(px, 1.05),
    arrowprops=dict(
        arrowstyle="<->",
        lw=1.5,
        color=ps.colors["green"],
        shrinkA=0,
        shrinkB=0
    )
)

ax.text(
    px/2,
    1.07,
    r"$x(t) = \cos(\omega_{\mathrm{t}} t)$",
    ha="center", va="bottom",
    color=ps.colors["green"],
)

# Achsen & Layout
ax.set_title("Einheitskreis")
ax.set_xlim(-1.31, 1.31)
ax.set_ylim(-1.31, 1.31)
ax.set_aspect("equal")

ps.origin_axes(fig, ax)

fig.tight_layout()

fig.savefig(PNG_PATH, dpi=150)
plt.close(fig)
#plt.show()