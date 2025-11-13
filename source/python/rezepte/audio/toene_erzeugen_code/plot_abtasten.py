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
FIG_DIR = SOURCE_DIR / "_static" / "plots" / "python" / "rezepte" / "audio"
FIG_DIR.mkdir(parents=True, exist_ok=True)

HERE = Path(__file__).resolve()
PNG_PATH = FIG_DIR / (HERE.stem + ".png")

# -- Parameter ----------
fs   = 2_000          # Abtastrate f_s [Hz]
f0   = 440.0           # Kammerton A4 [Hz]
dur  = 0.005           # 5 ms zeigen
amp  = 1.0
sr_plot = 200 * fs     # glatter Kurvenzug für den "analogen" Sinus (sehr fein)

# -- Daten ----------
# Kontinuierlicher (dicht gesampelter) Sinus für den Wellenzug:
t = np.arange(int(sr_plot * dur)) / sr_plot
x = amp * np.sin(2 * np.pi * f0 * t)

# Abtastpunkte:
Ts = 1.0 / fs
t_s = np.arange(0.0, dur + 1e-12, Ts)             # Abtastzeitpunkte [s]
x_s = amp * np.sin(2 * np.pi * f0 * t_s)          # Werte auf dem Sinus

# -- Plot ----------
ps = PlotStyle()
ps.set_font(family="sans", size=12)
fig, ax = plt.subplots(figsize=(8, 3.5), dpi=150)

# „Analoger“ Wellenzug:
ax.plot(t * 1000, x, lw=2, label="Sinus 440 Hz", color=ps.colors["blue"])

# Senkrechte Linien: von der minimalen Amplitude (ymin) bis zum jeweiligen Sinuswert
ymin, ymax = -1.15 * amp, 1.15 * amp
for ts, xs_val in zip(t_s, x_s):
    ax.vlines(ts * 1000, ymin, xs_val, linewidth=0.8, color=ps.colors["orange"], alpha=0.8)

# Punkte auf dem Wellenzug an den Abtaststellen:
ax.scatter(t_s * 1000, x_s, s=18, zorder=3, label="Abtastwerte", color=ps.colors["orange"])

# Bemaßung zwischen zwei benachbarten Abtastlinien:
if len(t_s) >= 2:
    t0, t1 = t_s[1] * 1000, t_s[2] * 1000          # in ms
    y_dim = ymin * 0.85                             # Position der Maßlinie unterhalb der Kurve
    # Doppelpfeil:
    ax.annotate("",
                xy=(t0, y_dim), xytext=(t1, y_dim),
                arrowprops=dict(arrowstyle="<->", lw=1.0, color=ps.colors["orange"]))
    # Text mittig über der Maßlinie:
    ts_ms = (t1 - t0)
    ax.text((t0 + t1) / 2, y_dim + 0.02 * (ymax - ymin),
            r"$T_s=\frac{1}{f_s}$",
            ha="center", va="bottom",
            color=ps.colors["orange"])

# Zusatz-Label für f_s:
ax.text(
    0.98, 0.05, rf"$f_s={fs/1000:.1f}\,\mathrm{{kHz}}$".replace(".",","),
    transform=ax.transAxes,
    ha="right", va="bottom",
    bbox=dict(
        boxstyle="round,pad=0.2", # leicht gerundete Ecken
        facecolor=ps.background_color,        # Hintergrundfarbe
        edgecolor="none",         # kein Rahmen
        alpha=0.9                 # leicht transparent
    )
)

# Achsen & Optik:
ax.set(
    title="Abtastung eines Sinustons (A4 = 440 Hz)",
    xlabel="Zeit [ms]",
    ylabel="Amplitude"
)
ax.set_xlim(0, dur * 1000)
ax.set_ylim(ymin, ymax)
ax.legend(
    loc="upper right",
    frameon=True,      # Rahmen aktivieren
    edgecolor="black", # Rahmenfarbe
    facecolor="white", # Hintergrund (optional)
    framealpha=0.8,    # Transparenz (1 = deckend)
)

ps.style_axes(fig, ax, comma_axis="y", decimals=1)

fig.tight_layout()
fig.savefig(PNG_PATH, dpi=150)
plt.close(fig)