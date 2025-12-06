(Grundlegende Einstellungen eines Plots Plotly)=
# Grundlegende Einstellungen eines Plots

In diesem Abschnitt wollen wir uns grundlegende Einstellungen anschauen, die die Plotly-Ausgabe beeinflussen und die Grafiken grob an unsere Anforderungen anpassen.

In dieser Beschreibung orientieren wir uns an diesem Minimalbeispiel:

```{code-block} python
:caption: Codebeispiel für die gezeigten Einstellungen
:linenos:

import numpy as np          # NumPy für numerische Berechnungen (Arrays, linspace, sin)
import plotly.express as px # Plotly Express High-Level-API

x = np.linspace(0, 2*np.pi, 200) # 200 Punkte gleichmäßig im Intervall [0, 2π]
y_sin = np.sin(x)                # Sinuswerte zu den x-Punkten

fig = px.line(x=x, y=y_sin) # Ploten der Funktion
fig.show()                  # Figur rendern und interaktiv anzeigen
```

## Layout

Das Layout umfasst alle globalen Eigenschaften einer Figure:

- Templates,
- Farben,
- Schriftarten,
- Gitterlinien und
- Dezimaltrennzeichen

Plotly Express setzt hier sinnvolle Standardwerte, aber für saubere wissenschaftliche Plots lohnt sich eine explizite Konfiguration.

### Templates

Plotly bietet einige bereits vorkonfigurierte Templates, die in der offiziellen Dokumentation zu finden sind: [https://plotly.com/python/templates/](https://plotly.com/python/templates/)

Zur Auswahl für 2D-Plots stehen:

- `"plotly"`
- `"plotly_white"`
- `"plotly_dark"`
- `"ggplot2"`
- `"seaborn"`
- `"simple_white"`
- `"none"`

Ein Template legt unter anderem fest:

- Hintergrundfarben von Plot und Seite,
- Standard-Schriftart und -größe,
- Gitterlinien und Achsenstil,
- Standard-Farbsequenzen für Traces.

Diese können über den `fig.update_layout()`-Aufruf gesetzt werden:

```{code-block} python
:caption: Verwendung eines Plotly-Templates
:linenos:

fig.update_layout(
    template="plotly_white",
)
```

Das Template wirkt dabei nur als **Voreinstellung**:  
Alle Layout-Parameter, die wir später explizit setzen (z. B. `font`, `xaxis`, `yaxis`, `legend`), überschreiben die Werte des Templates.\
Für wissenschaftliche Plots bietet sich häufig `"plotly_white"` oder `"simple_white"` als neutrale Basis an, auf der anschließend gezielt Achsen, Schrift und Farben angepasst werden.

```{hint}
Auch Plotly Express akzeptiert ein `template=`-Argument direkt im Funktionsaufruf. Intern wird dabei derselbe Mechanismus verwendet.
```

### Farben

Plotly unterstützt eine Vielzahl an Farbdefinitionen, die flexibel sowohl für Linien, Marker, Hintergründe als auch für komplette Farbsequenzen eingesetzt werden können.

- CSS-Farben\
    siehe in der offiziellen Dokumentation: [https://plotly.com/python/css-colors/](https://plotly.com/python/css-colors/)
- Hex-Codes
- RGB- und RGBA-Farben

```{code-block} python
:caption: Setzen von Farben
:linenos:

fig.update_traces(
    line=dict(color="#1F77B4"), # setzen einer Linienfarbe
    marker=dict(color="rgba(255, 127, 14, 0.7)", size=10), # setzen eines Markerfarbe
)
```

(Plotly Schriftart)=
### Schriftart

Plotly ermöglicht eine detaillierte Kontrolle über die Typografie eines Plots. Alle globalen Schriftparameter werden über den Eintrag `font` im Layout gesetzt und gelten automatisch für Titel, Achsenbeschriftungen, Ticklabels und Legendentexte, sofern diese nicht separat überschrieben werden.

```{code-block} python
:caption: Default Einstellungen der Schriftart
:linenos:

fig.update_layout(
    font=dict(
        color="#444",
        family="Open Sans, verdana, arial, sans-serif",
        size=12,
        style="normal",
        weight="normal",
    ),
)
```

- `color`\
    Farbe der Schrift: Unterstütz **CSS, Hex, RGB** und **RGBA**
- `family`\
    Hier kann die gewünschte Schriftart mit einer Fallbackkette hinterlegt werden\
    Durch die Fallback-Schriftarten kann eine konsistente Darstellung auf vielen Geräten gewährleistet werden.
- `size`\
    Schriftgröße als `int`
- `style`\
    Schriftschnitt / Kursivformatierung
    - `"normal"`
    - `"italic"` (echte Kursivschrift)
    - `"oblique"` (künstlich geneigte Schrift)
- `weight`\
    Werte zwischen `1` und `1000` oder Kategorie über `string`
    - `"normal"`
    - `"bold"`
    - `"lighter"`
    - `"bolder"`

### Dezimaltrennzeichen

In deutschsprachigen wissenschaftlichen Texten sind Dezimaltrennzeichen mit Komma und Tausendertrennzeichen mit Punkt üblich.
Plotly verwendet standardmäßig den amerikanischen Stil:

- 1234.56 $\rightarrow$ Punkt als Dezimaltrennzeichen
- 1,234.56 $\rightarrow$ Komma als Tausendertrennzeichen

Plotly kann jedoch über `separators` auf das deutsche Format umgestellt werden.

```{code-block} python
:caption: Deutsches Dezimalformat setzen
:linenos:

fig.update_layout(
    separators=",.",
)
```

Wenn kein Tausendertrennzeichen dargestellt werden soll, kann statt dem `.` auch schlicht ein Leerzeichen verwendet werden.

(Titel Plotly)=
## Titel

Wie alles ist auch der **Titel** ein kleines Objekt innerhalb des Layouts. Unter Zuhilfenahme eines Dictionarys `title=dict(...)` können wir dieses Objekt vollständig beschreiben und editieren.

```{code-block} python
:caption: Wichtige Einstellungen für den Plot-Titel
:linenos:

fig.update_layout(
    title=dict(
        text="Amplitudenverlauf<br>gedämpfter Schwingungen",  # Titeltext
        x=0.5,              # horizontale Position (0 = links, 0.5 = Mitte, 1 = rechts)
        y=0.95,             # vertikale Position (0 = unten, 1 = ganz oben)
        xanchor="center",   # Bezugspunkt für x: "left", "center", "right"
        yanchor="top",      # Bezugspunkt für y: "top", "middle", "bottom"
        font=dict(          # Schrift des Titels
            family="Arial, sans-serif",
            size=20,
            color="black"
        ),
        pad=dict(           # Innenabstände rund um den Titel (Padding)
            t=10,           # Abstand nach oben (top)
            b=10,           # Abstand nach unten (bottom)
            l=0,            # optional: links
            r=0,            # optional: rechts
        ),
    ),
)
```
- `text=`\
    Der eigentliche Titeltext.\
    Um Zeilenumbrüche in einem String einzufügen, kann der HTML-Tag `<br>` verwendet werden.
- `x=`, `y=`\
    Koordinaten des Ankerpunktes der Textbox:
- `xanchor=`, `yanchor=`\
    Position des Ankerpunktes im betreffenden Textfeld

(Ausrichtungen in Plotly)=
````{list-table} Ausrichtung in Plotly
:widths: 50 50
:header-rows: 0

* - ```{figure} ../../../../_static/plots/python/plotly/anchorpoints.png
      :align: center
      :width: 90%
    ```
  - ```{figure} ../../../../_static/plots/python/plotly/coordinates_plotly.png
      :align: center
      :width: 90%
    ```
````
- `font=`\
    siehe {ref}`Plotly Schriftart`
- `pad=`\
    Abstände des Titels zu umgebenden Objekten

Das Schöne an Plotly ist, dass das **Gestaltungsprinzip überall dasselbe** ist. Viele der Titel-Optionen tauchen in sehr ähnlicher Form auch bei {ref}`Plotly Legende` und {ref}`Plotly Achsen` wieder auf.\
Insbesondere `text`, `font` und Abstände (`pad` bzw. `standoff` bei Achsentiteln) können so gleichwertig verwendet werden.\
Wer den Titel verstanden hat, versteht damit gleichzeitig die grundlegende Logik der restlichen Layoutobjekte.

(Plotly Legende)=
## Legende

Die **Legende** ist, wie der Titel, ein eigenes Objekt innerhalb des Layouts.\
Mit `legend=dict(...)` lässt sich ihre Darstellung vollständig konfigurieren. Dazu gehören Positionierung, Schrift, Hintergrund, Rahmen und sogar die Ausrichtung der Einträge.

```{code-block} python
:caption: Wichtige Einstellungen für die Plot-Legende
:linenos:

fig.update_layout(
    showlegend=True,       # Legende ein- oder ausblenden

    legend=dict(
        title=dict(        # Titel der Legende (optional)
            text="Messreihe",
            font=dict(
                family="Arial, sans-serif",
                size=14,
                color="black",
            ),
        ),

        x=0.01,            # horizontale Position (0 = links, 1 = rechts)
        y=0.99,            # vertikale Position (0 = unten, 1 = oben)
        xanchor="left",    # Anker innerhalb der Legende: "left", "center", "right"
        yanchor="top",     # vertikaler Anker: "top", "middle", "bottom"

        bgcolor="rgba(255,255,255,0.8)",   # Hintergrundfarbe
        bordercolor="black",               # Rahmenfarbe
        borderwidth=1,                     # Rahmenbreite

        orientation="v",  # Orientierung: "v" (default), vertikal, "h" für horizontal
        traceorder="normal",  # Reihenfolge der Einträge (z. B. "reversed")
    )
)
```

- `showlegend`\
    Aktiviert oder deaktiviert die gesamte Legende.
- `title=`\
    siehe {ref}`Titel Plotly`
- `x=`, `y=`, `xanchor=`, `yanchor`\
    siehe {ref}`Ausrichtungen in Plotly`
- `bgcolor=`\
    Hintergrundfarbe der Legendenbox. Unterstützt CSS-Farbnamen, Hex-Farben und RGBA-Angaben.
- `bordercolor=`\
    Farbe des Rahmens um die Legende.
- `borderwidth=`\
    Breite des Legendenrahmens in Pixeln.
- `orientation=`\
    Legt die Ausrichtung der Einträge fest: `"v"` für vertikal (Standard) oder `"h"` für horizontal. Horizontal eignet sich besonders für breite oder Dashboard-artige Layouts.
- `traceorder=`\
    Bestimmt die Reihenfolge der Legenden-Einträge.  
    Mögliche Werte: `"normal"`, `"reversed"`, `"grouped"`.  
    Damit lässt sich die Legende logisch strukturieren oder an spezifische Darstellungsreihenfolgen anpassen.

(Plotly Achsen)=
## Achsen

Achsen steuern in Plotly unter anderem
- die Beschriftung,
- den dargestellten Wertebereich,
- die Skalierung (linear, logarithmisch, etc.),
- das Zahlenformat der Ticks und
- Zusatzlinien wie Nulllinien oder Grid.

```{code-block} python
:caption: Wichtige Einstellungen für die Achsen
:linenos:

fig.update_layout(
    xaxis=dict(
        title="x",          # Achsentitel
        range=[0, 2*np.pi], # sichtbarer Bereich der x-Achse
        type="linear",      # Skalierung: "linear", "log", "date", "category"
        tickformat=".2f",   # Format der Tick-Beschriftung
        tickmode="auto",    # Tick-Modus: "auto", "linear", "array"
        zeroline=True,      # Nullinie einblenden (z. B. bei t=0)
        zerolinecolor="#444",
    ),
    yaxis=dict(
        title="f(x)",
        range=[-1.2, 1.2],
        type="linear",
        tickformat=".1f",
        tickmode="auto",
        zeroline=True,
        zerolinecolor="#444",
    ),
)
```

- `title=`\
    Beschriftung der Achse.
    Entweder als einfacher String (`"x"`, `"f(x)"`) oder als eigenes Titel-Objekt mit Schriftparametern.\
    Analog zum Plot-Titel, siehe {ref}`Titel Plotly`.
- `range=`\
    Sichtbarer Wertebereich der Achse als [min, max].\
- `type=`\
    Skalierungstyp der Achse:\
    "linear" (Standard), `"log"`, `"date"`, `"category"`.
- `tickformat=`\
    Formatierungsstring für die Tick-Beschriftung (d3-Format).\
    Typische Beispiele:
	- `".2f"` $\rightarrow$ feste Schreibweise mit 2 Nachkommastellen
	- `".1e"` $\rightarrow$ wissenschaftliche Notation
- `tickmode=`\
    Steuerung, wie Ticks gesetzt werden:
	- `"auto"` $\rightarrow$ Plotly wählt sinnvolle Abstände selbst
	- `"linear"` + `dtick` $\rightarrow$ feste Abstände
	- `"array"` + `tickvals` / t`icktext` $\rightarrow$ Ticks explizit vorgeben
- `zeroline=` / zerolinecolor=
    Blendet eine zusätzliche Linie bei 0 ein (z. B. Zeit t=0 oder Nulllinie eines Signals).

Die Achsenobjekte `xaxis` und `yaxis` lassen sich, analog zu Titel und Legende, jederzeit erweitern, z. B. um Mehrfachachsen, spezielle Tickpositionen oder farblich hervorgehobene Bereiche.

### Gitterlinien (Grid)

Gitterlinien helfen dabei, Werte präzise abzulesen und Strukturen im Datensatz zu erkennen. In Plotly gehören die Gittereinstellungen ebenfalls zu den Achsenobjekten.

Ein typisches Muster ist, den gewünschten Grid-Stil einmal in einem Dictionary zu sammeln und dann für beide Achsen zu verwenden:

```{code-block} python
:caption: Gitterlinien für beide Achsen konsistent setzen
:linenos:

axis_grid = dict(
    showgrid=True,        # Gitterlinien einblenden
    gridcolor="#dddddd",  # Farbe der Gitterlinien
    gridwidth=1,          # Linienstärke
    griddash="dot",       # Linienstil: "solid", "dot", "dash", ...
)

fig.update_layout(
    xaxis=dict(
        title="x",
        **axis_grid,      # Grid-Style auf x-Achse anwenden
    ),
    yaxis=dict(
        title="f(x)",
        **axis_grid,      # Grid-Style auf y-Achse anwenden
    ),
)
```

- `showgrid=`\
    Aktiviert oder deaktiviert die Gitterlinien auf der jeweiligen Achse.
- `gridcolor=`\
    Farbe der Gitterlinien.
- `gridwidth=`\
    Linienstärke der Gitterlinien in Pixeln.
- `griddash=`\
    Strichart der Gitterlinien: `"solid"`, `"dot"`, `"dash"`, `"dashdot"`, etc.

Für feinere Raster können zusätzlich Minor-Grids verwendet werden:

```{code-block} python
:caption: Nebengitter (Minor Grid) aktivieren
:linenos:

fig.update_xaxes(
    showgrid=True,
    minor=dict(
        showgrid=True,
        gridcolor="#eeeeee",
    ),
)
```

Minor-Grids werden je nach Plot-Typ unterschiedlich gut unterstützt, eignen sich aber z. B. für dichte Skalen oder logarithmische Achsen.