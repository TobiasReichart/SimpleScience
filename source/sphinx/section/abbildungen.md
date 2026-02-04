(Abbildungen)=
# Abbildungen

Abbildungen sind kein "Dekorationselement", sondern ein **präzises Kommunikationsmittel**, die Informationen verdichten, Strukturen sichtbar machen und erlauben es, komplexe Inhalte schneller zu erfassen. Damit Abbildungen in Sphinx zuverlässig funktionieren, müssen sie jedoch als strukturierte, referenzierbare Objekte behandelt werden. Ähnlich wie Gleichungen oder Tabellen.

In diesem Kapitel geht es daher nicht nur um "Bilder einfügen", sondern um ein sauberes Vorgehen für

- konsistente Darstellung in HTML und PDF,
- reproduzierbare Projektstrukturen,
- nummerierte Abbildungen,
- stabile Referenzen im Fließtext.

## Grundbegriffe und Projektstruktur

### Abbildungen in Sphinx

In Sphinx ist eine Abbildung typischerweise ein **Float-Element** (äquivalent zu LaTeX). Das ist ein Objekt, das im Layout verschoben werden darf, um Seitenumbrüche und Textfluss zu **optimieren** (insbesondere im PDF/LaTeX-Export).\
Eine Abbildung besteht konzeptionell aus:

- **Grafik** (z.B. SVG, PNG, JPG, …),
- **Beschriftung** (Caption),
- optionalem **Label** (für Referenzen),
- optionalen **Layout-Optionen** (Größe, Ausrichtung, …).

```{figure} ../../_static/img/sphinx/abbildungen/beispielgrafik.png
:align: center
:width: 80%

Beispielgrafik
```

Das **Label** und die **Beschriftung** der Beispielgrafik sind farblich markiert.

```{note}
Abbildungen werden in dieser Dokumentation automatisch nummeriert.\
Die zugrunde liegende Konfiguration ist im Abschnitt\
{ref}`Globale Nummerierung von Objekten` beschrieben.
```

### Ablage von Bilddateien

Für Sphinx hat sich eine klare Trennung bewährt:

- Quellen (z.B. Mermaid `.mmd`, Matplotlib-Skripte `.py`) liegen außerhalb von `source/`.
- fertige Artefakte, die Sphinx direkt einbindet (`SVG`/`PNG`), liegen in `source/_static/`.

```{code-block} none
:caption: Empfohlene Ordnerstruktur
:emphasize-lines: 6, 7, 8

diagrams/                     ← Quellen (z.B. Mermaid)
plots/                        ← Quellen (z.B. Matplotlib)
source/
└ _static/
  └ img/
    ├ mermaid/
    ├ pictures/
    └ plots/
```

Diese Trennung verhindert, dass `source/` zu einem Mischordner aus Inhalt, Code und Artefakten wird.

### Bildformate: SVG, PNG, JPG

#### SVG (empfohlen für Diagramme und Plots)

SVG ist eine **Vektorgrafik**: Linien, Kurven und Text werden mathematisch beschrieben. Damit gilt:

- beliebig skalierbar ohne Qualitätsverlust,
- Texte bleiben scharf,
- ideal für Diagramme, technische Skizzen, Plots.

#### PNG/JPG (rasterbasiert)

PNG und JPG speichern Pixelraster. Das ist sinnvoll für:

- Screenshots,
- Fotos,
- sehr komplexe Bilddaten.

Für Diagramme sind Rasterformate dagegen oft ein Nachteil, da beim Skalieren schnell Unschärfe entsteht.

```{note}

**SVG** eignet sich für technische Visualisierungen (Linien, Pfeile, Text), weil es skalierbar und scharf bleibt.\
**PNG/JPG** eignen sich für Pixelbilder (Fotos, UI-Screenshots), sind aber auf eine feste Auflösung festgelegt.

$\Rightarrow$ Für eine wissenschaftlich saubere Dokumentation ist SVG für Diagramme und Plots in der Regel die beste Wahl.
```

## Die `figure`-Direktive

Die `figure`-Direktive ist der Standard in Dokumentationen mit Sphinx, da sie **Bildunterschriften**, **Numererierungen** und **Referenzen** sauber unterstützt.

````{code-block} markdown

```{figure} ../../_static/img/sphinx/abbildungen/beispielgrafik.png
:align: center
:width: 80%

Beispielgrafik
```
````

- Die erste Zeile enthält den **Pfad** zur Bilddatei.
- Die Optionen steuern Layout und Verhalten.
- Der Text unterhalb ist die **Bildunterschrift** (Caption).

```{admonition} Warum nicht einfach Markdown-Bilder?
:class: tip

Markdown-Bildsyntax: `![...](...)`

Markdown-Bilder sind schnell, aber funktional eingeschränkt.\ 
Mit `figure` bekommen wir:

- Captions (wissenschaftlich üblich),
- Nummerierung,
- Referenzen im Text (z.B. "siehe Abb. 3"),
- saubere Ausgabe in HTML und PDF.
```

### Optionen von `figure`

Die Verwendung von Optionen in Direktiven wird im Abschnitt {ref}`Optionen von Direktiven` genauer beschrieben.

#### Größe: `:width:`

Mit `:width:` legen wir die Breite der Abbildung fest.\
Hierbei gibt es zwei Grundlegende Möglichkeiten, die Größe der Grafik anzugeben:

- Prozentangaben (z.B. 90%): flexibel, gut für responsive HTML-Ausgabe
- Pixelangaben (z.B. 600px): eher für Screenshots

**Empfehlung:** Für SVGs meist `70–95%`, je nach Detailgrad.

#### Ausrichtung: `:align:`

Typische Werte:

- `center`: Standard für wissenschaftliche Abbildungen
- `left` / `right`: sinnvoll bei kleineren Abbildungen

#### Verlinkungen `:name:`

Damit wir Abbildungen im Text sauber referenzieren können, bekommen sie ein **Label** (eine eindeutige ID). Das Referenzieren ist genauer im Abschnitt {ref}`Inhalte Verlinken` beschrieben.

## Mehrere Abbildungen nebeneinander darstellen

Für die gleichzeitige Darstellung von **zwei oder mehr Abbildungen** nebeneinander bietet Sphinx mit der Erweiterung `sphinx-design` ein flexibles, semantisch sauberes Layoutsystem.\
Damit lassen sich beliebig viele Grafiken in einem **Grid-Layout** anordnen, ohne auf Tabellen oder HTML-Tricks zurückzugreifen.

Das zugrundeliegende Prinzip ist dabei stets gleich:\
Jede Abbildung bleibt eine eigenständige `figure` und wird lediglich über ein übergeordnetes Layout-Element positioniert.

````{dropdown} Installation der Erweiterung (falls noch nicht vorhanden)

Die Erweiterung wird einmalig über den Python-Paketmanager `pip` installiert:

```{code-block} console
:caption: Installation von sphinx-design

python -m pip install sphinx-design
```

Anschließend muss sie in der Datei `conf.py` aktiviert werden:

```{code-block} python
:caption: sphinx-design in conf.py aktivieren
:linenos:

extensions.append("sphinx_design")
```

Nach einem erneuten Build steht die Grid-Funktionalität projektweit zur Verfügung.
````

``````{code-block} markdown
:caption: Mehrere Abbildungen nebeneinander
:linenos:

`````{grid} 2
:gutter: 2

````{grid-item}
```{figure} ../../_static/img/Logo/Logo-black.png
:align: center
:width: 100%
:name: fig-links

Linke Abbildung
```
````
````{grid-item}
```{figure} ../../_static/img/Logo/Logo-black.png
:align: center
:width: 100%
:name: fig-rechts

Rechte Abbildung
```
````
`````
``````

Dabei gilt:

- die Zahl hinter `{grid}` gibt die **Spaltenanzahl** an
- `:gutter:` definiert den Space zwischen den Abbildungen
- jede Grafik ist eine **vollwertige `figure`**
- Referenzen über `{numref}` funktionieren weiterhin
- die Darstellung ist **responsiv** (bei schmalen Bildschirmen umbrechend)

``````{admonition} Gerendertes Ausgabe
:class: note

`````{grid} 2
:gutter: 2

````{grid-item}
```{figure} ../../_static/img/Logo/Logo-black.png
:align: center
:width: 100%
:name: fig-links

Linke Abbildung
```
````
````{grid-item}
```{figure} ../../_static/img/Logo/Logo-black.png
:align: center
:width: 100%
:name: fig-rechts

Rechte Abbildung
```
````
`````
``````