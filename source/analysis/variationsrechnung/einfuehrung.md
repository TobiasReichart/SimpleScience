(Einführung Variationsrechnung)=
# Einführung - Was ist Variationsrechnung

In der klassischen Analysis suchen wir häufig nach stationären Punkten von Funktionen.

```{admonition} Definition: stationärer Punkt
:class: note

Ein Punkt $x_{0}$ heißt **stationärer Punkt** einer differenzierbaren Funktion $f$, wenn dort die **erste Ableitung verschwindet**.

$$f^{\prime}(x_{0}) = 0$$

oder allgemein für eine Funktion von mehreren Variablen

$$\nabla f(\vec{x}_{0}) = 0.$$

Das bedeutet, dass sich der Funktionswert bei einer kleinen Änderung $\delta \vec{x}$ der Eingabe **in erster Ordnung nicht** ändert.\
Damit ist **noch nicht** gesagt, ob dort ein **Minimum**, ein **Maximum** oder etwas anderes vorliegt, sondern lediglich die notwendige Bedingung erfüllt.
```

Dabei ist eine Funktion nichts anderes als eine Abbildung von einer Menge in eine andere, bei der jedem Input-Objekt ein Output-Wert zugeordnet wird.

Im reellen wäre das zum Beispiel:

$$f: \mathbb{R} \rightarrow \mathbb{R}, \quad x \mapsto f(x)$$

Jede zulässige Eingabe $x$ (Definitionsbereich $\mathbb{D}$) wird auf eine Zahl $f(x) \in \mathbb{R}$ abgebildet.

$$\boxed{f: \mathbb{D} \subseteq \mathbb{R}^{n} \rightarrow \mathbb{R}, \quad \vec{x} \mapsto f(\vec{x})}$$

```{dropdown} Beispiel für eine Funktion
:icon: comment

Ein Beispiel wäre eine Funktion von zwei Variablen, also

$$f: \mathbb{R}^{2} \rightarrow \mathbb{R}, \quad \left( x, y \right) \mapsto x^{2} + y^{2}.$$

oder auch klassisch aufgeschrieben:

$$f(x,y) = x^{2} + y^{2}.$$

Damit ist die Funktion eine Vorschrift, die jedem zulässigen Eingabevektor

$$\begin{pmatrix} x \\ y \end{pmatrix} \in \mathbb{R}^{2}$$

genau eine reelle Zahl zuordnet. Ein konkreter Einsatz wäre:

$$f(1, 2) = 1^{2} + 2^{2} = 5.$$

Das bedeutet, dass der Eingabevektor $(1, 2)$ auf die Zahl $5$ abgebildet wird.
```

Wir suchen also Punkte $\vec{x}_{0}$, an denen die erste Ableitung bzw. der Gradient von $f(\vec{x})$ verschwindet $\left( \nabla f(\vec{x}_{0}) = 0 \right)$. Das bedeutet, dass an dieser Stelle eine horizontale Tangente, horizontale Tangentialebene oder ein höherdimensionales Äquivalent existiert.

```{figure} ../../_static/plots/analysis/variationsrechnung/einfuehrung/extremstellen.png
:align: center
:width: 100%

Stationäre Punkte einer Funktion von einer Variable
```

Der Charakter eines Punktes, also **Maximum** (*Hochpunkt*), **Minimum** (*Tiefpunkt*) oder Sattelpunkt, wird über die hinreichende Bedingung untersucht.

- $f^{\prime \prime}(x=x_{0}) > 0$: lokales Minimum (konvex / nach oben gekrümmt)
- $f^{\prime \prime}(x=x_{0}) = 0$: Der Test ist nicht entscheidend
- $f^{\prime \prime}(x=x_{0}) < 0$: lokales Maximum (konkav / nach unten gekrümmt)

```{admonition} Warum ist die erste Ableitung die wichtige Bedingung?
:class: hint

Betrachten wir eine kleine Änderung $x_{0} \rightarrow x_{0} + \delta x$, dann liefert die Taylorentwicklung um $\delta x \approx 0$:

$$f(x_{0} + \delta x) \approx f(x_{0}) + \delta x f^{\prime}(x_{0}) + \frac{\delta x^{2}}{2} f^{\prime \prime}(x_{0})$$

Also ist die Änderung

$$\Delta f(\delta x) = f(x_{0} + \delta x) - f(x_{0}) \approx \delta x f^{\prime}(x_{0}) + \frac{\delta x^{2}}{2} f^{\prime \prime}(x_{0}),$$

wobei $\lvert \delta x \rvert \gg \lvert \delta x^{2} \rvert$ für kleine $\delta x$ gilt.

Wenn $f^{\prime}(x_{0}) > 0$ ist und wir $\delta x < 0$ (*kleine negative Änderung*) betrachten, ist $\delta x f^{\prime}(x_{0}) < 0 \Rightarrow \Delta f(\delta x) < 0$ für kleine $\delta x$.\
Das bedeutet, dass $f(x_{0} + \delta x) < f(x_{0})$ ist, was einem Minimum widerspricht.

Andersherum können wir bei $f^{\prime}(x_{0}) < 0$, $\delta x > 0$ (*kleine positive Änderung) wählen. Damit ist wieder $\delta x f^{\prime}(x_{0}) < 0$.\
Das widerspricht ebenfalls nach derselben Logik einem Minimum.

Wenn $x_{0}$ ein lokales Minimum ist, dann darf es für hinreichend kleine positive und negative $\delta x$ keine Absenkung des Funktionswerts geben. Deshalb muss der lineare Term verschwinden, also $f^{\prime}(x_{0}) = 0$.
```

Eine gewöhnliche Funktion $f: \mathbb{R}^{n} \rightarrow \mathbb{R}$ hängt von endlich vielen unabhängigen Variablen ab. Für eine Abbildung

$$f: \mathbb{R}^{1} \rightarrow \mathbb{R}$$

können wir beispielsweise einen Freiheitsgrad $x$ frei bestimmen.

Für viele physikalische Probleme müssen wir jedoch nicht einen optimalen Punkt einer Abbildung finden, sondern die optimale Abbildung selbst. Wir haben damit unendlich viele Freiheitsgrade, da es je nach verwendeter Abbildung für jedes $x$ unendlich viele mögliche zugehörige $y=f(x)$-Werte gibt.

Die Unbekannte ist also keine Zahl mehr, sondern eine ganze Kurve.\
Das ist der Kern der Variationsrechnung.

## Das erste Funktional

Wenn wir beispielsweise eine Kurve suchen, die folgende Bedingungen erfüllt:

- die beiden Punkte $P_{1}$ und $P_{2}$ **geometrisch** kürzest möglich verbindet,
- **stetig differenzierbar** ist und
- für die gilt: $y(x_{1}) = y_{1} \, \land \, y(x_{2}) = y_{2}.$

```{figure} ../../_static/plots/analysis/variationsrechnung/einfuehrung/funktional.png
:align: center
:width: 100%

verschiedene Kurven zwischen zwei Punkten
```

Da wir die Bedingung haben, dass die gesuchte Kurve die beiden Punkte **geometrisch** kürzest möglich miteinander verbinden soll, wollen wir zunächst eine Funktion finden, die die Bogenlänge der Kurve in Abhängigkeit der verwendeten Funktion als Ergebnis liefert. Wenn wir solch eine Bogenlängenfunktion finden, können wir diese minimieren und erhalten dadurch die optimale Kurve.

Wir wollen hier Kurven betrachten, die sich als Graph einer Funktion $y(x)$ darstellen lassen.

```{figure} ../../_static/plots/analysis/variationsrechnung/einfuehrung/linienelement.png
:align: center
:width: 60%

Linienelement der Kurve "Möglichkeit II"
```

Nach Pythagoras muss in diesem infinitesimal rechtwinkligen Dreieck gelten

```{math}
\begin{align}
\mathrm{d}S^{2} &= \mathrm{d}x^{2} + \mathrm{d}y^{2} \\
\mathrm{d}S &= \sqrt{\mathrm{d}x^{2} + \mathrm{d}y^{2}} \\
\mathrm{d}S &= \mathrm{d}x \sqrt{1 + \left( \frac{\mathrm{d}y}{\mathrm{d}x} \right)^{2}}
\end{align}
```

wobei $\mathrm{d}y/\mathrm{d}x$ nichts anderes als die erste Ableitung der Funktion $y(x)$ ist.

$$\mathrm{d}S = \sqrt{1 + \left( y^{\prime}(x) \right)^{2}} \, \mathrm{d}x$$

Durch Integrieren der beiden Seiten erhalten wir schließlich eine Funktion $S$, die die Länge unserer Verbindungslinie der beiden Punkte repräsentiert.

$$\int_{x_{1}}^{x_{2}} \mathrm{d}S = \int_{x_{1}}^{x_{2}}  \sqrt{1 + \left( y^{\prime}(x) \right)^{2}} \, \mathrm{d}x $$

$$\boxed{S = \int_{x_{1}}^{x_{2}}  \sqrt{1 + \left( y^{\prime}(x) \right)^{2}} \, \mathrm{d}x}$$

Die Bogenlänge $S$ ist eine Funktion der ersten Ableitung von $y(x)$ und liefert nach Auswertung eine skalare Größe.\
Eine Funktion, die als Input eine Funktion erhält, also unendlich viele Freiheitsgrade, wird in der Mathematik als Funktional bezeichnet.

Ein Funktional ist also eine Abbildung, die einer Funktion eine Zahl zuordnet.

$$J: \mathcal{F} \rightarrow \mathbb{R}, \quad y \mapsto J[y]$$

wobei $\mathcal{F}$ ein geeigneter Funktionenraum ist.

Zur Unterscheidung schreibt man die Argumente von Funktionalen häufig in eckigen statt in runden Klammern (*Funktionen*).

Viele in der Variationsrechnung auftretende Funktionale haben die Form:

$$J[y] = \int_{a}^{b} F(x, y(x), y^{\prime}(x)) \, dx$$

Für unsere Bogenlänge wäre das Funktional also

$$S[y] = \int_{x_{1}}^{x_{2}}  \sqrt{1 + \left( y^{\prime}(x) \right)^{2}} \, \mathrm{d}x$$

---

`````{grid} 2
:gutter: 2

````{grid-item}

**Funktion**

```{figure} ../../_static/plots/analysis/variationsrechnung/einfuehrung/funktion-blockdiagramm.png
:align: center
:width: 100%

Funktion als Blockdiagramm
```
````
````{grid-item}

**Funktional**

```{figure} ../../_static/plots/analysis/variationsrechnung/einfuehrung/funktional-blockdiagramm.png
:align: center
:width: 100%

Funktional als Blockdiagramm
```
````
`````

## Typische Funktionale in der Physik

```{list-table} Übersicht der Funktionale in der Physik
:align: center

* - **Länge der Kurve**
  - $$S[y] = \int_{a}^{b}  \sqrt{1 + \left( y^{\prime}(x) \right)^{2}} \, \mathrm{d}x$$
* - **Laufzeit**
  - $$T[\gamma] = \int_{\gamma} \frac{\mathrm{d}S}{v(\vec{r})}$$
* - **Wirkung**
  - $$S[q] = \int_{t_{1}}^{t_{2}} L(q, \dot{q}, t) \, \mathrm{d}t$$
* - **Energie**
  - $$\Pi[u] = \int_{0}^{L} \left[ \frac{EA}{2} \left( u^{\prime}(x) \right)^{2} - f(x) u(x) \right] \, \mathrm{d}x$$
```