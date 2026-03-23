# Herleitung der Euler-Lagrange-Gleichung

In der {ref}`Einführung <Einführung Variationsrechnung>` der Variationsrechnung haben wir bereits die Bogenlänge, die zwei Punkte $P_{1}$ und $P_{2}$ verbindet, über das Funktional

$$S[y] = \int_{x_{1}}^{x_{2}}  \underbrace{\sqrt{1 + \left( y^{\prime}(x) \right)^{2}}}_{F(x,\, y(x),\, y^{\prime}(x))} \, \mathrm{d}x$$

beschrieben.

```{figure} ../../_static/plots/analysis/variationsrechnung/einfuehrung/funktional.png
:align: center
:width: 100%

verschiedene Kurven zwischen zwei Punkten
```

## Anforderungen an die gesuchte Kurve

Um nun die **geometrisch** kürzeste Verbindung zwischen diesen Punkten zu finden, fordern wir folgende zusätzlichen Voraussetzungen:

1. Die Funktion $F$ soll eine Abbildung aus dem abgeschlossenen Intervall von $x_{1}$ bis $x_{2}$, sowie für jeden Funktionswert $y \in \mathbb{R}$ und jede Steigung $y^{\prime} \in \mathbb{R}$ in die Reellen Zahlen sein.

$$F: \left[ x_{1},\, x_{2} \right] \times \mathbb{R} \times \mathbb{R} \rightarrow \mathbb{R}, \quad \left(x,\, y,\, y^{\prime} \right) \mapsto F(x,\, y,\, y^{\prime})$$

2. **Glattheit des Integranden** $F$ (*partielle Integration in Herleitung*):\
    $F$ sei hinreichend glatt, insbesondere stetig partiell differenzierbar nach seinen Argumenten.

3. **Randbedingung**

$$y(x_{1}) = y_{1} \quad \land \quad y(x_{2}) = y_{2}$$

Aus diesen Anforderungen ergibt sich die Menge $\mathcal{A}$ der zulässigen Funktionen

$$\mathcal{A} \coloneqq \left\{ y \in \mathcal{C}^{1}([x_{1},\, x_{2}]) \, \vert \, y(x_{1}) = y_{1}, \, y(x_{2}) = y_{2} \right\}$$

Dabei bezeichnet $\mathcal{C}^{1}([x_{1},\, x_{2}])$ den Raum aller einmal stetig differenzierbaren Funktionen auf $[x_{1},\, x_{2}]$.\
Unsere Funktion muss einmal stetig differenzierbar auf dem Intervall von $x_{1}$ bis $x_{2}$ sein, da in $F$ die erste Ableitung $y^{\prime}$ vorkommt.

Um nun die stationäre Kurve für unsere Problemstellung zu finden, suchen wir eine Funktion aus der Menge der zulässigen Funktionen $\mathcal{A}$, die das Funktional $S[y]$ extremal macht.

(Herleitung Euler-Lagrange Variation)=
## Herleitung über eine Variationsfamilie

Unter der Annahme, dass $y(x) \in \mathcal{A}$ das Funktional extremal macht (*optimale Kurve*), können wir eine Variationsfamilie definieren.\
Im Grunde ist das eine zweite nicht optimale Funktion $y_{\varepsilon}(x)$ die leicht von der extremalen Funktion $y(x)$ abweicht und über einen Parameter $\varepsilon$ steuerbar ist. Genauergesagt ist das eine gestörte Nachbarfunktion innerhalb der zulässigen Klasse.

**Variationsfamilie**

$$y_{\varepsilon}(x) = y(x) + \varepsilon \eta(x)$$

wobei $\varepsilon \in \mathbb{R}$ klein ist und $\eta(x)$  eine beliebige Störfunktion ist.

```{figure} ../../_static/plots/analysis/variationsrechnung/herleitung/variationsfamilie.png
:align: center
:width: 100%

Gesuchte Kurve $y$ und gestörte Kurve $y_{\varepsilon}$
```

Damit $y_{\varepsilon}$ die beiden Punkte trifft, gilt weiter

$$\eta(x_{1}) = \eta(x_{2}) = 0$$

Da der Integrand $F$ von der Steigung $y^{\prime}(x)$ abhängt, muss jede zulässige Variation $y_{\varepsilon}(x)$ ebenfalls differenzierbar sein.

$$\Rightarrow \eta(x) \in \mathcal{C}^{1}([x_{1},\, x_{2}])$$

$y(x)$ soll die optimale Kurve sein, was bedeuten muss, dass gilt

$$S[y] \leq S[y_{\varepsilon}]$$

Nach der Definition unserer Variationsfamilie $y_{\varepsilon}$ ist das Funktional $S[y_{\varepsilon}]$ eine Funktion von $\varepsilon$ und besitzt ein Extremum bei $\varepsilon=0$.

$\Rightarrow$ Für $\varepsilon \neq 0$ weicht die Funktion $y_{\varepsilon}(x)$ immer weiter von der optimalen Funktion $y(x)$ ab.\
Für $\varepsilon = 0$ gilt $y_{\varepsilon}(x) = y(x)$

Durch die Variation wird das Funktional zu einer gewöhnlichen Funktion des Parameters $\varepsilon$, nämlich

$$\Phi(\varepsilon) \coloneqq S[y_{\varepsilon}] = S[y(x) + \varepsilon \eta(x)]$$

```{figure} ../../_static/plots/analysis/variationsrechnung/herleitung/funktional_minimum.png
:align: center
:width: 100%

Minimum des Funktionals $S[y_{\varepsilon}]$
```

Für $\Phi(\varepsilon)$ können wir wieder unsere Werkzeuge aus der klassischen Analysis verwenden um das Minimum dieser Funktion von $\varepsilon$ zu finden.

**Notwendige Bedingung**

```{math}
\begin{align}
0 &= \frac{\mathrm{d}\Phi}{\mathrm{d} \varepsilon} \bigg|_{\varepsilon=0} \quad \Rightarrow \Phi^{\prime}(0) = 0\\
0 &= \frac{\mathrm{d}}{\mathrm{d} \varepsilon} \int_{x_{1}}^{x_{2}} F(x,\, y + \varepsilon \eta,\, y^{\prime} + \varepsilon \eta') \, \mathrm{d}x \bigg|_{\varepsilon=0}
\end{align}
```

Dabei setzen wir voraus, dass der Integrand $F$ hinreichend glatt ist, und dass $y(x)$ sowie die Variationsfunktion $\eta(x)$ so gewählt sind, dass Ableitung und Integration vertauscht werden dürfen (*Leibniz-Regel*)

$$0 = \int_{x_{1}}^{x_{2}} \frac{\partial}{\partial \varepsilon} F(x,\, y + \varepsilon \eta,\, y^{\prime} + \varepsilon \eta') \, \mathrm{d}x \bigg|_{\varepsilon=0}$$

````{admonition} Mehrdimensionale Kettenregel
:class: note

$$\frac{\partial}{\partial \varepsilon} F(x,\, y + \varepsilon \eta,\, y^{\prime} + \varepsilon \eta^{\prime})$$

$\Rightarrow$ $\varepsilon$ beeinflusst $F$ nicht direkt, sondern nur über die Argumente $y$ und $y^{\prime}$.

```{math}
\varepsilon \rightarrow
\begin{cases} 
y_{\varepsilon} = y + \varepsilon \eta, & \frac{\partial y_{\varepsilon}}{\partial \varepsilon} = \eta \\
y_{\varepsilon}^{\prime} = y^{\prime} + \varepsilon \eta^{\prime}, & \frac{\partial y_{\varepsilon}^{\prime}}{\partial \varepsilon} = \eta^{\prime} \\
x_{\varepsilon} = x, & \frac{\partial x_{\varepsilon}}{\partial \varepsilon} = 0
\end{cases}
```

$$\frac{\partial}{\partial \varepsilon} F(x_{\varepsilon},\, y_{\varepsilon},\, y_{\varepsilon}^{\prime}) = \frac{\partial F}{\partial y} \eta + \frac{\partial F}{\partial y^{\prime}} \eta^{\prime} + \ccancel{\red}{\frac{\partial F}{\partial x} \cdot 0}$$
````

Damit ist die Ableitung der Funktion $\Phi(\varepsilon)$ bzw. des Funktionals $S[y + \varepsilon \eta]$ nach $\varepsilon$

```{math}
\begin{align}
0 = \frac{\mathrm{d}}{\mathrm{d} \varepsilon} S[y + \varepsilon \eta] \bigg|_{\varepsilon=0} &= \int_{x_{1}}^{x_{2}} \frac{\partial F}{\partial y} \eta + \frac{\partial F}{\partial y^{\prime}} \eta^{\prime} \, \mathrm{d}x \\
&= \int_{x_{1}}^{x_{2}} \frac{\partial F}{\partial y} \eta \, \mathrm{d}x + \int_{x_{1}}^{x_{2}} \frac{\partial F}{\partial y^{\prime}} \eta^{\prime} \, \mathrm{d}x
\end{align}
```

````{admonition} Nebenrechnung
:class: hint

$$\int_{x_{1}}^{x_{2}} \frac{\partial F}{\partial y^{\prime}} \eta^{\prime} \, \mathrm{d}x$$

Dieses Integral kann durch partielle Integration vereinfacht werden. Dabei definieren wir

$$u = \frac{\partial F}{\partial y^{\prime}} \quad \land \quad v^{\prime} = \eta^{\prime}$$

was damit zu 

$$u^{\prime} = \frac{\mathrm{d}}{\mathrm{d} x} \left( \frac{\partial F}{\partial y^{\prime}} \right) \quad \land \quad v = \int_{x_{1}}^{x_{2}} \eta^{\prime} \, \mathrm{d}x = \left[ \eta \right]_{x_{1}}^{x_{2}}$$

führt.
````

Somit können wir die notwendige Bedingung auch schreiben als:

```{math}
\begin{align}
0 &= \int_{x_{1}}^{x_{2}} \frac{\partial F}{\partial y} \eta \, \mathrm{d}x + \underbrace{\left[ \frac{\partial F}{\partial y^{\prime}} \eta \right]_{x_{1}}^{x_{2}}}_{= 0 \text{, da } \eta(x_{1}) = \eta(x_{2}) = 0} - \int_{x_{1}}^{x_{2}} \frac{\mathrm{d}}{\mathrm{d} x} \left( \frac{\partial F}{\partial y^{\prime}} \right) \eta \, \mathrm{d}x \\
0 &= \int_{x_{1}}^{x_{2}} \left[ \frac{\partial F}{\partial y} - \frac{\mathrm{d}}{\mathrm{d} x} \left( \frac{\partial F}{\partial y^{\prime}} \right) \right] \eta \, \mathrm{d}x
\end{align}
```

Da $\eta(x)$ eine beliebige hinreichend glatte Testfunktion mit verschwindenden Randwerten ist, folgt aus dem Fundamentallemma der Variationsrechnung, dass der Klammerausdruck fast überall, unter den vorliegenden Glattheitsannahmen sogar überall, verschwinden muss.

$$\boxed{\frac{\partial F}{\partial y} - \frac{\mathrm{d}}{\mathrm{d} x} \left( \frac{\partial F}{\partial y^{\prime}} \right) = 0}$$

Das ist die **Euler-Lagrange-Gleichung**.

Stark vereinfacht sagt das Fundamentallemma: Wenn das Integral über ein Produkt aus einer Funktion $f(x)$ und einer völlig beliebigen Testfunktion $\eta(x)$ immer null ergibt, dann muss die Funktion $f(x)$ selbst schon überall null sein.

## Die geometrisch kürzeste Verbindung

```{figure} ../../_static/plots/analysis/variationsrechnung/herleitung/kuerzester_weg.png
:align: center
:width: 100%

mögliche Kurve für die Verbindung der beiden Punkte
```

In diesem Abschnitt wollen wir nun mit unserem aufgestellten Funktional für die Beschreibung der Länge einer Kurve

$$S[y] = \int_{x_{1}}^{x_{2}} \underbrace{\sqrt{1+ \left( y^{\prime} \right)^{2}}}_{=F} \, \mathrm{d}x = \int_{x_{1}}^{x_{2}} \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{\frac{1}{2}} \, \mathrm{d}x$$

und der im letzten {ref}`Abschnitt <Herleitung Euler-Lagrange Variation>` hergeleiteten Euler-Lagrange-Gleichung

$$\frac{\partial F}{\partial y} - \frac{\mathrm{d}}{\mathrm{d} x} \left( \frac{\partial F}{\partial y^{\prime}} \right) = 0$$

die kürzeste Verbindung der beiden Punkte ermitteln.

Im ersten Schritt berechnen wir die beiden partiellen Ableitungen unseres Integranden $F$.

````{admonition} Nebenrechnung
:class: hint

$$\frac{\partial}{\partial y} \left\{ \left( 1 + \left( y^{\prime} \right)^{2} \right)^{\frac{1}{2}} \right\} = 0 $$

$$\frac{\partial}{\partial y^{\prime}} \left\{ \left( 1 + \left( y^{\prime} \right)^{2} \right)^{\frac{1}{2}} \right\} = \ccancel{\red}{\frac{1}{2}} \left( 1 + \left( y^{\prime} \right)^{2} \right)^{-\frac{1}{2}} \cdot \ccancel{\red}{2} y^{\prime} = \frac{y^{\prime}}{\sqrt{1 + \left( y^{\prime} \right)^{2}}}$$
````

Diese Terme eingesetzt in die Euler-Lagrange-Gleichung ergeben

$$0 - \frac{\mathrm{d}}{\mathrm{d} x} \underbrace{\left( \frac{y^{\prime}}{\sqrt{1 + \left( y^{\prime} \right)^{2}}} \right)}_{g(x)} = 0$$

$\Rightarrow$ Da $g^{\prime}(x) = 0$ ist, muss $g(x) = \text{konst.}$ sein.

$$\frac{y^{\prime}}{\sqrt{1 + \left( y^{\prime} \right)^{2}}} = C = \text{konst.}$$

````{dropdown} ausführliche Umformung
:icon: comment

```{math}

\begin{align}
y^{\prime} &= C \cdot \sqrt{1 + \left( y^{\prime} \right)^{2}} \\
\left( y^{\prime} \right)^{2} &= C^{2} \cdot \left( 1 + \left( y^{\prime} \right)^{2} \right) \\
\left( y^{\prime} \right)^{2} &= C^{2} + C^{2} \left( y^{\prime} \right)^{2} \\
\left( y^{\prime} \right)^{2} \left( 1 - C^{2} \right) &= C^{2} \\
\left( y^{\prime} \right)^{2} &= \frac{C^{2}}{\left( 1 - C^{2} \right)} \\
y^{\prime } &= \underbrace{\pm \sqrt{\frac{C^{2}}{\left( 1 - C^{2} \right)}}}_{\text{konst.}} = a \\
\end{align}
```
````

$$y^{\prime}(x) = a, \quad a \in \mathbb{R} \, \text{konst.}$$

Durch Integrieren der beiden Seiten, erhalten wir die Funktion $y(x)$, die diese DGL erfüllt.

$$y = \int y^{\prime} \, \mathrm{d}x = \int a \, \mathrm{d}x = ax + b$$

````{admonition} Merke
:class: error

Die kürzeste geometrische Verbindung der beiden Punkte $P_{1}$ und $P_{2}$ ist eine Gerade.
````

Eine solche Verbindung wird als **Geodäte** bezeichnet und ist im Euklidschen Raum stets eine Gerade.

In allgemeinen Räumen müssen Geodäten nicht global die kürzeste Verbindung sein. Sie sind zunächst Kurven, die ein geeignetes Variationsproblem stationär machen.\
In manchen Anwendungen, etwa in der Relativitätstheorie, extremieren Geodäten nicht eine Länge, sondern beispielsweise die Eigenzeit. Dort können sie lokal auch ein Maximum dieser Größe darstellen.