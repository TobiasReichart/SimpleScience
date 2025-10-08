# Installation & erste Schritte

In diesem Abschnitt wollen wir die Dokumentation zum *"laufen"* bringen und die ersten optischen Anpassungen vornehmen.

```{attention}
**Hinweis**: Die folgenden Schritte zur Installation von Sphinx dienen ausschließlich der Orientierung. Installationsroutinen, Systemvoraussetzungen und Benutzeroberflächen können je nach Betriebssystem und Version variieren.  

Vor der Durchführung lies bitte meinen {ref}`Haftungsausschluss <disclaimer>`. Ich übernehme keine Verantwortung für eventuelle Schäden oder Fehlkonfigurationen.  

Voraussetzung für die Installation von Sphinx ist eine bereits installierte Version von Python.
```

```{note}
Es wird **dringend empfohlen**, Sphinx-Projekte in einer *virtuellen Umgebung* (`venv`) aufzubauen.<br>
So bleibt die Arbeitsumgebung stabil, unabhängig von globalen Paketen und jederzeit reproduzierbar.  

Auf diese Weise verhinderst du Versionskonflikte, hältst dein System sauber und stellst sicher, dass deine Dokumentation auch in Zukunft zuverlässig gebaut werden kann.<br>
Nähere Informationen findest du auf meiner Infoseite zu {ref}`Virtuellen Umgebungen <Virtuelle Umgebungen>`.
```

## Virtuelle Umgebungen (Quickstart)

```{dropdown} macOS/Linux

```

```{dropdown} Windows

```

## Installation

Bevor du mit Sphinx arbeiten kannst, musst du es zunächst in deiner Python-Umgebung (**Global** oder in der **Virtuellen Umgebung**)installieren.<br>
Am einfachsten gelingt das über den Python-Paketmanager `pip`. Führe dazu im Terminal den folgenden Befehl aus:

```{code-block} console
:caption: Installation von Sphinx
:linenos:

pip install sphinx
```

## Erstellen der Dokumentation

Die Erstellung eines neuen Sphinx-Projekts erfolgt direkt über die Kommandozeile.  
Gehe dazu in das Verzeichnis, in dem deine Dokumentation gespeichert werden soll.

```{note}
Unter **Windows** kannst du im gewünschten Ordner mit der **rechten Maustaste** klicken und *In Terminal öffnen* wählen.<br>
Unter **macOS** kannst du auf den gewünschten Zielordner mit der **rechten Maustaste** klicken und *Neues Terminal beim Ordner* wählen.<br>
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
├ source
│   ├ conf.py
│   └ index.rst
├ make.bat
└ Makefile
```

Das Projekt kann anschließend durch Eingabe von `sphinx-build -b html source build/html` im Terminal als statische HTML-Seite generiert werden.

```{code-block} console
:caption: statische HTML-Seite generieren
:linenos:

sphinx-build -b html source build/html
```

Dabei wird automatisch der Ordner `build` mit dem Unterordner `html` erzeugt, der die Datei `index.html` enthält.<br>
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

```{figure} bilder/default-theme.png
:align: center
:width: 100%

Voreingestelltes Layout
```