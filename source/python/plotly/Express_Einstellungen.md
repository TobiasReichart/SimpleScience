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
- Farben und
- Schriftarten.

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
    line=dict(color="#1F77B4") # setzen einer Linienfarbe
    marker=dict(color="rgba(255, 127, 14, 0.7)", size=10) # setzen eines Markerfarbe
)
```

### Schriftart

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

## Titel

## Legende

## Achsen

