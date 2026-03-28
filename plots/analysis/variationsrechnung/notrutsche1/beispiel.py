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
FIG_DIR = SOURCE_DIR / "_static" / "plots" / "analysis" / "variationsrechnung" / "notrutsche1"
FIG_DIR.mkdir(parents=True, exist_ok=True)

HERE = Path(__file__).resolve()
PNG_PATH = FIG_DIR / (HERE.stem + ".png")

# -- Plot ----------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import math
from pathlib import Path

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

def ratio_fn(theta):
    return (theta - math.sin(theta)) / (1 - math.cos(theta))

def solve_theta2(L, H, tol=1e-12, max_iter=300):
    """
    Solve (theta - sin theta)/(1 - cos theta) = L/H for theta in (0, 2π) (or up to 4π).
    Uses bisection for robustness.
    """
    target = L / H

    def f(theta):
        return ratio_fn(theta) - target

    lo = 1e-4
    hi = 2 * math.pi - 1e-6

    flo = f(lo)
    fhi = f(hi)

    if flo * fhi > 0:
        # try wider interval (allow one more arch)
        hi = 4 * math.pi - 1e-6
        fhi = f(hi)
        if flo * fhi > 0:
            raise RuntimeError("Could not bracket root for theta2. Try different A,B.")

    for _ in range(max_iter):
        mid = 0.5 * (lo + hi)
        fmid = f(mid)
        if abs(fmid) < tol:
            return mid
        if flo * fmid <= 0:
            hi = mid
            fhi = fmid
        else:
            lo = mid
            flo = fmid
    return 0.5 * (lo + hi)

def brachistochrone_cycloid(A, B, n_points=1400):
    """
    Brachistochrone between A=(xA,yA) and B=(xB,yB) in a coordinate system
    where y is positive downward. Returns cycloid parameters and sampled curve.
    """
    xA, yA = A
    xB, yB = B
    L = xB - xA
    H = yA - yB  # positive drop (since yB<yA)

    if L <= 0 or H <= 0:
        raise ValueError("Need xB>xA and yB<yA with y positive upward (drop H>0).")

    theta2 = solve_theta2(L, H)              # same equation uses L/H with H>0
    R = H / (1 - math.cos(theta2))
    theta = np.linspace(0, theta2, n_points)

    x = xA + R * (theta - np.sin(theta))
    y = yA - R * (1 - np.cos(theta))         # minus sign for y-up coordinates

    return R, theta2, theta, x, y

# Punkte A und B
x1, y1 = 1.0, 3.5
A = (x1, y1)

x2, y2 = 5.0, 1.0
B = (x2, y2)

ps = PlotStyle(background_color="#ffffff")
ps.set_font(family="sans", size=12)

fig, ax = plt.subplots(figsize=(10, 5))

setup_qualitative_axes(ax, xlim=(-0.2, 7.3), ylim=(-0.2, 4.3), xlabel="x", ylabel="y")

# Hilfslinien
ax.plot([-0.1, 7.3], [y1, y1], "--", lw=1.5, color=ps.colors["gray"])
ax.plot([-0.1, x2], [y2, y2], "--", lw=1.5, color=ps.colors["gray"])
ax.plot([x1, x1], [-0.1, y1], "--", lw=1.5, color=ps.colors["gray"])
ax.plot([x2, x2], [-0.1, y2], "--", lw=1.5, color=ps.colors["gray"])

# Beschriftung x1, x2, y1, y2
ax.text(x1, -0.12, r"$x_A$", ha="center", va="top",    fontsize=14, color=ps.colors["gray"])
ax.text(x2, -0.12, r"$x_B$", ha="center", va="top",    fontsize=14, color=ps.colors["gray"])
ax.text(-0.12, y1, r"$y_A$", ha="right",  va="center", fontsize=14, color=ps.colors["gray"])
ax.text(-0.12, y2, r"$y_B$", ha="right",  va="center", fontsize=14, color=ps.colors["gray"])

# Punkte A und B
ax.plot(x1, y1, "o", ms=6, color=ps.colors["blue"], zorder=3)
ax.plot(x2, y2, "o", ms=6, color=ps.colors["blue"], zorder=3)

ax.text(x1 - 0.25, y1 + 0.18, r"$A$ (Startpunkt)", fontsize=16, color=ps.colors["blue"])
ax.text(x2 + 0.12, y2 + 0.02, r"$B$ (Endpunkt)", fontsize=16, color=ps.colors["blue"])

R, theta2, theta, x, y = brachistochrone_cycloid(A, B)

# Rolling circle snapshots (dashed)
a = np.array([0.25, 0.45, 0.65, 0.85])
snap_thetas = a * theta2
phi = np.linspace(0, 2*np.pi, 480)

# Cycloid (fastest slide)
ax.plot(x, y, linewidth=2.8)

# Circles (dashed) + current point on rim
for th, a in zip(snap_thetas, np.flip(a)):
    # circle center while rolling along the horizontal through A
    xc = A[0] + R * th
    yc = A[1] - R

    cx = xc + R * np.cos(phi)
    cy = yc - R * np.sin(phi)
    ax.plot(cx, cy, linestyle="--", linewidth=1.2, color=ps.colors["black"], alpha=a)

    # point on rim generating the cycloid
    px = A[0] + R * (th - np.sin(th))
    py = A[1] - R * (1 - np.cos(th))
    ax.scatter([px], [py], s=28, color=ps.colors["red"], zorder=10, alpha=a)

ax.set_aspect("equal", adjustable="box")

fig.savefig(PNG_PATH, dpi=300)
plt.close(fig)
# plt.show()