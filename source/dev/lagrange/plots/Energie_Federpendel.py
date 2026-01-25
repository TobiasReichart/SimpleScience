from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch

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
FIG_DIR = SOURCE_DIR / "_static" / "plots" / "mechanik" / "lagrange"
FIG_DIR.mkdir(parents=True, exist_ok=True)

HERE = Path(__file__).resolve()
PNG_PATH = FIG_DIR / (HERE.stem + ".png")

def spring_xy(x0, y0, x1, y1, n_coils=8, amplitude=0.12):
    """Erzeugt (x,y)-Punkte einer "Zickzack"-Feder zwischen (x0,y0) und (x1,y1)."""
    t = np.linspace(0, 1, 2*n_coils + 1)

    # Grundlinie
    x = x0 + (x1 - x0) * t
    y = y0 + (y1 - y0) * t

    # Perpendikuläre Auslenkung (Zickzack)
    dx = x1 - x0
    dy = y1 - y0
    L = np.hypot(dx, dy) + 1e-12
    nx, ny = -dy / L, dx / L  # Normale

    zig = np.zeros_like(t)
    zig[1:-1] = amplitude * np.where(np.arange(1, len(t)-1) % 2 == 1, 1.0, -1.0)

    x = x + nx * zig
    y = y + ny * zig
    return x, y

# -- Plot ----------------------------------------------------------------------
ps = PlotStyle(background_color="#ffffff")
ps.set_font(family="sans", size=12)

# --- Figure / Layout ---
fig = plt.figure(figsize=(12, 5))
gs = fig.add_gridspec(1, 2, width_ratios=[1, 1.35], wspace=0.0)
axL = fig.add_subplot(gs[0, 0])
axR = fig.add_subplot(gs[0, 1])

# === linker Plot ===
# --- Decke ---
ceiling_y = 1.0
axL.plot([-1.2, 1.2], [ceiling_y, ceiling_y], linewidth=2, color="black")

# Schraffur
ceiling_h = 0.15
rect = Rectangle(
    (-1.2, ceiling_y),
    2.4, ceiling_h,
    fill=False, hatch='//', linewidth=0.0
)
axL.add_patch(rect)

# Aufhängepunkt
anchor = (0.0, ceiling_y)
axL.scatter(*anchor, marker='o', s=50, color=ps.colors["blue"], zorder=10)

# Kugelposition
mass_center = (0.0, -0.9)
mass_radius = 0.25
ball = Circle(mass_center, mass_radius, color=ps.colors["red"])
axL.add_patch(ball)
axL.scatter(*mass_center, marker='o', s=50, color="black", zorder=10)

# Feder zwischen Decke und Kugel (bis Kugeloberkante)
spring_end = (mass_center[0], mass_center[1] + mass_radius)
sx, sy = spring_xy(anchor[0], anchor[1], spring_end[0], spring_end[1],
                   n_coils=9, amplitude=0.12)
axL.plot(sx, sy, linewidth=2)

# --- Kräfte ---
x, y = mass_center

# Gewichtskraft (mg) nach unten
arrow_g = FancyArrowPatch(
    (x, y), (x, y - 0.75),
    arrowstyle='-|>', mutation_scale=18, linewidth=2, color="black", zorder=10
)
axL.add_patch(arrow_g)
axL.text(x + 0.08, y - 0.65, r'$\vec{F}_g = m\vec{g}$', va='center', color="black", fontsize=12,)

# Rückstellkraft (Federkraft) nach oben
arrow_s = FancyArrowPatch(
    (x, y), (x, y + 0.75),
    arrowstyle='-|>', mutation_scale=18, linewidth=2, color="black", zorder=10
)
axL.add_patch(arrow_s)
axL.text(x + 0.08, y + 0.65,
        r'$\vec{F}_\mathrm{R} = -k\,x$',
        va='center', color="black", fontsize=12,
        bbox=dict(
            facecolor='white',
            alpha=0.7,
            edgecolor='none',
            boxstyle='round,pad=0.2'
        )         
)

axL.set_title("Federpendel", fontsize=16)
axL.set_aspect('equal')
axL.set_xlim(-1.2, 1.2)
axL.set_ylim(-2.0, ceiling_y + ceiling_h)
axL.axis('off')

# --- rechter Plot ---
t = np.linspace(0, 10, 1200)    # Zeit
omega = 2*np.pi/5               # Periodendauer ~5 s
E_max = 1.0                     # Normiert

# E_pot ~ cos^2, E_kin ~ sin^2 (phasengedreht)
E_pot = E_max * np.cos(omega * t)**2
E_kin = E_max * np.sin(omega * t)**2

# Flächen einfärben: unten (E_kin), oben (E_pot)
axR.fill_between(t, 0, E_kin, alpha=0.25, label=r'$E_\mathrm{kin}$')
axR.fill_between(t, E_kin, E_max, alpha=0.18, label=r'$E_\mathrm{pot}$')

# Trennlinie (sinusförmig im Sinne von sin^2; ist glatt periodisch)
axR.plot(t, E_kin, linewidth=2, color="black")

# E_max als waagerechte Linie
axR.axhline(E_max, linewidth=2, color="black", linestyle="--")
axR.text(t[-1]*0.985, E_max + 0.03, r'$E_\mathrm{max}$', ha='right', va='bottom')

axR.text(2.7, 0.8, r'$E_\mathrm{pot}$', ha='right', va='bottom', color=ps.colors["orange"], fontsize=16)
axR.text(1.5, 0.2, r'$E_\mathrm{kin}$', ha='right', va='bottom', color=ps.colors["blue"], fontsize=16)

# Achsen und Stil
axR.set_xlim(t[0], t[-1])
axR.set_ylim(0, 1.1)
axR.set_xlabel(r'$t$ [s]')
axR.set_ylabel(r'$E(t)$')
axR.set_title("Energieaufteilung über der Zeit")

ps.style_axes(fig, axR, comma_axis="y", decimals=1)

fig.tight_layout()

fig.savefig(PNG_PATH, dpi=300)
plt.close(fig)
#plt.show()