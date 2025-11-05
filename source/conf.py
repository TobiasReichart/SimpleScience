from datetime import date

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

# -- Options for HTML output -------------------------------------------------
html_static_path = ["_static"]
html_favicon = "_static/favicon.ico"

# -- Theme Einstellungen -----------------------------------------------------
html_theme = "sphinx_rtd_theme" # default: "alabaster"

html_theme_options = {
    "collapse_navigation": True,            # Navigationsmenüs nicht einklappen
    "sticky_navigation": False,              # Navigation scrollt nicht mit
    "includehidden": True,                   # Hidden toctree-Einträge anzeigen
    "prev_next_buttons_location": "bottom",  # Position der Navigationsbuttons
    "style_nav_header_background": "#2980B9",# Hintergrundfarbe der Kopfzeile
    "style_external_links": True,            # Externe Links markieren
    "body_max_width": "none",                # HTML-Layout auf Bildschirmbreite skalieren
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

# Optionen speziell für die Mathe-Verarbeitung (dollarmath/amsmath)
extensions.append("sphinx.ext.mathjax") # MathJax für Matheformeln
myst_dmath_allow_labels = True  # erlaubt \label{} und \ref{} innerhalb von $$...$$
myst_dmath_allow_space  = True  # erlaubt $x = y$ auch mit Leerzeichen nach dem ersten $
myst_dmath_allow_digits = True  # erlaubt $3x$ (Ziffer direkt nach $) statt Fehler

# --- Codeblöcke--------------------------------------------------------------
extensions.append("sphinx_copybutton") # Kopierbutton für Codeblöcke hinzufügen
html_css_files.append("style/codeblock_layout.css") # Anpassen des HTML-Styles der Codeblöcke


# --- Layout- und Stilmittel -------------------------------------------------



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

# -- Mermaid-Diagramme ------------------------------------------------------
extensions.append("sphinxcontrib.mermaid") # Mermaid-Diagramme unterstützen

mermaid_init_js = """
mermaid.initialize({
    startOnLoad: true,
    theme: "default",       // ""deefault, "dark", "forest", "neutral"
    securityLevel: "loose"  // erlaubt Links/HTML im Diagramm (vorsichtig verwenden!)
});
"""