# Code

Quellcode ist oft nicht nur "Dekoration", sondern ein **formales Beweismittel**. Er macht Schritte reproduzierbar, minimiert Interpretationsspielräume und erlaubt anderen Ergebnisse direkt nachzuvollziehen.\
Sphinx stellt dafür ein konsistentes System aus **Inlinecode**, **Codeblöcken**, **Syntax-Highlighting**, **Datei-Einbindungen** und **automatisierter API-Dokumentation** bereit.

## Inlinecode

Inlinecode dient dazu, kurze Bezeichner im Fließtext eindeutig als Code zu markieren, z.B.:

- Variablen (`x`, `omega`, `df`)
- Dateinamen (`conf.py`, `index.md`)
- Befehle (`sphinx-build`, `pip`)
- Module oder Funktionen (`numpy.fft`, `plt.plot`)

In MyST-Markdown wird Inlinecode mit Backticks (`` ` ``) gesetzt:

```{code-block} markdown
:caption: Inlinecode
:linenos:

Die Konfiguration erfolgt in `conf.py` über `html_theme_options`.
```

Inlinecode ist semantisch stark: Er signalisiert "dies ist wörtlich zu übernehmen".\
Für lange Ausdrücke oder mehrere Parameter ist ein Codeblock lesbarer.

## Codeblöcke

Codeblöcke sind sinnvoll, sobald

- mehrere Zeilen benötigt werden,
- Einrückungen relevant sind,
- Befehle kopierbar sein sollen,
- oder die Lesbarkeit im Textfluss leiden würde.

In MyST wird ein Codeblock als Direktive geschrieben:

````{code-block} markdown
:caption: Codeblöcke
:linenos:

```{code-block} python
print("Hello Sphinx")
```
````

```{figure} ../_static/img/sphinx/code/codeblock.png
:align: center
:width: 100%

```

### Caption und Zeilennummern

Captions und Zeilennummern und die Hervorhebung einzelner Zeilen sind besonders hilfreich, weil sie Referenzen ermöglichen wie beispielsweise *("siehe Zeile 1 bis 3 und 5")* ermöglichen:

````{code-block} markdown
:caption: Codeblöcke
:linenos:

```{code-block} python
:caption: Minimalbeispiel (Python)
:emphasize-lines: 1-3, 5
:linenos:

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```
````

- `:caption:` setzt eine Beschriftung (Titel) für den Codeblock; sie erscheint oberhalb des Blocks und dient als inhaltliche Einordnung sowie als Referenz im Text.
- `:emphasize-lines:` hebt die angegebenen Zeilen visuell hervor (hier Zeilen 1–3 und 5); sinnvoll, um in längeren Blöcken die relevanten Stellen zu markieren.
- `:linenos:` aktiviert Zeilennummern am linken Rand; erleichtert präzise Verweise im Fließtext und erhöht die Nachvollziehbarkeit bei Debugging/Erklärungen.

```{figure} ../_static/img/sphinx/code/codeblock-nummerriert.png
:align: center
:width: 100%

```

```{tip}
Wenn wir später Codeblöcke nummerieren (global), werden Captions zusätzlich wichtig, weil sie den Block inhaltlich eindeutig beschreiben.
```

## Syntax-Highlighting

Sphinx nutzt für Highlighting standardmäßig Pygments. Die Sprache wird neben den Direktiventyp gesetzt.\
`python`, `bash`, `console`, `json`, `toml`, `xml`, `css`, …

````{code-block} markdown
:caption: Codeblöcke
:linenos:

```{code-block} csharp
:caption: Klassen in C#

class Auto
{
    // Eigenschaften (Properties)
    public string Marke { get; set; }
    public string Modell { get; set; }
    public int Leistung { get; set; }

    // Konstruktor
    public Auto(string marke, string modell, int leistung)
    {
        Marke = marke;
        Modell = modell;
        Leistung = leistung;
    }

    // Methode
    public void WelchesAuto() => ConsoleWriteLine($"Es ist ein {Modell} {Marke} mit {Leistung} PS");
}
```
````

```{figure} ../_static/img/sphinx/code/syntax-highlight.png
:align: center
:width: 100%

```

Wichtige Einordnung: "console" vs. "bash"

- console eignet sich für Terminalausgaben mit Prompt
- bash für reine Shell-Skripte

Für Dokumentationen ist das relevant, weil sich Leser sonst fragen, was "Prompt" und was "Befehl" ist.

## Externe Dateien einbinden

Wenn Code nicht doppelt gepflegt werden soll, wird er aus Dateien eingebunden. Das ist insbesondere wichtig für längere Skripte, Beispielprojekte oder Quellcode, der wirklich ausführbar sein soll.

### Ablage von Quellcode

Ähnlich wie Bilder bewährt sich auch für Quellcode eine klare Trennung.

Fertiger Quellcode, den Sphinx direkt einbindet, liegt in `source/_static/`.

```{code-block} none
:caption: Empfohlene Ordnerstruktur
:emphasize-lines: 6, 7, 8

diagrams/                     ← Quellen (z.B. Mermaid)
plots/                        ← Quellen (z.B. Matplotlib)
source/
└ _static/
  └ code/
    ├ code1.py
    ├ code2.c
    └ code3.css
```

### Einbinden von Code mit `literalinclude`

````{code-block} markdown
:caption: Codeblöcke
:linenos:

```{literalinclude} ../_static/code/sphinx/code/rain.py
:language: python
:linenos:
:caption: Beispielskript (aus Datei)
```
````

```{literalinclude} ../_static/code/sphinx/code/rain.py
:language: python
:linenos:
:caption: Beispielskript (aus Datei)
```

Optionen, die in der Praxis besonders relevant sind:

- `:lines:` nur bestimmte Zeilen einbinden (z. B. 1–40)
- `:start-after:` / `:end-before:` Marker-basiertes Ausschneiden
- `:emphasize-lines:` wichtige Zeilen hervorheben

## Codeblock Layout anpassen

Standardmäßig übernimmt Sphinx das Layout der Codeblöcke weitgehend vom verwendeten Theme. Wie die oben als Bild eingefügten Codeblöcke zeigen, zeigt das Design von Read the Docs nicht die verwendete Sprache an. Dies stellt besonders ein Problem dar, wenn mehrere Sprachen gemischt verwendet werden und eine klare visuelle Trennung von Fließtext und unterschiedlichen Sprachen gewünscht ist.

### CSS-Datei im Projekt ablegen

Statische Ressourcen wie CSS-Dateien werden in Sphinx im Ordner `_static` abgelegt. In diesem Projekt wird eine klare Trennung nach Ressourcentyp verwendet:

```{code-block} none
:caption: Ablageort für eigene Stylesheets
:emphasize-lines: 5, 6

Sphinx-Projekt
├ build/
└ source/
  ├ _static/
  │ └ style/
  │   └ codeblock_layout.css
  ├ conf.py
  └ index.md
```

Der Ordner `_static` wird beim HTML-Build automatisch in die Ausgabe kopiert.\
CSS-Dateien darin sind damit zuverlässig lokal verfügbar und CDN-frei.

### CSS-Datei in `conf.py` einbinden

Damit Sphinx das Stylesheet lädt, wird es in der `conf.py` registriert. Voraussetzung ist, dass `_static` als `html_static_path` gesetzt ist.

```{code-block} python
:caption: Codeblock-Stylesheet einbinden
:linenos:

html_css_files.append("style/codeblock_layout.css")
```

Beim nächsten Build wird die CSS-Datei automatisch im `<head>` der HTML-Seiten eingebunden.

### Grundlayout für alle Codeblöcke definieren

Sphinx erzeugt für Codeblöcke (über Pygments) typischerweise einen äußeren Container der Form:

- `div.highlight`
- plus Sprachklasse, z.B. `div.highlight-python`

Wir definieren zunächst ein einheitliches Grundlayout für alle Codeblöcke:

```{code-block} css
:caption: Basis-Layout für alle Codeblöcke
:linenos:

/* -------------------------------------------------------------------------- */
/* Basislayout für alle Codeblöcke */
/* -------------------------------------------------------------------------- */
div.highlight {
  border-radius: 5px;                 /* Rundungen für alle Ecken */
  overflow: hidden;                   /* Inhalt an Rundungen anpassen */
  border: 1px solid rgba(0,0,0,.08);  /* dezenter Rahmen */
  background: #f5f5f5;                /* neutraler Hintergrund */
}

div.highlight pre,
pre.literal-block {
  background: transparent;            /* Hintergrund übernimmt Container */
  margin: 0;                          /* bündig zum Container */
  padding: 0.75rem 1rem;              /* Lesbarkeit durch Weißraum */
  border-radius: 0;                   /* Rundungen macht der Container */
  overflow: auto;                     /* Scrollbar bei langen Zeilen */
}
```

- `div.highlight` ist die "Karte" um den Code.
- Das `<pre>` enthält den tatsächlichen Code und wird bewusst transparent gehalten.
- `overflow: auto` verhindert Layoutbrüche bei langen Zeilen (z.B. URLs, lange Funktionssignaturen).

### Titelbalken für Sprache und Kontext hinzufügen

Ein Titelbalken ist besonders hilfreich, wenn viele Codeblöcke unterschiedlicher Sprachen im Dokument vorkommen. Er dient als schneller Kontextindikator.

Du erzeugst diesen Balken mit einem Pseudoelement:

```{code-block} css
:caption: Titelbalken für Codeblöcke
:linenos:

/* -------------------------------------------------------------------------- */
/* Titelbalken für alle Codeblöcke */
/* -------------------------------------------------------------------------- */
div.highlight::before {
  content: var(--code-title, "Code");          /* Standardtitel */
  display: block;
  font-weight: 600;

  background: var(--code-title-bg, #3b3b3b);   /* Standardfarbe */
  color: var(--code-title-fg, #fff);

  padding: 6px 10px;
  border-radius: 5px 5px 0 0;                 /* nur oben runden */
  line-height: 1.2;
}
```

Diese beiden CSS Ausschnitte verfolgen den Ansatz, dass die Layout-Logik einmal definiert wird und Sprache bzw. Design über Variablen parametrisiert wird.

### Sprache pro Codeblock automatisch zuordnen

Pygments erzeugt Klassen wie:

- `.highlight-python`
- `.highlight-bash`
- `.highlight-console`
- …

Du setzt dort nur die Variablenwerte:

```{code-block} css
:caption: Sprachabhängige Titel und Farben
:linenos:

/* -------------------------------------------------------------------------- */
/* Titelbalken pro Sprache befüllen */
/* -------------------------------------------------------------------------- */
div.highlight-bash    { --code-title: "Bash";    --code-title-bg: #000;    --code-title-fg: #fff; }
div.highlight-console { --code-title: "Konsole"; --code-title-bg: #000;    --code-title-fg: #fff; }

div.highlight-python  { --code-title: "Python";  --code-title-bg: #3771a1; --code-title-fg: #fff; }
div.highlight-json    { --code-title: "JSON";    --code-title-bg: #434343; --code-title-fg: #fff; }
div.highlight-xml     { --code-title: "XML";     --code-title-bg: #439eff; --code-title-fg: #fff; }
```

```{note}
Diese Lösung ist skalierbar: Neue Sprachen benötigen nur eine zusätzliche Zeile mit Variablenwerten.
```

## Kopier-Button einfügen

Der Kopier-Button ist ein klarer Usability-Gewinn für die Verwendung der Dokumentation in Browsern. Er erlaubt es, dass User den gesamten Quellcode aus einem Codeblock mit einem Mausklick kopieren können.\
Um den Kopier-Button in Code-Blöcken einzufügen muss zunächst eine Erweiterung Installiert werden. Dies kann wie gewohnt über die Paketverwaltung `pip` realisiert werden.

```{code-block} console
:caption: Installation von sphinx-copybutton

python -m pip install sphinx-copybutton
```

Im Anschluss muss die Erweiterung lediglich nur noch in der `conf.py` in die Extension-Liste eingepflegt werden.

```{code-block} python
:caption: Kopier-Button in der conf.py aktivieren
:linenos:

extensions.append("sphinx_copybutton")
```

- Ein "Copy"-Icon erscheint oben rechts am Codeblock.
- Leser können Code ohne Markieren kopieren.
- Besonders relevant in Tutorials, Installationsanleitungen und CLI-Kommandos.

### Anpassen der Position des Kopier-Buttons

Wenn Anpassungen an dem Design der Code-Blöcke vorgenommen wurde, kann es unter Umständen dazu kommen, dass der Kopier-Button an ungünstigen stellen durch Sphinx platziert wird.

Für die oben gezeigten Designänderungen hat sich folgende Konfiguration als sinnvoll herausgestellt;

```{code-block} css
:caption: Anpassungen Kopier-Button
:linenos:

/* -------------------------------------------------------------------------- */
/* Kopier-Button-Konfiguration */
/* -------------------------------------------------------------------------- */
div.highlight .copybtn {
  position: absolute;    /* entkoppeln der Position vom Fließlayout */
  top: 35px;             /* Abstand vom oberen Rand */
  right: 8px;            /* Abstand vom rechten Rand */
  z-index: 2;            /* verhindern von Überlagerung durch andere Layer */
}
```

Dieser CSS-Code kann ebenfalls in die CSS-Datei mit den Anpassungen für die Codeblöcke eingefügt werden.

## API-Dokumentation mit `autodoc`

Inhalt folgt...