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
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="petal_length", color="species")

# -- Export --------------------------------------------------------------------
fig.write_html(
    HTML_PATH,
    include_plotlyjs=True,     # Plotly lokal
    include_mathjax="../../../js/mathjax/tex-chtml-full.js",   # MathJax lokal
    full_html=True
)