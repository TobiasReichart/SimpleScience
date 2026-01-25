# Plotly Express

Plotly Express ist die High-Level-Schnittstelle der Plotly-Bibliothek und ermöglicht das schnelle Erstellen interaktiver Visualisierungen mit minimalem Codeaufwand.\
Der Fokus liegt auf einem datenzentrierten Ansatz: Diagramme werden direkt aus Tabellenstrukturen wie **Pandas-DataFrames** erzeugt und automatisch mit passenden Achsentiteln, Farben und Legenden versehen.

```{code-block} python
:caption: Import von Plotly Express
:linenos:

import plotly.express as px
```

Die Express-Funktionen bieten einen idealen Einstieg, um Daten rasch zu explorieren oder Zwischenergebnisse visuell zu prüfen.
Da Plotly Express intern vollständig auf den Plotly Graph Objects aufbaut, lassen sich alle erzeugten Plots jederzeit erweitern und flexibel anpassen.