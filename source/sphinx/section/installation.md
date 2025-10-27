# Installation & erste Schritte

In diesem Abschnitt wollen wir die Dokumentation zum *"laufen"* bringen und die ersten optischen Anpassungen vornehmen.

```{attention}
**Hinweis**: Die folgenden Schritte zur Installation von Sphinx dienen ausschließlich der Orientierung. Installationsroutinen, Systemvoraussetzungen und Benutzeroberflächen können je nach Betriebssystem und Version variieren.  

Vor der Durchführung lies bitte meinen {ref}`Haftungsausschluss <disclaimer>`. Ich übernehme keine Verantwortung für eventuelle Schäden oder Fehlkonfigurationen.  

Voraussetzung für die Installation von Sphinx ist eine bereits installierte Version von Python.
```

```{note}
Es wird **dringend empfohlen**, Sphinx-Projekte in einer *virtuellen Umgebung* (`venv`) aufzubauen.\
So bleibt die Arbeitsumgebung stabil, unabhängig von globalen Paketen und jederzeit reproduzierbar.  

Auf diese Weise verhinderst du Versionskonflikte, hältst dein System sauber und stellst sicher, dass deine Dokumentation auch in Zukunft zuverlässig gebaut werden kann.\
Nähere Informationen findest du auf meiner Infoseite zu {ref}`Virtuellen Umgebungen <Virtuelle Umgebungen>`.
```

## Virtuelle Umgebungen (Quickstart)

```{hint}
Die Quickstart Beschreibungen beziehen sich auf das VS Code **TERMINAL**.
```

````{dropdown} Windows
**Erstellen einer virtuellen Umgebung im Ordner** `.venv`
```{code-block} console
python -m venv .venv
```
**Aktivieren der Umgebung**
```{code-block} console
.venv\Scripts\Activate.ps1
```
(Falls blockiert: `Set-ExecutionPolicy -Scope Process Bypass` nur für die aktuelle Session.)

**Aktualisieren von pip innerhalb der venv** (saubere Basis)
```{code-block} console
python -m pip install -U pip
```
**Installieren der Pakete in der venv**
```{code-block} console
python -m pip install <paket1> <paket2>
```
**Schreiben der Paketversionen in** `requirements.txt`
```{code-block} console
python -m pip freeze > requirements.txt
```
**Reproduzieren der venv anhand von** `requirements.txt`
```{code-block} console
python -m pip install -r requirements.txt
```
**Deaktivieren der virtuellen Umgebung**
```{code-block} console
deactivate
```
````

````{dropdown} macOS
**Erstellen einer virtuellen Umgebung im Ordner** `.venv`
```{code-block} console
python3 -m venv .venv
```
**Aktivieren der Umgebung**
```{code-block} console
source .venv/bin/activate
```
**Aktualisieren von pip innerhalb der venv** (saubere Basis)
```{code-block} console
python -m pip install -U pip
```
**Installieren der Pakete in der venv**
```{code-block} console
python -m pip install <paket1> <paket2>
```
**Schreiben der Paketversionen in** `requirements.txt`
```{code-block} console
python -m pip freeze > requirements.txt
```
**Reproduzieren der venv anhand von** `requirements.txt`
```{code-block} console
python -m pip install -r requirements.txt
```
**Deaktivieren der virtuellen Umgebung**
```{code-block} console
deactivate
```
````

## Installation

Bevor du mit Sphinx arbeiten kannst, musst du es zunächst in deiner Python-Umgebung (**Global** oder in der **Virtuellen Umgebung**)installieren.\
Am einfachsten gelingt das über den Python-Paketmanager `pip`. Führe dazu im Terminal den folgenden Befehl aus:

```{code-block} console
:caption: Installation von Sphinx
:linenos:

python -m pip install sphinx
```

(Erstellen der Dokumentation)=
## Erstellen der Dokumentation

Die Erstellung eines neuen Sphinx-Projekts erfolgt direkt über die Kommandozeile.  
Gehe dazu in das Verzeichnis, in dem deine Dokumentation gespeichert werden soll.

```{note}
Unter **Windows** kannst du im gewünschten Ordner mit der **rechten Maustaste** klicken und *In Terminal öffnen* wählen.\
Unter **macOS** kannst du auf den gewünschten Zielordner mit der **rechten Maustaste** klicken und *Neues Terminal beim Ordner* wählen.\
In **beiden** Betriebssystemen kannst du im Terminal mit `cd` in den Zielordner navigieren, oder das Terminal in VS Code verwenden (hier muss der Zielordner im Explorer geöffnet sein
).
```

In dem nun geöffneten Terminal kann nun durch die Eingabe von `sphinx-quickstart` und anschlißende Bestätigung durch {kbd}`Enter` die Erstellung einer neuen Dokumentation gestartet werden.

```{code-block} console
:caption: Neue Dokumentation erstellen
:linenos:

sphinx-quickstart
```

Daraufhin können einige Spezifikationen für die Dokumentation festgelegt werden. Diese Parameter lassen sich teilweise auch nachträglich im Projekt anpassen. Im folgenden Beispiel wurden die **gelb markierten** Einträge gesetzt, alle übrigen durch einfaches Bestätigen mit {kbd}`Enter` leer übernommen.

```{code-block} console
:caption: Dokumentationsparameter setzen
:emphasize-lines: 12, 15, 16, 25

Pfad>sphinx-quickstart
Welcome to the Sphinx 8.1.3 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: .

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]: y

The project name will occur in several places in the built documentation.
> Project name: Sphinx
> Author name(s): Tobias Reichart
> Project release []:

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
> Project language [en]: de

Creating file D:\Dokumente\Dokumentationen\Sphinx\source\conf.py.
Creating file D:\Dokumente\Dokumentationen\Sphinx\source\index.rst.
Creating file D:\Dokumente\Dokumentationen\Sphinx\Makefile.
Creating file D:\Dokumente\Dokumentationen\Sphinx\make.bat.

Finished: An initial directory structure has been created.

You should now populate your master file D:\Dokumente\Dokumentationen\Sphinx\source\index.rst and create other documentation
source files. Use the Makefile to build the docs, like so:
make builder
where "builder" is one of the supported builders, e.g. html, latex or linkcheck.
```

Nach Abschluss aller Eingaben wurde das Standardgerüst eines neuen Sphinx-Projekts erzeugt:

```{code-block} none
:caption: Ordnerstruktur eines neuen Sphinx-Projekts

Sphinx-Projekt
├ build
├ source
│ ├ _static
│ ├ _templates
│ ├ conf.py
│ └ index.rst
├ make.bat
└ Makefile
```

Das Projekt kann anschließend durch Eingabe von `sphinx-build -b html source build/html` im Terminal als statische HTML-Seite generiert werden.

```{code-block} console
:caption: statische HTML-Seite generieren
:linenos:

sphinx-build -b html source build/html
```

Dabei wird automatisch der Ordner `build` mit dem Unterordner `html` erzeugt, der die Datei `index.html` enthält.\
Diese kann per Doppelklick im Browser geöffnet werden und zeigt die Startseite der frisch generierten Dokumentation.

```{code-block} none
:caption: Ordnerstruktur des Sphinx-Projekts nach erstem Render
:emphasize-lines: 9

Sphinx-Projekt
├ build
│ └ html
│   ├ _sources
│   ├ _static
│   ├ .doctrees
│   ├ .buildinfo
│   ├ genindex.html
│   ├ index.html
│   ├ objects.inv
│   ├ search.html
│   └ searchindex.js
├ source
├ make.bat
└ Makefile
```

Im Browser erscheint daraufhin die folgende Ansicht:

```{figure} ../../_static/img/sphinx/installation/default-theme.png
:align: center
:width: 100%

Voreingestelltes Layout
```

(Theme anpassen)=
## Theme anpassen

Sphinx bietet zahlreiche vordefinierte Themes, mit denen sich das Erscheinungsbild der generierten Dokumentation anpassen lässt.\
Eine Übersicht verfügbarer Themes findet sich auf der [Website Write the Docs](https://www.writethedocs.org/guide/tools/sphinx-themes/) .\
Für diese Dokumentation wird das Layout Read the Docs verwendet.

Um das Theme zu installieren, kann wie bei der Sphinx-Installation der Python-Paketmanager `pip` verwendet werden. Führe dazu im Terminal den folgenden Befehl aus:

```{code-block} console
:caption: Read the Docs installieren
:linenos:

python -m pip install sphinx-rtd-theme
```

Nach der Installation muss das Theme in der Konfigurationsdatei `conf.py` eingetragen werden. Diese Datei befindet sich im `source`-Verzeichnis des Projekts und enthält sämtliche Einstellungen der Dokumentation.

```{code-block} none
:caption: Ordnerstruktur des Sphinx-Projekts
:emphasize-lines: 6

Sphinx-Projekt
├ build
├ source
│ ├ _static
│ ├ _templates
│ ├ conf.py
│ └ index.rst
├ make.bat
└ Makefile
```

```{code-block} python
:caption: conf.py nach sphinx-quickstart
:linenos:
:emphasize-lines: 26

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sphinx'
copyright = '2025, Tobias Reichart'
author = 'Tobias Reichart'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'de'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
```

In der `conf.py` findet sich die Variable `html_theme`, der nun der Name des neuen Themes zugewiesen wird.\
Lösche hierfür die markierte Zeile aus deiner `conf.py` und füge unter `html_static_path = ['_static']` die folgende Codezelle ein. Im folgenden werden wir noch weitere Einstellungen an unserem verwendeten Theme vornehmen.

```{code-block} python
:caption: Theme festlegen
:linenos:

# -- Theme Einstellungen -----------------------------------------------------
html_theme = 'sphinx_rtd_theme' # default: 'alabaster'
```

Um die Änderung zu übernehmen, wird die Dokumentation erneut mit folgendem Befehl gerendert:

```{code-block} console
:caption: HTML-Seite neu generieren
:linenos:

sphinx-build -b html source build/html
```

Nach dem erfolgreichen Build kann die Seite im Browser mit kbd`F5` aktualisiert werden.\
Das Layout erscheint nun im **Read the Docs**-Design:

```{figure} ../../_static/img/sphinx/installation/rtd-theme.png
:align: center
:width: 100%

Theme: *Read the Docs*
```

Das Theme Read the Docs lässt sich über den Parameter `html_theme_options` in der `conf.py` weiter anpassen.\
Ein Beispiel möglicher Optionen:

```{code-block} python
:caption: Theme-Optionen anpassen
:linenos:

html_theme_options = {
    'collapse_navigation': True,             # Navigationsmenüs nicht einklappen
    'sticky_navigation': False,              # Navigation scrollt nicht mit
    'includehidden': True,                   # Hidden toctree-Einträge anzeigen
    'prev_next_buttons_location': 'bottom',  # Position der Navigationsbuttons
    'style_nav_header_background': '#2980B9',# Hintergrundfarbe der Kopfzeile
    'style_external_links': True,            # Externe Links markieren
    'body_max_width': 'none',                # HTML-Layout auf Bildschirmbreite skalieren
}

html_show_sourcelink = False  # Quelltext-Button ausblenden
html_css_files = []           # Liste für eigene Styles
```

Die Variable `html_css_files` bleibt hier zunächst leer, um die `conf.py` übersichtlich zu halten.\
Später können eigene CSS-Dateien mit `.append()` hinzugefügt werden, um gezielt optische Anpassungen vorzunehmen.

Die `conf.py` sollte nach diesen Änderungen folgendermaßen aussehen:

```{code-block} python
:caption: Konfigurationsdatei nach den ersten Anpassungen
:linenos:

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sphinx'
copyright = '2025, Tobias Reichart'
author = 'Tobias Reichart'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'de'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']

# -- Theme Einstellungen -----------------------------------------------------
html_theme = 'sphinx_rtd_theme' # default: 'alabaster'

html_theme_options = {
    'collapse_navigation': True,             # Navigationsmenüs nicht einklappen
    'sticky_navigation': False,              # Navigation scrollt nicht mit
    'includehidden': True,                   # Hidden toctree-Einträge anzeigen
    'prev_next_buttons_location': 'bottom',  # Position der Navigationsbuttons
    'style_nav_header_background': '#2980B9',# Hintergrundfarbe der Kopfzeile
    'style_external_links': True,            # Externe Links markieren
    'body_max_width': 'none',                # HTML-Layout auf Bildschirmbreite skalieren
}

html_show_sourcelink = False  # Quelltext-Button ausblenden
html_css_files = []           # Liste für eigene Styles
```

````{tip}
Das Copyright-Jahr in der `conf.py` kann automatisch aus dem aktuellen Systemdatum erzeugt werden.\
Passe hierfür einfach die obersten Zeilen deiner `conf.py`-Datei an.

```{code-block} python
:caption: Automatische Jahresangabe im Copyright
:linenos:
:emphasize-lines: 1, 5

from datetime import date

project = 'Sphinx'
author = 'Tobias Reichart'
copyright = f'{date.today().year}, {author}'
````

(sphinx-autobuild)=
## Live-Vorschau mit sphinx-autobuild

Um Änderungen in Sphinx **sofort im Browser sichtbar zu machen**, kann das Werkzeug `sphinx-autobuild` verwendet werden.
Es überwacht das Projektverzeichnis und aktualisiert die Ausgabe automatisch, sobald eine Datei gespeichert wird ( {kbd}`Strg` + {kbd}`S` ).

Die Installation erfolgt wie gewohnt über `pip`.
```{code-block} console
:caption: sphinx-autobuild installieren
:linenos:

python -m pip install sphinx-autobuild
```
Anschließend kann der folgende Befehl in der Konsole ausgeführt werden - entweder in der noch geöffneten Eingabeaufforderung des Projekts oder, wie in {ref}`Erstellen der Dokumentation` beschrieben, in einem neuen Terminalfenster:
```{code-block} console
:caption: Live-Build mit sphinx-autobuild starten
:linenos:

sphinx-autobuild source build/html
```
Nach dem Start erfolgt eine erste vollständige Kompilierung der Dokumentation.
Die Konsole zeigt anschließend die lokale Serveradresse, über die die Seite aufgerufen werden kann:
```{code-block} console
:caption: Ausgabe nach Start des Live-Servers
:linenos:
:emphasize-lines: 17

(.venv) PS Dateipfad> sphinx-autobuild source build/html
[sphinx-autobuild] Starting initial build
[sphinx-autobuild] > python -m sphinx build source build/html
Running Sphinx v7.4.7
loading translations [de]... done
loading pickled environment... done
building [mo]: targets for 0 po files that are out of date
writing output...
building [html]: targets for 0 source files that are out of date
updating environment: 0 added, 0 changed, 0 removed
reading sources...
looking for now-outdated files... none found
no targets are out of date.
build succeeded.

The HTML pages are in build\html.
[sphinx-autobuild] Serving on http://127.0.0.1:8000
[sphinx-autobuild] Waiting to detect changes...
```
Falls sich die Seite nicht automatisch öffnet, kann die angegebene Adresse `http://127.0.0.1:8000` manuell in die Adresszeile des Browsers kopiert werden.\
Alternativ kann auch mit gedrückter {kbd}`Strg`-Taste auf die Adresse gelklickt werden, so wird die lokale Serveradresse im Standardbrowser geöffnet.

Sobald nun eine Markdown- oder reST-Datei geändert und mit {kbd}`Strg` + {kbd}`S` gespeichert wird, erkennt sphinx-autobuild die Änderung automatisch, rendert die Seite neu und aktualisiert die Anzeige im Browser in Echtzeit.

### Live-Vorschau über eine Verknüpfung starten (Windows)

Mit einer Batch-Datei ( `.bat` ) lässt sich der Sphinx-Autobuild per Doppelklick starten. Die Dokumentation wird automatisch im Browser geöffnet und bei jeder Änderung neu gerendert.

**Schritt-für-Schritt**

1. Lege im Projektverzeichnis eine Datei Autobuild starten.bat an.
2. Füge folgenden Inhalt ein und speichere die Datei:

```{code-block} bat
:caption: Batch-Datei für den Autobuild (Windows)
:linenos:

@echo off
setlocal
rem In das Verzeichnis der Batch-Datei wechseln
pushd "%~dp0"
rem (Optional) Virtuelle Umgebung aktivieren, wenn vorhanden
if exist ".venv\Scripts\activate.bat" call ".venv\Scripts\activate.bat"
rem Live-Server starten und Browser öffnen
sphinx-autobuild source build/html --open-browser
rem Aufräumen und Pfad zurücksetzen (nach Beenden)
popd
endlocal
```
3. (Optional) Erstelle per *Rechtsklick* $\rightarrow$ *Weitere Optionen anzeigen* $\rightarrow$ *Verknüpfung erstellen* eine Desktop-Verknüpfung.

Die Verknüpfung kann nun an einen beliebigen Ort verschoben werden.

## Umbau von reST auf MyST-Markdown

(*reST bleibt weiterhin vollständig nutzbar*)

In dieser Dokumentation wird künftig MyST-Markdown als Standardformat verwendet.
Bestehende `.rst`-Seiten können jedoch parallel weiterverwendet werden.
Der Build bleibt dabei vollständig **Sphinx-kompatibel** - sowohl für HTML als auch für PDF-Ausgaben.

### Warum auf Markdown umstellen?

- **Einfachere Syntax**: weniger Tippfehler, schnelleres Schreiben.
- **Bekanntes Format**: Markdown wird in vielen Projekten und Editoren unterstützt.
- **Kein Funktionsverlust**: MyST unterstützt alle Sphinx-Direktiven und Rollen\
    (z. B. Code-Blöcke, toctree, mathematische Formeln, literalinclude, Admonitions …).
- **Erweiterbar**: Mit myst-nb können zusätzlich Jupyter-Notebooks integriert werden.

### Voraussetzungen installieren

Damit Sphinx Markdown-Dateien versteht, muss der **MyST-Parser** installiert werden.\
Die Installation erfolgt wie gewohnt über `pip`.\

```{code-block} console
python -m pip install myst-parser
```

Für Live-Vorschau und automatisches Neurendern kann weiterhin `sphinx-autobuild` genutzt werden (siehe {ref}`sphinx-autobuild`).

### MyST in der Konfiguration aktivieren

Nach der Installation wird der Parser wie unter {ref}`Theme anpassen` in der Datei `conf.py` eingebunden.

Öffne `conf.py` und füge am Ende des Dokuments die folgenden Zeilen hinzu:

```{code-block} python
:caption: MyST-Markdown und reST parallel aktivieren
:linenos:

# -- Umbau von rst auf MySt-Markdown -----------------------------------------
extensions.append('myst_parser') # Verwendung von MySt-Markdown erlauben
root_doc = 'index'   # (bei älteren Sphinx-Versionen: master_doc = 'index')

# reST und Markdown parallel erlauben: (Altlasten auch einpfelgbar)
source_suffix = {
    '.rst': 'restructuredtext',
    '.md':  'markdown',
}

# sinnvolle MyST-Erweiterungen
myst_enable_extensions = [
    # Liste der MyST-Erweiterungen, die aktiv sind
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
```

### Startseite auf Markdown umstellen

Zum Abschluss muss die bisherige `index.rst` in `index.md` umbenannt werden.\
Dazu genügt ein Rechtsklick auf die Datei $\rightarrow$ Umbenennen oder {kdb}`F2`.

Der Inhalt der neuen `index.md` kann anschließend ersetzt werden durch:

```{code-block} markdown
:caption: index.md (Beispiel)
:linenos:

# Sphinx

Der Inhalt der Dokumentation wird im nächsten Kapitel Strukturierungselemente ergänzt.
```

Nach all diesen Schritten erkennt Sphinx automatisch sowohl `.rst`- als auch `.md`-Dateien.\
Du kannst also schrittweise von reStructuredText auf Markdown umsteigen, ohne bestehende Inhalte anzupassen.
Beim nächsten Build (`sphinx-build -b html source build/html`) werden alle Dateien korrekt verarbeitet - unabhängig von deren Format.