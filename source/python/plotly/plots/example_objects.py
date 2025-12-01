from pathlib import Path
import sys

# -- Hilfsfunktion: source-Verzeichnis finden ----------------------------------
def _find_source_dir(start: Path | None = None) -> Path:
    """Geht vom Skript nach oben und gibt den Ordner 'source' zurück."""
    here = (start or Path(__file__).resolve())
    for p in [here] + list(here.parents):
        if p.name == "source":
            return p
    raise RuntimeError("Kein 'source'-Ordner in den übergeordneten Pfaden gefunden.")

# -- source auf sys.path + Pfade ableiten --------------------------------------
SOURCE_DIR = _find_source_dir()

# Ausgabe-Verzeichnis für Plots relativ zu source/
FIG_DIR = SOURCE_DIR / "_static" / "plots" / "python" / "plotly"
FIG_DIR.mkdir(parents=True, exist_ok=True)

HERE = Path(__file__).resolve()
HTML_PATH = FIG_DIR / (HERE.stem + ".html")

MATHJAX = SOURCE_DIR / "_static" / "js" / "mathjax" / "tex-chtml-full.js"

# -- Plot ----------------------------------------------------------------------
import numpy as np                # NumPy für numerische Berechnungen (Arrays, linspace, sin)
import plotly.graph_objects as go # Plotly low-level API für interaktive Plots

x = np.linspace(0, 2*np.pi, 100) # 100 Punkte gleichmäßig im Intervall [0, 2π]
y_sin = np.sin(x)                # Sinuswerte zu den x-Punkten

fig = go.Figure() # Leere Plotly-Figur anlegen

fig.add_trace(    # Eine Spur (Trace) zur Figur hinzufügen
    go.Scatter(
        x=x,                                    # x-Daten: Array von 0 bis 2π
        y=y_sin,                                # y-Daten: sin(x)
        mode="lines",                           # Darstellung: nur Linie, keine Marker
        name=r"$f(x) = \sin \left( x \right)$", # Name der Spur, erscheint in der Legende
        marker={"color": "#1F77B4"}           # Linien-/Markerfarbe (Plotly-Standardblau)
    )
)

fig.show() # Figur rendern und interaktiv anzeigen

# -- Export --------------------------------------------------------------------
fig.write_html(
    HTML_PATH,
    include_plotlyjs=True,     # Plotly lokal
    include_mathjax="../../../js/mathjax/tex-chtml-full.js",   # MathJax lokal
    full_html=True
)