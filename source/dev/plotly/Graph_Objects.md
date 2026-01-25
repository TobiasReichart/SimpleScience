# Plotly Graph Objects

Während Plotly Express eine komfortable, datenzentrierte High-Level-Schicht bietet, erlauben Graph Objects eine **präzise Kontrolle auf niedrigster Ebene**. Damit bietet **Plotly Graph Objects** ebenfalls eine Möglichkeit das Design ganz nach den eigenen Ansprüchen anzupassen und auch Interaktivität und Animationen hinzuzufügen.

```{code-block} python
:caption: Import von Plotly Graph Objects
:linenos:

import plotly.graph_objects as go 
```

## Das Objektmodell

Plotly basiert auf einem hierarchischen Datenmodell, das aus drei Ebenen besteht:
- Figure $\rightarrow$ Container für alles
- Traces $\rightarrow$ Darstellungsobjekte (Linien, Marker, Balken, etc.)
- Layout $\rightarrow$ Achsen, Titel, Legende, Styles, Interaktionen

<div class="mermaid">
flowchart TD
  F["go.Figure<br/><small>(Obercontainer)</small>"] --> D["data<br/><small>Liste von Traces</small>"]
  F --> L["layout<br/><small>Achsen, Schrift, Farben, Buttons</small>"]
  D --> S["Scatter<br/><small>Linien, Punkte, Linien+Marker</small>"]
  D --> B["Bar<br/><small>Balkendiagramme</small>"]
  D --> C["Contour / Heatmap<br/><small>2D Felder</small>"]
  D --> M["Mesh3D / Surface<br/><small>3D-Objekte</small>"]
  L --> A["xaxis / yaxis<br/><small>Skalen, Tickformat, Labels</small>"]
  L --> T["title<br/><small>Titel, Schrift, Position</small>"]
  L --> G["legend<br/><small>Position, Rahmen, Formatierung</small>"]
  L --> U["updatemenus<br/><small>Dropdowns & Buttons</small>"]
</div>

## Erste Schritte

Der praktische Einstieg in Plotly Graph Objects beginnt mit einer sauberen Trennung zwischen Daten, Darstellung und Layout.  
Im Gegensatz zu Plotly Express erzeugen wir hier die gesamte Figur explizit.

Wir legen eine leere `Figure` an, füllen sie mit einzelnen Spuren (Traces) und konfigurieren das Layout anschließend vollständig selbst.  
Dieser Ansatz wirkt anfangs etwas ausführlicher, eröffnet jedoch die volle gestalterische Kontrolle über jede Komponente des Plots.

Das folgende Minimalbeispiel zeigt den typischen Arbeitsablauf:  
Wir erzeugen einen eindimensionalen Datensatz, definieren einen `Scatter`-Trace und binden diesen in eine `Figure` ein.

```{code-block} python
:caption: Graph Objects - Minimalbeispiel
:linenos:

import numpy as np                # NumPy für numerische Berechnungen (Arrays, linspace, sin)
import plotly.graph_objects as go # Plotly low-level API für interaktive Plots

x = np.linspace(0, 2*np.pi, 100) # 100 Punkte gleichmäßig im Intervall [0, 2π]
y_sin = np.sin(x)                # Sinuswerte zu den x-Punkten

fig = go.Figure() # Leere Plotly-Figur anlegen

fig.add_trace(    # Eine Spur (Trace) zur Figur hinzufügen
    go.Scatter(
        x=x,                                    # x-Daten: Array von 0 bis 2π
        y=y_sin,                                # y-Daten: sin(x)
        mode="lines",                           # Darstellung: nur Linie, keine Marker
        name=r"$f(x) = \sin \left( x \right)$", # Name der Spur, erscheint in der Legende
        marker={"color": "#1F77B4"}           # Linien-/Markerfarbe (Plotly-Standardblau)
    )
)

fig.show() # Figur rendern und interaktiv anzeigen
```

```{raw} html
<iframe
    src="../../_static/plots/python/plotly/example_objects.html"
    width="100%"
    height="400"
    frameborder="0">
</iframe>
```

Alle Einstellungen, die unter {ref}`Grundlegende Einstellungen eines Plots Plotly` erläutert wurden können auch für Objekts-Plots verwendet werden. **Graph Objects** bietet uns jedoch weitere Möglichkeiten, die unter **Plotly Express** nicht möglich waren:

```{list-table} Unterschied Plotly Express vs. Graph Objects
:align: center
:header-rows: 1

* - Feature
  - Plotly Express
  - Graph Objects
* - alles Layout-Einstellungen (`update_layout`)
  - Ja
  - Ja
* - Achsen, Fonts, Farben, Templates
  - Ja
  - Ja
* - mehrere Subplots
  - eingeschränkt
  - Ja
* - Buttons, Dropdowns, Menüs (`updatemenus`)
  - Nein
  - Ja
* - Slider (z.B. Zeit, Animation)
  - Nein
  - Ja
* - Animationen
  - wenig Kontrolle
  - Ja
* - Komplese Traces (Surface, Mesh3D)
  - Nein
  - Ja
* - Zustandsabhängige Layoutänderungen
  - Nein
  - Ja
```