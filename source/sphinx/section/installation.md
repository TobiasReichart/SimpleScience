# Installation & erste Schritte

In diesem Abschnitt wird der **vollständige** Einstieg in ein neues Sphinx-Projekt beschrieben. Von der Einrichtung einer isolierten Python-Umgebung (empfohlen) bis zur ersten Live-Vorschau im Browser.\
Ziel ist es, eine reproduzierbare, erweiterbare und zukunftssichere Ausgangsbasis für eine technische Dokumentation zu schaffen.

Der Abschnitt richtet sich bewusst an Leserinnen und Leser ohne Vorerfahrung mit Sphinx, setzt jedoch grundlegende Kenntnisse im Umgang mit der Kommandozeile voraus.

```{attention}
**Hinweis**: Die folgenden Schritte zur Installation von Sphinx dienen ausschließlich der Orientierung. Installationsroutinen, Systemvoraussetzungen und Benutzeroberflächen können je nach Betriebssystem und Version variieren.  

Vor der Durchführung lies bitte meinen {ref}`Haftungsausschluss <disclaimer>`. Ich übernehme keine Verantwortung für eventuelle Schäden oder Fehlkonfigurationen.  

Voraussetzung für die Installation von Sphinx ist eine bereits installierte Version von Python.
```

```{note}
Es wird **dringend empfohlen**, Sphinx-Projekte in einer *virtuellen Umgebung* (`venv`) aufzubauen.\
So bleibt die Arbeitsumgebung stabil, unabhängig von globalen Paketen und jederzeit reproduzierbar.  

Auf diese Weise werden Versionskonflikte verhindert, das System sauber gehalten und sichergestellt, dass die Dokumentation auch in Zukunft zuverlässig gebaut werden kann.\
Nähere Informationen findest du auf meiner Infoseite zu {ref}`Virtuellen Umgebungen <Virtuelle Umgebungen>`.
```

## Virtuelle Umgebungen (Quickstart)

```{hint}
Die folgenden Quickstart-Schritte beziehen sich auf die Verwendung des **integrierten Terminals in Visual Studio Code**.
```

`````{tab-set}
:sync-group: os
````{tab-item} Windows
:sync: win
**Erstellen einer virtuellen Umgebung im Ordner** `.venv`
```{code-block} console
python -m venv .venv
```
**Aktivieren der Umgebung**
```{code-block} console
.venv\Scripts\Activate.ps1
```

Falls die Ausführung blockiert ist:
```{code-block} console
Set-ExecutionPolicy -Scope Process Bypass
```
*(wirkt nur für die aktuelle Session)*

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

````{tab-item} macOS
:sync: mac
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
`````

Nach diesen Schritten steht eine **isolierte, reproduzierbare Python-Umgebung** zur Verfügung, die als Grundlage für alle weiteren Installations- und Konfigurationsschritte im Sphinx-Projekt dient.

## Installation

Bevor mit Sphinx gearbeitet werden kann, muss das Framework zunächst in der Python-Umgebung installiert werden. Die Installation kann grundsätzlich global oder innerhalb einer virtuellen Umgebung erfolgen. Für alle produktiven Projekte wird jedoch ausdrücklich die Verwendung einer **virtuellen Umgebung** empfohlen (siehe vorherigen Abschnitt).

Die Installation erfolgt über den Python-Paketmanager `pip` im Terminal.

```{code-block} console
:caption: Installation von Sphinx
:linenos:

python -m pip install sphinx
```

Dabei wird Sphinx als zentrales Dokumentationsframework installiert.\
Nach erfolgreicher Installation stehen alle grundlegenden Werkzeuge zur Erstellung und zum lokalen Testen einer Sphinx-Dokumentation zur Verfügung.

(Erstellen der Dokumentation)=
## Erstellen der Dokumentation

Die Erstellung eines neuen Sphinx-Projekts erfolgt direkt über die Kommandozeile. Gehe hierfür in das Verzeichnis, in dem die neue Dokumentation gespeichert werden soll.

```{note}
Unter **Windows** kann im gewünschten Ordner durch klicken mit der **rechten Maustaste** und *In Terminal öffnen* ein neues Terminal geöffnet werden.

Unter **macOS** kann schlicht auf den gewünschten Zielordner mit der **rechten Maustaste** geklickt werden und ein Terminal durch *Neues Terminal beim Ordner* geöffnet werden.

In **beiden** Betriebssystemen ist zum einen das navigieren im Terminal mit `cd` möglich, zum anderen kann das Terminal in VS Code verwendt werden (hier muss der Zielordner im Explorer von VS Code geöffnet sein).
```

In dem nun geöffneten Terminal kann nun durch die Eingabe von `sphinx-quickstart` und anschließende Bestätigung durch {kbd}`Enter` die Erstellung einer neuen Dokumentation gestartet werden. 

```{code-block} console
:caption: Neue Dokumentation erstellen
:linenos:

sphinx-quickstart
```

Daraufhin können einige Spezifikationen für die Dokumentation festgelegt werden. Im folgenden Beispiel wurden die **gelb markierten** Einträge gesetzt, alle übrigen durch einfaches Bestätigen mit {kbd}`Enter` leer übernommen.

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

```{admonition} Einordnung der beim Quickstart gesetzten Parameter
:class: note

Während des `sphinx-quickstart` werden grundlegende Eigenschaften der Dokumentation festgelegt.\
Die meisten dieser Parameter können später in der Datei `conf.py` angepasst werden.

Besonders relevant sind dabei:

- **Separate source- und build-Verzeichnisse**\
    Durch die Trennung von Quelltext (source) und erzeugter Ausgabe (build) bleibt die Projektstruktur übersichtlich.\
    Änderungen betreffen ausschließlich die Quelldateien, während erzeugte Artefakte klar isoliert sind.

- **Projektsprache (`language = de`)**\
    Diese Einstellung beeinflusst automatisch generierte Texte (z. B. Suchfeld, Inhaltsverzeichnis) und ist insbesondere für deutschsprachige Dokumentationen sinnvoll.

- **Index-Datei (`index.rst`)**\
    Die erzeugte `index.rst` fungiert als Einstiegspunkt der gesamten Dokumentation.\
    Über sie wird die logische Struktur der Inhalte definiert.
```

Nach Abschluss aller Eingaben wurde das Standardgerüst eines neuen Sphinx-Projekts erzeugt:

```{code-block} none
:caption: Ordnerstruktur eines neuen Sphinx-Projekts
:emphasize-lines: 6, 7

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

Nach dem Initialisieren des Projekts sind insbesondere zwei Dateien von zentraler Bedeutung:

- `conf.py`\
    Enthält sämtliche Konfigurationsparameter der Dokumentation (Erweiterungen, Layout, Sprache, Build-Verhalten).\
    Diese Datei bildet das technische Herzstück des Projekts.
- `index.rst`\
    Definiert den Einstieg und die Navigationsstruktur der Dokumentation.\
    Alle weiteren Seiten werden direkt oder indirekt über diese Datei eingebunden.

Die Ordner `_static` und `_templates` sind für spätere optische Anpassungen vorgesehen und bleiben im Quickstart zunächst unverändert.

### Statischer HTML-Build

Der Befehl

```{code-block} console
:caption: statische HTML-Seite generieren
:linenos:

sphinx-build -b html source build/html
```

erzeugt eine statische **HTML-Version** der Dokumentation.\
Jede Änderung an den Quelldateien erfordert einen erneuten Build, damit sie im Browser sichtbar wird.

Für die kontinuierliche Arbeit an der Dokumentation empfiehlt sich daher eine Live-Vorschau mit automatischem Neuladen, die im nächsten Abschnitt behandelt wird.

Nach Durchführung des HTML-Build kann nun durch **Doppelklick** die Datei `index.html` unter `build/html/` im Browser geöffnet werden und der bisherige Stand der Dokumentation begutachtet werden.

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

Sphinx stellt eine Vielzahl vordefinierter Themes bereit, mit denen sich das Erscheinungsbild der generierten Dokumentation anpassen lässt.\
Ein Theme beeinflusst dabei unter anderem:

- die Seitennavigation,
- die Typografie,
- Farben und Abstände,
- sowie die Darstellung von Codeblöcken und Hinweisen.

Eine Übersicht verfügbarer Themes findet sich auf der Website von Write the Docs unter\
[https://www.writethedocs.org/guide/tools/sphinx-themes/](https://www.writethedocs.org/guide/tools/sphinx-themes/)

Für diese Dokumentation wird das weit verbreitete **Read the Docs** Theme verwendet, da es sich besonders für **technische Dokumentationen** bewährt hat und eine klare, gut strukturierte Navigation bietet.

### Installation des Themes

Themes werden in Sphinx als Python-Pakete bereitgestellt und können daher direkt über den Paketmanager `pip` installiert werden.\
Die Installation erfolgt innerhalb der aktuell aktiven Python-Umgebung (idealerweise einer virtuellen Umgebung).

```{code-block} console
:caption: Read the Docs installieren
:linenos:

python -m pip install sphinx-rtd-theme
```

Nach erfolgreicher Installation steht das Theme dem Sphinx-Projekt zur Verfügung, ist jedoch noch nicht aktiv.

### Einbindung des Themes

Die Auswahl und Konfiguration des Themes erfolgt über die Datei `conf.py`.\
Diese Datei befindet sich im `source`-Verzeichnis des Projekts und fungiert als zentrale Konfigurationsdatei der gesamten Dokumentation.

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

Nach dem Ausführen von `sphinx-quickstart` enthält die `conf.py` standardmäßig folgende relevante Einstellung:

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

Das Theme `alabaster` ist das von Sphinx voreingestellte Standard-Theme. Um stattdessen das **Read the Docs** Theme zu verwenden, wird diese Einstellung angepasst.

Lösche die markierte Zeile und ergänze unterhalb von `html_static_path = ['_static']` folgenden Abschnitt:

```{code-block} python
:caption: Theme festlegen
:linenos:

# -- Theme Einstellungen -----------------------------------------------------
html_theme = 'sphinx_rtd_theme' # default: 'alabaster'
```

Die Trennung der Theme-Einstellungen in einen eigenen Abschnitt erhöht die Übersichtlichkeit der Konfigurationsdatei und erleichtert spätere Anpassungen.

### Dokumentation neu rendern

Damit die Änderungen wirksam werden, muss die Dokumentation erneut gebaut werden:

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

### Automatische Jahresangabe im Copyright (optional)

Standardmäßig wird das Copyright-Jahr in der `conf.py` als fester Wert hinterlegt.\
Für langfristige Projekte ist es sinnvoll, dieses Jahr automatisch aus dem aktuellen Systemdatum zu erzeugen.

Hierzu kann die `conf.py` minimal erweitert werden.\
Dabei ist zu beachten, dass die Variable `author` vor c`opyright` definiert sein muss.

```{code-block} python
:caption: Automatische Jahresangabe im Copyright
:linenos:
:emphasize-lines: 1, 5

from datetime import date

project = 'Sphinx'
author = 'Tobias Reichart'
copyright = f'{date.today().year}, {author}'
```

### Konfigurationsdatei nach den ersten Anpassungen

Nach den beschriebenen Änderungen ergibt sich folgende konsolidierte Fassung der `conf.py`:

```{code-block} python
:caption: Konfigurationsdatei nach den ersten Anpassungen
:linenos:

from datetime import date # für copyright Jahr

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sphinx'
author = 'Tobias Reichart'
copyright = f"{date.today().year}, {author}"

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
```

(sphinx-autobuild)=
## Live-Vorschau mit sphinx-autobuild

Während der aktiven Arbeit an einer Sphinx-Dokumentation ist es wenig effizient, nach jeder Änderung einen vollständigen manuellen Build auszuführen.\
Für diesen Zweck stellt Sphinx mit `sphinx-autobuild` ein Werkzeug zur Verfügung, das eine **Live-Vorschau** im Browser ermöglicht.

`sphinx-autobuild` überwacht das Projektverzeichnis kontinuierlich und startet automatisch einen neuen Build, sobald eine Quelldatei gespeichert wird (z. B. mit {kbd}`Strg` + {kbd}`S`).\
Die aktualisierte Dokumentation wird anschließend unmittelbar im Browser neu geladen.

### Installation von sphinx-autobuild

Die Installation erfolgt, wie bei allen Sphinx-Erweiterungen, über den Python-Paketmanager `pip` innerhalb der aktiven Python-Umgebung:

```{code-block} console
:caption: sphinx-autobuild installieren
:linenos:

python -m pip install sphinx-autobuild
```

Nach erfolgreicher Installation steht das Kommando `sphinx-autobuild` im Terminal zur Verfügung.

### Starten der Live-Vorschau

Der Live-Build wird direkt aus dem Projektverzeichnis heraus gestartet:

```{code-block} console
:caption: Live-Build mit sphinx-autobuild starten
:linenos:

sphinx-autobuild source build/html
```

Dabei gilt:

- `source` bezeichnet das Verzeichnis mit den Quelldateien (`.rst`, `.md`),
- `build/html` ist das Zielverzeichnis für die erzeugte HTML-Ausgabe.

Beim Start führt `sphinx-autobuild` zunächst einen **vollständigen Initial-Build** aus.\
Anschließend wird ein lokaler Webserver gestartet und auf Dateiänderungen gewartet.

#### Konsolenausgabe und lokale Serveradresse

Nach dem erfolgreichen Start erscheint in der Konsole eine Ausgabe ähnlich der folgenden:

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

Die angegebene Adresse `http://127.0.0.1:8000` ist die **lokale Serveradresse**, unter der die Dokumentation im Browser aufgerufen werden kann.\
Falls sich der Browser nicht automatisch öffnet, kann die Adresse:

- manuell in die Adresszeile kopiert werden, oder
- bei gedrückter {kbd}`Strg`-Taste direkt aus dem Terminal angeklickt werden.

```{admonition} Technischer Hintergrund: 127.0.0.1 (Loopback-Adresse)
:class: note

Die IP-Adresse `127.0.0.1` bezeichnet die sogenannte **Loopback-Schnittstelle** des eigenen Rechners. Sie verweist immer auf das **lokale System** selbst und ist unabhängig von einer Internetverbindung erreichbar.\
Der Live-Server ist somit:

- ausschließlich lokal verfügbar,
- nicht von außen erreichbar,
- und ausschließlich für Entwicklungszwecke gedacht.
```

Sobald eine Markdown- oder reStructuredText-Datei geändert und gespeichert wird, erkennt `sphinx-autobuild` die Änderung automatisch. Im Hintergrund wird erneut `sphinx-build` ausgeführt, und der Browser lädt die betroffene Seite ohne manuelles Zutun neu.\
Dieser Workflow ermöglicht:

- sofortiges visuelles Feedback,
- iteratives Arbeiten an Text und Layout,
- und ein deutlich effizienteres Schreiben größerer Dokumentationen.

Der Live-Server läuft dabei blockierend im Terminal und bleibt aktiv, bis der Prozess mit {kbd}`Strg` + {kbd}`C` beendet wird.

```{hint}

`sphinx-autobuild` ersetzt nicht den finalen HTML-Build, sondern dient ausschließlich der **lokalen Entwicklung**. Für produktive Builds (z.B. für **GitHub Pages** oder **PDF-Export**) wird weiterhin ein regulärer `sphinx-build` verwendet.
```

### Live-Vorschau über eine Verknüpfung starten

Für den täglichen Entwicklungsworkflow ist es oft komfortabler, die Live-Vorschau **nicht über manuelle Terminalbefehle**, sondern per **Doppelklick** zu starten.\
Dies lässt sich sowohl unter Windows als auch unter macOS über kleine Startskripte realisieren.\
Die Dokumentation wird dabei automatisch:

- im Projektverzeichnis gebaut,
- im Browser geöffnet,
- und bei jeder Änderung erneut gerendert.

`````{tab-set}
:sync-group: os
````{tab-item} Windows
:sync: win

1. Lege im Projektverzeichnis eine neue Batch-Datei mit der Endung `.bat` an.
2. Füge den folgenden Inhalt ein und speichere die Datei:

```{code-block} console
:caption: Autobuild über Batch-Datei (Windows)
:linenos:

@echo off
setlocal
rem In das Verzeichnis der Batch-Datei wechseln
pushd "%~dp0"

rem Virtuelle Umgebung aktivieren, falls vorhanden
if exist ".venv\Scripts\activate.bat" call ".venv\Scripts\activate.bat"

rem Live-Server mit aktivem dev-Tag starten
sphinx-autobuild source build/html --open-browser

rem Aufräumen nach Beenden
popd
endlocal
```

3. *(Optional)*\
   Über **Rechtsklick $\rightarrow$ Weitere Optionen anzeigen $\rightarrow$ Verknüpfung erstellen** kann eine Verknüpfung erzeugt werden, die anschließend frei auf dem System platziert werden kann (z.B. Desktop oder Taskleiste).
````

````{tab-item} macOS
:sync: mac

1. Lege im Projektverzeichnis eine neue Datei mit der Endung `.command` an.
2. Füge den folgenden Inhalt ein und speichere die Datei:

```{code-block} console
:caption: Autobuild über Command-Datei (macOS)
:linenos:

#!/usr/bin/env bash

# In das Verzeichnis der Skriptdatei wechseln
cd "$(dirname "$0")" || exit 1

# Virtuelle Umgebung aktivieren, falls vorhanden
if [ -f ".venv/bin/activate" ]; then
    source ".venv/bin/activate"
fi

# Entwickler-Build mit aktivem dev-Tag starten
sphinx-autobuild source build/html --open-browser
```

3. Mache die Datei einmalig über das Terminal ausführbar:

```{code-block} console
:caption: Datei ausführbar machen
:linenos:

chmod +x <Dateiname>.command
```

4. *(Optional)*\
   Über **Rechtsklick $\rightarrow$ Alias erzeugen** kann eine Verknüpfung erstellt und an einen beliebigen Ort verschoben werden.
````
`````

```{note}

- Das Skript startet den Live-Server **blockierend** im Terminal.\
    Das Terminalfenster muss geöffnet bleiben, solange die Live-Vorschau genutzt wird.
- Die virtuelle Umgebung wird automatisch aktiviert, sofern sie im Projektordner als `.venv` existiert.
- Der Build erfolgt ausschließlich lokal über `127.0.0.1` und ist nicht von außen erreichbar.
```

## Umbau von reStructuredText auf MyST-Markdown

(*reStructuredText bleibt weiterhin vollständig nutzbar*)

In dieser Dokumentation wird künftig **MyST-Markdown** als bevorzugtes Quellformat verwendet. Bestehende Inhalte in reStructuredText (`.rst`) können jedoch weiterhin parallel genutzt werden.

Der Build-Prozess bleibt dabei für HTML- als auch für PDF-Ausgaben vollständig Sphinx-kompatibel.\
Ein vollständiger Umbau bestehender Inhalte ist daher nicht erforderlich.

### Motivation für den Einsatz von Markdown

Die Umstellung auf MyST-Markdown bietet mehrere praktische und konzeptionelle Vorteile:

- **Reduzierte syntaktische Komplexität**\
    Markdown ist weniger fehleranfällig und ermöglicht schnelleres Schreiben.
- **Hohe Verbreitung**\
    Markdown wird von zahlreichen Editoren, Plattformen und Werkzeugen nativ unterstützt.
- **Kein Funktionsverlust gegenüber reST**\
    MyST unterstützt sämtliche Sphinx-Direktiven und Rollen\
    (z.B. `toctree`, Code-Blöcke, mathematische Formeln, `literalinclude`, Admonitions).
- **Erweiterbarkeit**\
    Mit Zusatzpaketen wie `myst-nb` lassen sich auch Jupyter-Notebooks direkt integrieren.

MyST-Markdown verbindet damit die Einfachheit von Markdown mit der Ausdrucksstärke von Sphinx.

### Installation der Voraussetzungen

Damit Sphinx Markdown-Dateien interpretieren kann, muss der **MyST-Parser** installiert werden.\
Die Installation erfolgt innerhalb der aktiven Python-Umgebung über `pip`:

```{code-block} console

python -m pip install myst-parser
```

Für Live-Vorschau und automatisches Neurendern kann weiterhin `sphinx-autobuild` verwendet werden (siehe Abschnitt {ref}`sphinx-autobuild`).

### Aktivierung von MyST in der Konfiguration

Nach der Installation wird der MyST-Parser in der Datei `conf.py` aktiviert.\
Die Konfiguration erlaubt dabei explizit die parallele Nutzung von **reST und Markdown**.

Öffne `conf.py` und ergänze am Ende der Datei folgenden Abschnitt:

```{code-block} python
:caption: MyST-Markdown und reST parallel aktivieren
:linenos:

# -- Umbau von rst auf MySt-Markdown -----------------------------------------
extensions.append('myst_parser') # MyST-Markdown aktivieren
root_doc = 'index'               # Einstiegspunkt der Dokumentation
# (bei älteren Sphinx-Versionen: master_doc = 'index')

# Gleichzeitige Unterstützung von reST und Markdown
source_suffix = {
    '.rst': 'restructuredtext',
    '.md':  'markdown',
}

# sinnvolle MyST-Erweiterungen
myst_enable_extensions = [
    # Liste der MyST-Erweiterungen, die aktiv sind
    "colon_fence",   # :::-Direktiven (Alternative zu ```{note})
    "dollarmath",    # Inline- und Block-Mathe mit $...$ / $$...$$
    "amsmath",       # LaTeX-Umgebungen wie align, gather, …
    "deflist",       # Definitionslisten im Markdown-Stil
    "tasklist",      # Aufgabenlisten mit Checkboxen
]
```

Diese Konfiguration stellt sicher, dass:

- bestehende reST-Dateien weiterhin funktionieren
- und neue Inhalte bevorzugt in Markdown geschrieben werden können.

### Startseite auf Markdown umstellen

Zum Abschluss wird die zentrale Startseite der Dokumentation von `index.rst` auf `index.md` umgestellt.\
Dazu genügt es, die Datei umzubenennen (Rechtsklick $\rightarrow$ Umbenennen oder {kbd}`F2`).

Ein minimaler Inhalt der neuen `index.md` könnte beispielsweise so aussehen:

```{code-block} markdown
:caption: index.md (Beispiel)
:linenos:

# Sphinx

Das weitere Vorgehen wird im nächsten Kapitel "Struktur und Navigation" erläutert.
```

Beim nächsten Build erkennt Sphinx automatisch sowohl `.rst`- als auch `.md`-Dateien.\
Der Umstieg von reStructuredText auf MyST-Markdown kann somit schrittweise und ohne Brüche erfolgen.