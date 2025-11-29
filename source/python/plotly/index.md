# Plotly

Plotly ist ein leistungsfähiges Python-Framework für wissenschaftliche Visualisierungen, das sich ideal für technische Anwendungen, Physik, Datenanalyse und moderne Lehrmaterialien eignet.\
Im Unterschied zu klassischen Bibliotheken wie Matplotlib erzeugt Plotly vollständig interaktive **HTML-Grafiken**, die sich direkt in Webseiten, Jupyter-Notebooks oder Sphinx-Dokumentationen einbetten lassen.

Ich verwende Plotly (stand jetzt) ausschließlich für interaktive oder animierte Inhalte dieser Website. Hierfür bringt Plotly einige Vorteile, wie die

1. **Interaktivität**,\
    Jeder Plot ist automatisch interaktive, ohne das zusätzlicher Code geschrieben werden muss. Jede Grafik kann gezoomt oder gefiltert werden und verfügt über Hover-Informationen.
2. die **Präzise Kontrolle** und\
    Mit den `graph_objects` lassen sich Achsen, Layouts, Ticks, Farben und Interaktionen detailliert steuern. Damit können umfangreiche interaktive Lehr- oder Publikationsgrafiken erstellt werden.
3. die **Web-Ready Schnittstelle**.\
    Jede Grafik kann als HTML exportiert werden und so ohne Probleme in Webseiten, wie Sphinx-Dokumentationen eingebettet werden. Die Interaktivität bleibt dabei vollständig erhalten und das auch ohne Python-Backend.

**Installation**

Die Installation von Plotly erfolgt wie bei allen anderen Python-Pakten über den Python-Paketmanager `pip`.

```{code-block} console
:caption: Installation von Plotly
:linenos:

python -m pip install plotly

```
Sobald Plotly installiert ist, kann es unmittelbar sowohl in einem Jupyter Notebook als auch in VSCode verwendet werden.

Ich empfehle `Numpy` und `Pandas` direkt mitzuinstallieren, da diese Module für diese Dokumentation vorausgesetzt werden.

```{code-block} console
:caption: Installation von Numpy und Pandas
:linenos:

python -m pip install numpy pandas

```

**Erste Schritt**

Als schnellste Möglichkeit, Plotly zu testen, genügt bereits:

```{code-block} python
:caption: Plotly Beispiel für den Schnelleinstig
:linenos:

import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="petal_length", color="species")
fig.show()
```
*Codebeispiel aus der offiziellen Dokumentation*: [https://plotly.com/python/plotly-express/](https://plotly.com/python/plotly-express/)

Dieser einfache Scatterplot ist vollständig interaktiv.\
Wir können hineinzoomen, Punkte auswählen, Achsen untersuchen und Werte direkt im Browser erkunden.

```{raw} html
<iframe
    src="../../_static/plots/python/plotly/example.html"
    width="100%"
    height="400"
    frameborder="0">
</iframe>
```

>*Die Grafik zeigt die Beziehung zwischen Kelchblattbreite und Kronblattlänge dreier Iris-Arten. Die farbliche Trennung macht sichtbar, wie stark sich die Arten in ihren morphologischen Merkmalen unterscheiden und welche Clusterstrukturen sich in den Messdaten ausbilden.*

**Dokumentation und weiterführende Ressourcen**

Für vertiefende Informationen lohnt sich ein Blick in die offiziellen Quellen:
- **Plotly Python**\
    [https://plotly.com/python/](https://plotly.com/python/)
- **Plotly Express**\
    [https://plotly.com/python/plotly-express/](https://plotly.com/python/plotly-express/)
- **Plotly Graph Objects**\
    [https://plotly.com/python/graph-objects/](https://plotly.com/python/graph-objects/)
- **Plotly auf PyPI**\
    [https://pypi.org/project/plotly/](https://pypi.org/project/plotly/)