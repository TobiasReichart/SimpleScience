# Struktur, Navigation und Schreiben

Nun wollen wir uns die **konzeptionellen Grundlagen** einer Sphinx-Dokumentation ansehen. Zentrale Fragestellungen sind: Wie werden Inhalte strukturiert, wie entsteht die Navigation und wie schreiben wir gut lesbare technische Texte.

Ziel ist es, von Beginn an eine skalierbare, wartbare und konsistente Dokumentationsstruktur aufzubauen, die **unabhängig von der Seitenzahl** auf viele Szenarien anwendbar ist.

## Der ToC Tree

Der **Toctree** ist das zentrale Strukturelement jeder Sphinx-Dokumentation. Er definiert **nicht nur die Navigation**, sondern auch, **welche Dateien überhaupt Teil des Builds sind**.

```{important}
Eine Seite, die **nicht** über einen Toctree eingebunden ist,\
wird von Sphinx **nicht gerendert** und erscheint weder in der Navigation noch im Suchindex

Der MyST-Parser gibt bei nicht eingebundenen Dateien auch eine Warnung aus:\
`D:\SimpleScience\source\sphinx\section\struktur.md: WARNING: document isn't included in any toctree [toc.not_included]`
```

### Grundprinzip

Ein Toctree ist eine Direktive, die auf andere Dokumente verweist:

````{code-block} markdown
:caption: Einfacher Toctree
:linenos:

```{toctree}
:maxdepth: 2
:caption: Inhaltsverzeichnis

installation
struktur-navigation
layout
```
````

Dabei gilt:

- jede Zeile verweist auf **eine Datei ohne Dateiendung**
- die Reihenfolge bestimmt die **Reihenfolge in der Navigation**
- `:maxdepth:` steuert, wie tief Überschriften eingeblendet werden
- `:caption:` erzeugt die Überschrift, die in der Sidebar über den anwählbaren Seitenlinks angezeigt wird
- Die Hauptüberschrift eines Artikels `# ...` aus der ersten Zeile wird als verlinkter Text in der Sidebar angezeigt (hier: Installation, Struktur und Navigation, Layout)

```{figure} ../_static/img/sphinx/struktur/toctree.png
:width: 40%
:align: center

Einfacher Toctree in der Sidebar
```

## Die Rolle von `index`-Dateien

`index.md` (oder `index.rst`) fungiert in Sphinx als **Einstiegspunkt eines Abschnitts**.

### Wann braucht man eine `index`-Datei?

Immer dann, wenn:

- ein Abschnitt **mehrere Unterseiten** besitzt
- eine **eigene Navigationsebene** entstehen soll
- ein Kapitel **inhaltlich eingerahmt** werden soll (Einleitung, Überblick)

```{code-block} none
:caption: Typische Abschnittsstruktur
:linenos:

section/
├ index.md
├ installation.md
├ struktur-navigation.md
└ layout.md
```

Die `index.md`:

- enthält eine inhaltliche Einführung
- definiert einen lokalen Toctree
- bildet die Übersichtsseite des Kapitels
- nur die `:caption:` des Toctrees der obersten `index.md` wird als Titel in der Sidebar angezeigt

### Die Ordnerstruktur des Inhalts

Sphinx zwingt bewusst keine feste Ordnerstruktur auf. Gute Dokumentationen folgen jedoch klaren Konventionen.

Bewährtes Grundmuster

```{code-block} none
:caption: Empfohlene Inhaltsstruktur
:linenos:
:emphasize-lines: 3

source/
├ index.md
├ section/
│ ├ index.md
│ ├ installation.md
│ ├ struktur-navigation.md
│ └ layout.md
├ _static/
└ conf.py
```

Prinzipien dahinter:

- ein Ordner = ein thematischer Block
- keine tiefen Ordnerhierarchien
- Navigation entsteht logisch, nicht technisch

```{note}
Die Ordnerstruktur dient primär der **Autorenorganisation**.\
Die sichtbare Navigation wird ausschließlich durch Toctrees bestimmt.
```

## Navigationsdesign

Die Navigation in Sphinx ist strukturgetrieben, nicht layoutgetrieben.\
Das bedeutet:

- keine manuelle Menüdefinition
- keine separate Navigationsdatei
- vollständige Ableitung aus Überschriften + Toctrees

**Ebenen der Navigation**

1. Seitennavigation (Toctree)
2. Inhaltsnavigation (Überschriften innerhalb einer Seite)
3. Vor-/Zurück-Links (automatisch generiert)

## Schreiben in Sphinx (MyST-Markdown)

Sphinx mit MyST-Markdown kombiniert **wissenschaftliche Struktur** mit **lesbarer Syntax**.

### Überschriften

```{code-block} markdown
:caption: Überschriften
:linenos:

# Kapitel
## Abschnitt
### Unterabschnitt
```

Regel:

- eine `#`-Überschrift **pro Datei**
- konsistente Hierarchie
- keine Sprünge (nicht von `##` zu `####`)

### Hervorhebungen

```{code-block} markdown
:caption: Hervorhebungen
:linenos:

*Kursiv*  
**Fett**  
***Fett + kursiv***
```

Empfohlene Nutzung:

- *Kursiv* $\rightarrow$ Begriffe, Betonung
- **Fett** $\rightarrow$ Kernaussagen, Definitionen
- ***Fett + kursiv*** $\rightarrow$ sparsam einsetzen

### Zitate und eingerückter Text

```{code-block} markdown
:caption: Zitate und eingerückter Text
:linenos:

> Dies ist ein eingerückter Absatz.
```

> Dies ist ein eingerückter Absatz.

Dieses Stilmittel kann sehr gut für Einordnungen, Kommentare oder Meta-Erläuterungen verwendet werden.

### Listen

```{code-block} markdown
:caption: Listen
:linenos:

- ungeordnete Liste
  - Unterpunkt der Liste\
    weitere Zeile des Unterpunkts
- weiterer Punkt

1. nummerierte Liste\
  1.1. Stichpunkt zu 1.
2. zweiter Punkt
```

```{admonition} Gerendertes Listenbeispiel
:class: note

- ungeordnete Liste
  - Unterpunkt der Liste\
    weitere Zeile des Unterpunkts
- weiterer Punkt

1. nummerierte Liste\
  1.1. Stichpunkt zu 1.
2. zweiter Punkt
```

Listen sollten:

- semantisch zusammengehören
- nicht zu lang sein
- konsistent formatiert werden
- durch Einrückungen und erzwungene Zeilenumbrüche nicht zu komplex gestaltet werden

### Inline-Formatierungen

Sphinx bietet eine Vielzahl von Rollen zur Formatierung von Text, insbesondere für Befehle, Dateipfade, Tasten und Benutzeroberflächen. Hier sind einige der wichtigsten:

```{list-table} Inline-Formatierungen
  :header-rows: 1

  * - Rolle
    - Syntax
    - Beispiel
  * - `{kbd}`
    - ``` {kbd}`Strg` ```
    - {kbd}`Strg`
 * - `{file}`
    - ``` {file}`C:\Pfad\Datei.txt` ```
    - {file}`C:\Pfad\Datei.txt`
  * - `{menuselection}`
    - ``` {menuselection}`Datei --> Neu` ```
    - {menuselection}`Datei --> Neu`
  * - `{guilabel}`
    - ``` {menuselection}`OK` ```
    - {guilabel}`OK`
  * - `{command}`
    - ``` {command}`git commit` ```
    - {command}`git commit`
  * - `{abbr}`
    - ``` {abbr}`HTML (HyperText Markup Language)` ```
    - {abbr}`HTML (HyperText Markup Language)`
  * - `{dfn}`
    - ``` {dfn}`Fourier-Transformation` ```
    - {dfn}`Fourier-Transformation`
  * - `{samp}`
    - ``` {samp}`python {script}.py` ```
    - {samp}`python {script}.py`
```

### Typografie und Lesbarkeit

Eine gute Dokumentation ist nicht nur korrekt, sondern **lesbar**.

Grundregeln:

- kurze Absätze
- ein Gedanke pro Absatz
- ausreichende Weißräume
- klare Überschriften

#### Zeilenumbrüche und Absätze in Markdown

In Markdown wird zwischen **Zeilenumbrüchen** und **Absätzen** unterschieden.

- Ein Absatz entsteht durch **eine leere Zeile** zwischen zwei Textblöcken.
- Ein **erzwungener Zeilenumbruch innerhalb eines Absatzes** kann durch einen Backslash (`\`) am Zeilenende erzeugt werden.


```{code-block} markdown
:caption: Zeilenumbrüche und Absätze in Markdown
:linenos:

Dies ist ein Absatz mit erzwungenem Zeilenumbruch.\
Die beiden Zeilen gehören weiterhin zum selben Absatz.

Dies ist ein neuer Absatz, da zwischen den Textblöcken
eine leere Zeile steht. Der Zeilenumbruch von Zeile 4 auf 5 wird ignoriert.
```

```{admonition} Gerendertes Zeilenumbruch und Absatz Beispiel
:class: note

Dies ist ein Absatz mit erzwungenem Zeilenumbruch.\
Die beiden Zeilen gehören weiterhin zum selben Absatz.

Dies ist ein neuer Absatz, da zwischen den Textblöcken
eine leere Zeile steht. Der Zeilenumbruch von Zeile 4 auf 5 wird ignoriert.
```

## Rechtschreibprüfung und Textqualität

Neben einer sauberen Struktur und konsistentem Layout ist die **sprachliche Qualität** essentiell für die Verständlichkeit und Seriosität einer Dokumentation. Gerade in umfangreichen Sphinx-Projekten mit vielen Markdown-Dateien ist eine manuelle Rechtschreibprüfung weder effizient noch zuverlässig.\
Für die kontinuierliche Qualitätssicherung empfiehlt sich daher der Einsatz einer Editor-gestützten Rechtschreibprüfung.

### Rechtschreibprüfung in Visual Studio Code

Wenn **Visual Studio Code** als Editor verwendet wird, können zahlreiche leistungsfähige Erweiterungen verwendet werden, die dateiformatübergreifende Rechtschreibprüfung ermöglichen.

Bewährt haben sich insbesondere die folgenden Erweiterungen:

- **Code Spell Checker**\
    Allgemeine Rechtschreibprüfung für Quelltexte, Markdown und Konfigurationsdateien.\
    siehe: [https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)

```{figure} ../_static/img/sphinx/struktur/code_spell_checker.png
:width: 80%
:align: center

Code Spell Checker Erweiterung in VS Code
```

- **German Code Spell Checker**\
    Ergänzt deutsche Wörterbücher und reduziert Fehlalarme in deutschsprachigen Texten.\
    siehe: [https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker-german](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker-german)

```{figure} ../_static/img/sphinx/struktur/german_code_spell_checker.png
:width: 80%
:align: center

German Code Spell Checker Erweiterung in VS Code
```

**Vorteile einer integrierten Rechtschreibprüfung**\
Der Einsatz einer Editor-basierten Lösung bietet mehrere Vorteile:

- Echtzeit-Feedback beim Schreiben
- Formatunabhängigkeit (Markdown, reST, Python, YAML, …)
- Keine Beeinflussung des Builds (rein editorseitig)
- Konsistente Terminologie über das gesamte Projekt hinweg

```{note}

Die Rechtschreibprüfung erfolgt ausschließlich im Editor.\
Sie hat **keinen Einfluss** auf den Sphinx-Build und erzeugt keine Warnungen oder Fehler beim Rendern der Dokumentation.
```

### Einbindung der Einstellungen in VS Code

Nach der Installation der beiden Erweiterungen erfolgt die Konfiguration über die Datei `settings.json`. Für Dokumentationsprojekte empfiehlt sich eine **projektlokale** Konfiguration, damit:

- alle Mitwirkenden dieselben Regeln nutzen,
- globale VS-Code-Einstellungen unberührt bleiben.

Diese Einstellungsdatei kann entweder über die Workspace-Einstellungen direkt in Visual Studio Code durch die Tastenkombination {kbd}`Strg` + {kbd}`Shift` + {kbd}`P` und den Befehl\
`Preferences: Open Workspace Settings (JSON)` erstellt und auch bearbeitet werden.\
VS Code legt dabei automatisch die Datei `.vscode/settings.json` im Projekt an.

Alternativ kann manuell der Ordner `.vscode` und darin die Datei `settings.json` angelegt werden. VS Code erkennt die Datei Automatisch als projektlokale Konfigurationsdatei.

```{code-block} none
:caption: Konfigurationsdatei

Sphinx-Projekt
└ .vscode/
  └ settings.json
```

In dieser Datei können nun die folgenden Konfigurationen eingefügt werden. Diese Einstellungen haben sich während der Arbeit am Projekt SimpleScience als sinnvoll erwiesen.

```{code-block} json
:caption: Konfiguration des Code Spell Checker
:linenos:

{
  "cSpell.enabled": true,             // Erweiterung für das Projekt aktivieren
  "cSpell.language": "de",            // Deutsch als primäre Prüfsprache
  "cSpell.allowCompoundWords": true,  // Erlaubt deutsche Komposita
  "cSpell.languageSettings": [
    {
      "languageId": "python",         // Rechtschreibprüfung in Python, für
      "includeRegExpList": [
        "comments",                   // Kommentare
        "strings"                     // Docstrings und String-Literalen
      ]
    }
  ],
  "cSpell.words": [                   // Liste für manuell erlaubte Wörter

  ],
}
```

### Wörter zur Liste der erlaubten Begriffe hinzufügen

Bei der Arbeit an technischen Dokumentationen kommt es regelmäßig vor, dass korrekt geschriebene **Fachbegriffe**, **Eigennamen** oder **projektspezifische Bezeichnungen** von der Rechtschreibprüfung als Fehler markiert werden.\
Diese Wörter sollten nicht ignoriert, sondern gezielt zur Liste der erlaubten Begriffe hinzugefügt werden.

In Visual Studio Code erfolgt dies komfortabel direkt aus dem Editor heraus:

- Ein als falsch markiertes Wort wird unterstrichen dargestellt.
- Über einen **Rechtsklick** auf das Wort öffnet sich das Kontextmenü.
- Mit der Option **Spelling** $\rightarrow$ **Add Words to Workspace Settings** wird der Begriff automatisch in die Datei `settings.json` unter `cSpell.words` eingetragen.

Der Begriff ist anschließend im gesamten Projekt als korrekt akzeptiert.

```{figure} ../_static/img/sphinx/struktur/woerterbuch.png
:width: 70%
:align: center

Wörter als erlaubte Begriffe setzen
```

```{note}
Wörter, die auf diese Weise hinzugefügt werden, gelten ausschließlich für den aktuellen Workspace und beeinflussen keine globalen VS-Code-Einstellungen.
```

### Rechtschreibvorschläge und Korrekturen

Neben dem Hinzufügen eigener Wörter bietet der Code Spell Checker auch **kontextsensitive Korrekturvorschläge**:

- Bei einem erkannten Schreibfehler zeigt VS Code eine Liste möglicher Alternativen an.
- Diese Vorschläge basieren auf dem aktiven Wörterbuch sowie der Umgebung (Deutsch / Englisch).
- Die gewünschte Korrektur kann direkt ausgewählt und übernommen werden.

```{figure} ../_static/img/sphinx/struktur/spelling.png
:width: 60%
:align: center

Rechtschreibvorschläge abfragen
```

```{tip}

Bevor ein neues Wort dauerhaft zur Wörterliste hinzugefügt wird, sollte geprüft werden,  
ob es sich tatsächlich um einen Fachbegriff handelt oder lediglich um einen einmaligen Tippfehler.
```