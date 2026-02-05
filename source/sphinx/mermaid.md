# Diagramme mit Mermaid

Diagramme sind ein zentrales Element technischer Dokumentationen. Sie ermöglichen es, **Strukturen**, **Abläufe und Abhängigkeiten** kompakt und visuell darzustellen, ohne umfangreiche Textbeschreibungen lesen zu müssen. Für textbasierte Dokumentationssysteme wie Sphinx bietet sich hier für einfache Diagramme **Mermaid** an.

Mermaid ist eine **deklarative Diagrammsprache**, mit der Diagramme ausschließlich über Text beschrieben werden.

In diesem Abschnitt werden zwei mögliche Integrationswege vorgestellt und eingeordnet. Anschließend wird der für veröffentlichte Sphinx-Dokumentationen empfohlene Workflow detailliert beschrieben.

## Verwendung von Mermaid mit Sphinx

### Mermaid direkt verwenden (als Direktive)

Sphinx bietet mit der Erweiterung `sphinxcontrib-mermaid` die Möglichkeit, Mermaid-Code **direkt innerhalb** der Dokumentation zu schreiben und beim Build rendern zu lassen. Dabei wird der Diagrammcode direkt in einer Markdown-Datei eingebettet.

Konzeptionell wirkt dieser Ansatz zunächst attraktiv, da:

- Diagramm und erklärender Text unmittelbar nebeneinander stehen,
- keine externen Dateien notwendig sind,
- Änderungen sofort sichtbar werden.

```{admonition} Einschränkungen dieses Ansatzes
:class: warning

Für öffentliche, langfristig gepflegte Dokumentationen ist diese Methode jedoch problematisch:

- Die Diagramme werden **clientseitig per JavaScript** gerendert.
- Es bestehen **Abhängigkeiten von externen Bibliotheken** (z.B. Mermaid, d3, ELK).
- Unterschiede zwischen lokalem Build, GitHub Pages und PDF-Export sind möglich.
- Debugging bei Fehlern ist **aufwendig** und browserabhängig.
- Offline-Builds sind nur eingeschränkt oder gar nicht möglich.
```

>Einordnung:\
>Die direkte Mermaid-Integration eignet sich für **lokale Experimente** oder **Entwurfsphasen**, wird jedoch für veröffentlichte Sphinx-Dokumentationen ausdrücklich **nicht** empfohlen.

````{code-block} markdown
:caption: Beispielhafter Mermaid-Code in Markdown-Datei
:linenos:

```{mermaid}
:center:

flowchart LR
    A[while True] --> B[Code im Schleifenrumpf]
    B --> C{Abbruchbedingung erfüllt?}
    C -- Ja --> D([break / Ende])
    C -- Nein --> A
```
````

```{figure} ../_static/img/sphinx/mermaid/while_true.svg
:width: 100%
:align: center

Output: beispielhafter Mermaid-Code
```

### Mermaid als .svg Export (Empfohlener Ansatz)

Für produktive Dokumentationen wird ein zweistufiger Workflow empfohlen:

1. Mermaid wird ausschließlich zur Erstellung der Diagramme verwendet.
2. Die Diagramme werden vorab als `svg` (`png` ist auch möglich) gerendert.

$\Rightarrow$ Sphinx bindet die SVGs oder PNGs statisch als Abbildungen ein (siehe {ref}`Abbildungen`).

Dadurch wird die Diagrammquelle vollständig von der Darstellung und der schlussendlichen Dokumentation entkoppelt. Dieser Workflow bietet zusätzlich einige nicht unerhebliche Vorteile:

- vollständig offlinefähig
- livevorschau direkt in VS Code
- keine JavaScript-Abhängigkeiten im Sphinx-Build
- identisches Verhalten in HTML und PDF
- reproduzierbar und versionsstabil
- didaktisch sauber (Quelle $\neq$ Darstellung)

```{admonition} Vektor- statt Rastergrafik
:class: tipp

SVG beschreibt Grafiken mathematisch (Linien, Kurven, Texte), während PNG aus festen Pixelrastern besteht.\
Dadurch ergeben sich folgende Unterschiede:

- Beliebige Skalierbarkeit\
    SVG-Grafiken bleiben bei jeder Vergrößerung gestochen scharf.\
    PNG-Grafiken verlieren bei Skalierung sichtbar an Qualität.
-   Optimale Lesbarkeit\
    Texte in SVGs bleiben klar und scharf, unabhängig von Bildschirmauflösung oder Zoomstufe.
```

## Mermaid-Diagramme mit Visual Studio Code erstellen

Für die Erstellung und Vorschau von Mermaid-Diagrammen empfiehlt sich Visual Studio Code in Kombination mit einer spezialisierten Erweiterung.

**Voraussetzungen:**

- [Visual Studio Code](https://code.visualstudio.com/download)
- VS-Code-Erweiterung [Mermaid Preview](https://marketplace.visualstudio.com/items?itemName=vstirbu.vscode-mermaid-preview)

```{figure} ../_static/img/sphinx/mermaid/mermaid_preview.png
:width: 80%
:align: center

Mermaid Preview Erweiterung in VS Code
```

### Anlegen einer Mermaid-Datei

Für größere Projekte ist eine klare Ordnerstruktur essenziell.

```{code-block} none
:caption: Empfohlene Ordnerstruktur
:emphasize-lines: 4, 9

Sphinx-Projekt
├ build/
├ diagrams/
│ └ while_true.mmd
├ source/
│ ├ _static/
│ │ └ img/
│ │   └ mermaid/
│ │     └ while_true.svg
│ ├ _templates/
│ ├ conf.py
│ └ index.rst
├ ...
```

- `diagrams/` enthält nur Mermaid-Quellen
- `_static/img/mermaid/` enthält nur gerenderte SVGs

Diese Trennung verhindert eine Vermischung von Quelle, Darstellung und Dokumentation.

Diagramme werden in separaten Dateien mit der Endung `.mmd` abgelegt. Diese Dateien enthalten ausschließlich den Mermaid-Code und **keinen** Dokumentationstext.

```{code-block} text
:caption: Beispieldatei: while_true.mmd
:linenos:

flowchart LR
    A[while True] --> B[Code im Schleifenrumpf]
    B --> C{Abbruchbedingung erfüllt?}
    C -- Ja --> D([break / Ende])
    C -- Nein --> A
```

```{hint}

Die Dateiendung `.mmd` signalisiert klar, dass es sich um eine Diagrammquelle handelt.
```

### Vorschau eines Diagramms öffnen

Die Erweiterung *Mermaid Preview* ermöglicht eine grafische Vorschau des Diagramms über die **Command Palette** (`Mermaid Preview: Preview Diagram`). Die Command Palette ist über die Tastenkombination {kbd}`Strg` + {kbd}`Shift` + {kbd}`P` erreichbar,

Die Vorschau erfolgt in einem **separaten Fenster**, unabhängig von Markdown- oder Sphinx-Vorschauen.


```{figure} ../_static/img/sphinx/mermaid/mermaid_preview_vscode.png
:width: 100%
:align: center

Mermaid Preview mit Vorschau in VS Code
```

### Export des Diagramms als SVG

Aus der Vorschau heraus kann das Diagramm direkt als SVG oder PNG exportiert werden:

1. Links oben in der Ecke der Vorschau auf den Download-Pfeil
2. Image as SVG

```{figure} ../_static/img/sphinx/mermaid/save_as.png
:width: 80%
:align: center

Mermaid Preview mit Vorschau in VS Code
```

$\Rightarrow$ Dieser Export kann nun wie jede andere {ref}`Abbildung <Abbildungen>` in die Sphinx-Dokumentation eingebunden werden.

## Styling von Mermaid-Diagrammen

Der Stil eines Diagramms wird direkt im Mermaid-Code festgelegt und beim Export dauerhaft ins SVG eingebettet.\
Mermaid stellt hierfür mehrere vordefinierte Themes zur Verfügung, die das grundlegende Erscheinungsbild eines Diagramms beeinflussen (Farben, Kontraste, Schriftgewicht). Das gewünschte Theme wird über den `init`-Block am Anfang des Diagramms gesetzt.

```{code-block} text
:caption: Styling von Mermaid-Diagrammen
:linenos:

%%{init: {"theme": "<theme-name>"}}%%
```

Aktuell stehen folgende Themes zur Verfügung:

- `default`\
    **Das Standard-Theme von Mermaid.**\
    Farblich ausgewogen, jedoch eher generisch und weniger für wissenschaftliche Dokumentation optimiert.
- `neutral`\
    **Reduziertes, kontrastarmes Design mit klaren Linien.**\
    Empfohlen für technische und wissenschaftliche Dokumentationen, da es ruhig wirkt und gut mit Fließtext harmoniert.
- `dark`\
    **Dunkles Farbschema mit hohem Kontrast.**\
    Geeignet für Präsentationen oder dunkle Benutzeroberflächen, jedoch weniger geeignet für PDF-Ausgaben.
- `forest`\
    **Grünton-basiertes Theme mit dekorativem Charakter.**\
    Für erklärende Visualisierungen geeignet, jedoch stilistisch weniger neutral.
- `base`\
    **Minimalistisches Ausgangstheme ohne starke Voreinstellungen.**\
    Gedacht für vollständig benutzerdefinierte Designs über `themeVariables`.

## Weiterführende Dokumentation zu Mermaid

In diesem Abschnitt wurde Mermaid gezielt im Kontext einer **stabilen**, **veröffentlichungsfähigen Sphinx-Dokumentation** eingeordnet und auf die für diesen Anwendungsfall relevanten Aspekte fokussiert. Mermaid selbst unterstützt jedoch eine Vielzahl weiterer Diagrammtypen, Syntaxelemente und Konfigurationsmöglichkeiten.

Eine vollständige und stets aktuelle Übersicht der verfügbaren Diagrammtypen sowie deren Syntax findet sich in der offiziellen Mermaid-Dokumentation:

**Offizielle Mermaid-Dokumentation**\
[https://mermaid.ai/open-source/intro/index.html](https://mermaid.ai/open-source/intro/index.html)