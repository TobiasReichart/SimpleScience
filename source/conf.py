from datetime import date # für copyright Jahr
import os                 # für path manipulations
import sys                # für path manipulations

sys.path.insert(0, os.path.abspath('.'))        # Sicherstellen, dass _ext gefunden wird
sys.path.insert(0, os.path.abspath('./_ext'))   # Sicherstellen, dass _ext gefunden wird

# -- Project information -----------------------------------------------------
project = "SimpleScience"
author = "Tobias Reichart"
copyright = f"{date.today().year}, {author}"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
extensions = []
templates_path = ["_templates"]
exclude_patterns = []
language = "de"
html_js_files = []

# --- Entwicklerbereich ---
exclude_patterns = []
if not tags.has("dev"):
    exclude_patterns.append("dev/**")

# -- Options for HTML output -------------------------------------------------
html_static_path = ["_static"]
html_favicon = "_static/favicon.ico"

# -- Theme Einstellungen -----------------------------------------------------
html_theme = "sphinx_rtd_theme" # default: "alabaster"

html_theme_options = {
    "collapse_navigation": False,               # Navigationsmenüs nicht einklappen
    "navigation_depth": -1,                     # alle Ebenen anzeigen (-1 = unbegrenzt)
    "sticky_navigation": False,                 # Navigation scrollt nicht mit
    "includehidden": True,                      # Hidden toctree-Einträge anzeigen
    "prev_next_buttons_location": "bottom",     # Position der Navigationsbuttons
    "style_nav_header_background": "#2980B9", # Hintergrundfarbe der Kopfzeile
    "style_external_links": True,               # Externe Links markieren
    "body_max_width": "none",                   # HTML-Layout auf Bildschirmbreite skalieren
}

html_show_sourcelink = False  # Quelltext-Button ausblenden
html_css_files = []           # Liste für eigene Styles

# -- Umbau von rst auf MySt-Markdown -----------------------------------------
extensions.append("myst_parser") # Verwendung von MySt-Markdown erlauben
root_doc = "index"               # (bei älteren Sphinx-Versionen: master_doc = "index")

# reST und Markdown parallel erlauben: (Altlasten auch einpfelgbar)
source_suffix = {
    ".rst": "restructuredtext",
    ".md":  "markdown",
}

# sinnvolle MyST-Erweiterungen
myst_enable_extensions = [
    "colon_fence",   # erlaubt ::: fenced directives (Alternative zu ```{note} ... ``` mit :::note)
    "dollarmath",    # $...$ und $$...$$ für Inline- und Block-Mathe
    "amsmath",       # unterstützt LaTeX-Umgebungen wie \begin{align}...\end{align}
    "deflist",       # Definition Lists im Markdown-Stil
    "tasklist",      # - [ ] und - [x] für Aufgabenlisten mit Checkboxen
]

# -- MathJax ----------------------------------------------------------------
# Optionen speziell für die Mathe-Verarbeitung (dollarmath/amsmath)
extensions.append("sphinx.ext.mathjax")           # MathJax für Matheformeln
mathjax_path = "js/mathjax/es5/tex-chtml-full.js" # lokales MathJax

myst_dmath_allow_labels = True  # erlaubt \label{} und \ref{} innerhalb von $$...$$
myst_dmath_allow_space  = True  # erlaubt $x = y$ auch mit Leerzeichen nach dem ersten $
myst_dmath_allow_digits = True  # erlaubt $3x$ (Ziffer direkt nach $) statt Fehler

mathjax3_config = {
    "loader": {"load": ["[tex]/color"]},
    "tex": {
        "packages": {"[+]": ["color"]},
        "macros": {
            "red":    ["{\\color[RGB]{214,39,40} #1}", 1],     # D62728
            "blue":   ["{\\color[RGB]{31,119,180} #1}", 1],    # 1F77B4
            "green":  ["{\\color[RGB]{44,160,44} #1}", 1],     # 2CA02C
            "orange": ["{\\color[RGB]{255,127,14} #1}", 1],    # FF7F0E
            "purple": ["{\\color[RGB]{148,103,189} #1}", 1],   # 9467BD
            "cyan":   ["{\\color[RGB]{23,190,207} #1}", 1],    # 17BECF
            "teal":   ["{\\color[RGB]{42,161,152} #1}", 1],    # 2AA198
            "gray":   ["{\\color[RGB]{110,110,110} #1}", 1],   # 6E6E6E
        },
        "inlineMath": [
            ["$", "$"],       # $ ... $ als Inline-Math
            ["\\(", "\\)"],   # \( ... \) ebenfalls
        ],
        "displayMath": [
            ["$$", "$$"],     # $$ ... $$ als Display-Math
            ["\\[", "\\]"],   # \[ ... \] ebenfalls
        ],
    },
}
# -- Codeblöcke--------------------------------------------------------------
extensions.append("sphinx_copybutton") # Kopierbutton für Codeblöcke hinzufügen
html_css_files.append("style/codeblock_layout.css") # Anpassen des HTML-Styles der Codeblöcke

# -- Layout- und Stilmittel -------------------------------------------------



# Nummerierung von Bidern, Tabellen und Codeblöcken
numfig = True # Nummerierung von Bildern Tabellen etc. aktivieren
numfig_format = { # Benennung von Abbildung -> Abb, Tabelle -> Tab, etc. ändern
    "figure": "Abb. %s:",    # Bilder: Bsp.: Abb. 1:
    "table": "Tab. %s:",     # Tabellen: Bsp.: Tab. 1:
    "code-block": "Code %s:" # Codeblöcke: Bsp.: Code 1:
}

extensions.append("sphinx_design") # Dropdown-Menü hinzufügen
html_css_files.append("style/hinweisboxen_layout.css") # Anpassen des HTML-Styles der Hinweisboxen

# --- Downloadbutton ---------------------------------------------------------
html_css_files.append("style/download_button.css") # Anpassen des HTML-Styles des Downloadbuttons

# -- Audio-Player -----------------------------------------------------------
html_css_files.append("style/audioplayer.css") # Anpassen des HTML-Styles des Audio-Players
extensions.append("_ext.audiocard")             # Eigene Directive für Audio-Player