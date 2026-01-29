(Sphinx Veröffentlichen)=
# Veröffentlichung mit GitHub Pages

## Github Pages


## Entwicklerbereiche nur lokal rendern

Bei der Veröffentlichung einer Sphinx-Dokumentation stellt sich ab einer gewissen Projektgröße häufig die Frage, wie **interne Entwickler-Inhalte** behandelt werden sollen, die nicht öffentlich auf der Website erscheinen dürfen.\
Typische Beispiele sind:

- persönliche Notizen
- TODO-Listen
- technische Skizzen
- unfertige Konzepte
- Build- oder Deployment-Hinweise

Diese Inhalte sollen lokal sichtbar, aber nicht öffentlich ausgeliefert werden. Sphinx bietet hierfür mit Tags und der Direktive `{only}` eine robuste und saubere Lösung.

### Grundidee: Tag-basierte Build-Trennung

Sphinx erlaubt es, Inhalte abhängig von gesetzten **Build-Tags** ein- oder auszublenden. Ein Inhalt wird nur dann gerendert, wenn der entsprechende Tag beim Build explizit gesetzt ist.

Konkret:
- **Lokaler Build**: mit Tag `dev`
- **Öffentlicher Build** (GitHub Pages): ohne diesen Tag

Fehlt der Tag, werden die entsprechenden Inhalte **bereits beim Parsen verworfen** und tauchen **weder im HTML noch im Suchindex** auf.

### Entwickler-Toctree nur lokal einbinden

Der empfohlene Ansatz besteht darin, den **gesamten Entwicklerbereich** über einen **eigenen Toctree** einzubinden, der mit `{only} dev` geschützt ist.

`````{code-block} markdown
:caption: Entwickler Toctree in Haupt-index.md-Datei einbinden
:linenos:

````{only} dev
```{toctree}
:maxdepth: 1
:hidden:
:caption: Entwicklerbereich

dev/index
```
````
`````

Dabei wird in der obersten `index.md` des Projekts ein **einziger Einstiegspunkt** für den Entwicklerbereich definiert.\
Alle Seiten, die ausschließlich über diesen Toctree eingebunden werden, erscheinen nur dann, wenn beim Build der Tag `dev` gesetzt ist.

Es ist nicht notwendig, die im Entwicklerbereich enthaltenen Seiten selbst mit `{only} dev` zu versehen. Die Sichtbarkeit wird vollständig über den Toctree gesteuert.

Voraussetzung ist lediglich, dass diese Seiten **nicht zusätzlich an anderer Stelle eingebunden** oder verlinkt werden.

**Optional: zusätzliche Absicherung über** `exclude_patterns`

Für größere Projekte empfiehlt es sich, den Entwicklerbereich zusätzlich auf Parser-Ebene auszuschließen:

```{code-block} python
:caption: Absicherung über exclude_patterns (conf.py)
:linenos:

# --- Entwicklerbereich ---
exclude_patterns = []
if not tags.has("dev"):
    exclude_patterns.append("dev/**")
```

Damit werden Entwicklerseiten selbst dann nicht gebaut, wenn sie versehentlich öffentlich verlinkt werden.

### Lokaler Build mit Entwicklerbereich

Für den lokalen Build muss der Tag `dev` explizit gesetzt werden.

Mit `sphinx-autobuild`:

```{code-block} bash
:caption: Autobuild mit dev-Tag

sphinx-autobuild -b html -t dev source build/html
```

Alternativ ohne Autobuild:

```{code-block} bash
:caption: Standardbuild mit dev-Tag

sphinx-build -b html -t dev source build/html
```

### Lokaler Entwickler-Build per Skript automatisieren

Für den lokalen Entwicklungsprozess empfiehlt es sich, den Build mit aktivem Entwicklerbereich über ein Skript zu automatisieren.
Dadurch wird sichergestellt, dass stets der korrekte Build-Tag (dev) gesetzt ist und die Dokumentation konsistent gerendert wird.

`````{tab-set}
:sync-group: os
````{tab-item} Windows
:sync: win

1. Lege im Projektverzeichnis eine Batch-Datei (`.bat`) an.
2. Füge folgenden Inhalt ein und speichere die Datei:

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
sphinx-autobuild -b html -t dev source build/html --open-browser

rem Aufräumen nach Beenden
popd
endlocal
```

3. (Optional) Per Rechtsklick $\rightarrow$ Weitere Optionen anzeigen $\rightarrow$ Verknüpfung erstellen kann eine Verknüpfung erstellt werden.
````

````{tab-item} macOS
:sync: mac

1. Lege im Projektverzeichnis eine Command-Datei (`.command`) an.
2. Füge folgenden Inhalt ein und speichere die Datei:

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
sphinx-autobuild -b html -t dev source build/html --open-browser
```
3. Mache die Datei durch den folgenden Befehl über das Terminal ausführbar:
```{code-block} console
:caption: Datei ausführbar machen
:linenos:

chmod +x <Dateiname>.command
```

4. (Optional) Per Rechtsklick $\rightarrow$ Alias erzeugen kann eine Verknüpfung erstellt werden.
````
`````

Die Verknüpfung kann nun an einen beliebigen Ort verschoben werden.

Das Skript:

- wechselt automatisch in das Projektverzeichnis,
- aktiviert optional eine virtuelle Python-Umgebung,
- startet `sphinx-autobuild` mit gesetztem Build-Tag `dev`,
- öffnet die gerenderte Dokumentation direkt im Browser.

Alle mit `{only} dev` geschützten Inhalte sind damit lokal sichtbar.