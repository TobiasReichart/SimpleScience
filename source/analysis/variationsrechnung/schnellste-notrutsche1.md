# schnellste Notrutsche I

In diesem Abschnitt wollen wir uns einer Herausforderung stellen, die der Schweizer Mathematiker **Johann Bernoulli** im Juni 1696 in der Zeitschrift *Acta Eruditorum* an die klügsten Köpfe seiner Zeit stellte. Das Problem klingt im ersten Moment simpel, barg aber zu der damaligen Zeit eine völlig neue mathematische Komplexität.

>Gegeben sind zwei Punkte $A$ und $B$ in einer vertikalen Ebene. Man bestimmt die Kurve, auf der ein Massenpunkt unter dem Einfluss der Schwerkraft und Vernachlässigung der Reibung in der kürzeste Zeit von $A$ nach $B$ gleitet.

```{figure} ../../_static/plots/analysis/variationsrechnung/notrutsche1/problem.png
:align: center
:width: 100%

Problemstellung der Brachistochrone
```

Eine solche Bahn wird als **Brachistochrone** bezeichnet, was sich aus dem Griechischen ableitet: *brachistos* (kürzester) und *chronos* (Zeit).

Johann Bernoulli setzte eine Frist von sechs Monaten, die später auf Drängen von Leibniz verlängert wurde, um sicherzustellen, dass auch Gelehrte aus ganz Europa (insbesondere aus England) teilnehmen konnten.\
Obwohl sich Galileo Galilei bereits Jahrzehnte zuvor mit diesem Problem beschäftigt hatte, gingen fünf abweichende, aber korrekte Lösungen von Johann Bernoulli, Jakob I Bernoulli (legte mit seiner Lösung die Grundlagen für die moderne Variationsrechnung), Gottfried Wilhelm Leibniz, Guillaume de L'Hospital und Sir Isaac Newton ein.

Galileo Galilei hatte in seinem Werk *Discorsi* (1638) richtigerweise vermutet, dass die gerade Linie (trotz des geometrisch kürzesten Weges) nicht die schnellste Verbindung sei. Er irrte sich jedoch bei der Form der Kurve und hielt den Kreisbogen für die Lösung. Dass die Natur eine komplexere Antwort bereithielt, sollten erst die fünf Teilnehmer der Herausforderung beweisen.

Eine legendäre Anekdote zu diesem Problem geht auf Sir Isaac Newton zurück. Er erhielt das Problem nach einem langen Arbeitstag in der Münzanstalt. Er löste es noch in derselben Nacht und schickte die Antwort anonym zurück. Als Johann Bernoulli die Lösung sah, erkannte er sofort den Stil des Engländers und rief aus: "*Ex ungue leonem*" (Man erkennt den Löwen an seiner Klaue).

## Ausgangslage

In *schnellste Notrutsche I* wollen wir das Problem unter den folgenden Voraussetzungen betrachten:

- $y(x)$ ist eine glatte Kurve im Vertikalprofil.
- Die Höhe $y$ ist nach oben positiv: $y_{2} < y_{1}$\
    $\Rightarrow$ Der Endpunkt liegt tiefer als der Startpunkt
- Ein Körper startet in Ruhe und rutscht reibungsfrei unter der Schwerkraft $g$ nach unten

**Ziel**: Finde $y(x)$, sodass die Rutschzeit minimal wird.

````{admonition} Physikalische Intuition
:class: note

Die Bahn ist am Anfang steil $\rightarrow$ schnell Geschwindigkeit aufbauen.\
Die Bahn ist am Ende flach $\rightarrow$ hohe Geschwindigkeit ausnutzen.
````

Um die Kurve der schnellsten Reise zu finden, müssen wir die Gesamtzeit $T$ als Funktion der Kurvenform $y(x)$ ausdrücken.

```{warning}
Die folgende Herleitung ist bewusst direkt über die Euler-Lagrange-Gleichung geführt.  
Sie ist korrekt, aber algebraisch aufwändig.

Gerade daran soll sichtbar werden, dass bei Variationsproblemen nicht nur die formale Anwendung der Theorie entscheidend ist, sondern bereits die Wahl einer geschickten Modellierung oder einer geeigneten Erhaltungsgröße.

Wir rechnen diesen Weg hier daher bewusst einmal aus. Nicht weil er der eleganteste ist, sondern weil er zeigt, warum man im Vorfeld über die Struktur eines Problems nachdenken sollte.
```

Da der Körper in unserer Annahme die Bahn **reibungsfrei** hinunter rutscht, muss die Energie erhalten bleiben.

$$E_{\text{kin}} + E_{\text{pot}} = \frac{1}{2} m v^{2} + m g y = m g y_{1}$$

*Da der Körper aus der Ruhe startet, gilt für*\
$y_{1}: \, v_{1} = 0 \Rightarrow E_{\text{kin}} = 0 \Rightarrow E_{\text{ges}} = E_{\text{pot}}$

$$\frac{1}{2} m v^{2} = m g \left( y_{1} - y \right)$$

Das Teilchen wandelt seine potenzielle Energie direkt in kinetische Energie um.

Ein winziges Wegstück $\mathrm{d}S$ auf einer beliebigen Kurve lässt sich über den Satz des Pythagoras ausdrücken. Wenn wir die Kurve als Funktion $y(x)$ betrachten, gilt:

$$\mathrm{d}S = \sqrt{\mathrm{d} x^{2} + \mathrm{d} y^{2}} = \sqrt{1 + \left( y^{\prime}(x) \right)^{2}} \, \mathrm{d} x$$

Um die Gesamtfahrzeit $T$ zu berechnen, nutzen wir den Zusammenhang zwischen Geschwindigkeit, Weg und Zeit. Da wir die Form der Kurve noch nicht kennen, wissen wir zunächst nicht, wie sich die Zeit $t$ verhält. Wir wissen jedoch, dass die Geschwindigkeit $v$ an jedem Punkt der Bahn durch die Energieerhaltung festgelegt ist.

$$v(y) = \sqrt{2 g \left( y_{1} - y(x) \right)} = \frac{\mathrm{d} S}{\mathrm{d}t}$$

Wir betrachten das Zeitintervall $\mathrm{d} t$, das das Teilchen benötigt, um ein infinitesimal kurzes Wegstück ds zurückzulegen. Da $v = \frac{\mathrm{d} S}{\mathrm{d} t}$ gilt, lässt sich das Zeitintervall formal als

$$\mathrm{d} t = \frac{\mathrm{d} S}{v}$$

ausdrücken.

$$\text{mit} \, T = \int_{t_{1}}^{t_{2}} \, \mathrm{d}t \quad \text{und} \quad \mathrm{d}S = \sqrt{1 + \left( y^{\prime}(x) \right)^{2}} \, \mathrm{d}x$$


````{dropdown} mathematische Randnotiz
:icon: comment

Da $v = \frac{\mathrm{d} S}{\mathrm{d}t} > 0$ (Bewegung vorwärts entlang der Bahn, das Teilchen kehrt nicht um) ist, muss $S(t)$ (lokal) streng monoton steigen und ist damit invertierbar. Wir können also die Zeit $t$ als Funktion des Weges $S$ auffassen.

Durch Substitution schreiben wir nun unser Integral für die Gesamtzeit nun in der folgenden Form:

$$T = \int_{S(t_{1})}^{S(t_{2})} \frac{1}{v(S)} \, \mathrm{d}S$$

Wir definieren $S_{1} \coloneqq S(t_{1}) = 0$ und $S_{2} \coloneqq S(t_{2})$.

$$T = \int_{0}^{S(t_{2})} \frac{1}{v(S)} \, \mathrm{d}S,$$

wobei die Bogenlänge

$$S(x) = S_{1} + \int_{x_{1}}^{x} \sqrt{1 + \left( y^{\prime}(x) \right)^{2}} \, \mathrm{d}x$$

ist. Damit liegt der Startpunkt bei $x=x_{1}$ und $S=S_{1}$

Damit können wir nun das Zeitfunktional $T$ aufstellen.
````

$$T[y] = \int_{x_{1}}^{x_{2}} \underbrace{\frac{\sqrt{1 + \left( y^{\prime}(x) \right)^{2}}}{\sqrt{2 g \left( y_{1} - y(x) \right)}}}_{F(x, \, y, \, y^{\prime})} \, \mathrm{d}x$$

***Hinweis***: *Der Integrand $F(x, \, y, \, y^{\prime})$ hängt nicht explizit von $x$ ab. Damit würde die* ***Beltrami Identität*** *(benannt nach dem Mathematiker Eugenio Beltrami) gelten und eine zugehörige Erhaltungsgröße existieren (Emmy Noether). Da wir diese jedoch noch nicht kennen, müssen wir in diesem Abschnitt leider ohne sie auskommen.*

## Anwenden der Euler-Lagrange-Gleichung

Die Euler-Lagrange-Gleichung lautet:

$$\frac{\partial F}{\partial y} - \frac{\mathrm{d}}{\mathrm{d} x} \left( \frac{\partial F}{\partial y^{\prime}} \right) = 0$$

Den Integrand $F(y, \, y^{\prime})$ können wir auch schreiben als:

$$F(y, \, y^{\prime}) = \left[ 1 + \left( y^{\prime}(x) \right)^{2} \right]^{\frac{1}{2}} \cdot \left[ 2 g \left( y_{1} - y(x) \right) \right]^{-\frac{1}{2}}$$

Zunächst berechnen wir die beiden partiellen Ableitungen des Integranden $F$. Der Übersichtlichkeit wegen definieren wir $y \coloneqq y(x)$ und $y^{\prime} \coloneqq y^{\prime}(x)$.

```{math}
\begin{align}
\frac{\partial F}{\partial y} &= \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{\frac{1}{2}} \cdot \ccancel{\red}{\left(- \frac{1}{2} \right)} \left[ 2 g \left( y_{1} - y \right) \right]^{-\frac{3}{2}} \left(\ccancel{\red}{- 2}g \right) \\
\frac{\partial F}{\partial y} &= \frac{g \sqrt{1 + \left( y^{\prime} \right)^{2}}}{\left[ 2 g \left( y_{1} - y \right) \right]^{\frac{3}{2}}} = \frac{g \sqrt{1 + \left( y^{\prime} \right)^{2}}}{\left( 2 g \right)^{\frac{3}{2}} \left( y_{1} - y \right)^{\frac{3}{2}}} \\
\frac{\partial F}{\partial y} &= \frac{ \ccancel{\red}{g} \sqrt{1 + \left( y^{\prime} \right)^{2}}}{ \sqrt{2^{2} \cdot 2} \sqrt{\ccancel{\red}{g^{2}} \cdot g} \, \left( y_{1} - y \right)^{\frac{3}{2}}} = \frac{ \sqrt{1 + \left( y^{\prime} \right)^{2}}}{ \sqrt{2^{3} g \frac{g^{2}}{g^{2}}} \, \left( y_{1} - y \right)^{\frac{3}{2}}}
\end{align}
```

$$\boxed{\frac{\partial F}{\partial y} = \frac{g \sqrt{1 + \left( y^{\prime} \right)^{2}}}{\left[ 2g \left( y_{1} - y \right) \right]^{\frac{3}{2}}}}$$

---

$$\frac{\partial F}{\partial y^{\prime}} = \ccancel{\red}{\frac{1}{2}} \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{-\frac{1}{2}} \cdot \ccancel{\red}{2} y^{\prime} \cdot \left[ 2 g \left( y_{1} - y \right) \right]^{-\frac{1}{2}}$$

$$\boxed{\frac{\partial F}{\partial y^{\prime}} = \frac{y^{\prime}}{\sqrt{2 g \left( y_{1} - y \right)} \cdot \sqrt{1 + \left( y^{\prime} \right)^{2}}}}$$

Die nächste Ableitung $\frac{\mathrm{d}}{\mathrm{d} x}$, die wir nun berechnen müssen, ist nun eine sehr aufwändige Ableitung. Es lohnt sich daher die Ableitung aufzuteilen und Schritt für Schritt zu berechnen. Dafür definieren wir

$$\frac{\mathrm{d}}{\mathrm{d} x} \left( \frac{\partial F}{\partial y^{\prime}} \right): \quad \frac{\partial F}{\partial y^{\prime}} = y^{\prime} \cdot A(x) \cdot B(x)$$

mit

$$A(x) = \left[ 2 g \left( y_{1} - y \right) \right]^{-\frac{1}{2}} \quad \text{und} \quad B(x) = \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{-\frac{1}{2}},$$

wobei $A \coloneqq A(x)$ und $B \coloneqq B(x)$.

Damit ergibt die Ableitung

$$\frac{\mathrm{d}}{\mathrm{d} x} \left( \frac{\partial F}{\partial y^{\prime}} \right) = \underbrace{y^{\prime \prime} A B}_{\text{Term 1}} + \underbrace{y^{\prime} A^{\prime} B}_{\text{Term 2}} + \underbrace{y^{\prime} A B^{\prime}}_{\text{Term 3}}$$

````{admonition} Nebenrechnung
:class: hint

```{math}
\frac{\mathrm{d}}{\mathrm{d} x} A &= \ccancel{\red}{- \frac{1}{2}} \left[ 2g \left( y_{1} - y \right) \right]^{-\frac{3}{2}} \cdot \ccancel{\red}{-2} g y^{\prime} \\
A^{\prime} &= g y^{\prime} \left[ 2g \left( y_{1} - y \right) \right]^{-\frac{3}{2}}
```
---
```{math}
\frac{\mathrm{d}}{\mathrm{d} x} B &= - \ccancel{\red}{\frac{1}{2}} \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{-\frac{3}{2}} \ccancel{\red}{2} y^{\prime} y^{\prime \prime} \\
B^{\prime} &= - y^{\prime} y^{\prime \prime} \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{-\frac{3}{2}}
```
````

Eingesetzt in die die Terme 1, 2 und 3 ergibt sich:

**Term 1**

```{math}
y^{\prime \prime} A B &= y^{\prime \prime} \cdot \left[ 2 g \left( y_{1} - y \right) \right]^{-\frac{1}{2}} \cdot \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{-\frac{1}{2}} \\
&= \frac{y^{\prime \prime}}{\sqrt{1 + \left( y^{\prime} \right)^{2}} \sqrt{2 g \left( y_{1} - y \right)}}
```

**Term 2**

```{math}
y^{\prime} A^{\prime} B &= y^{\prime} \cdot g y^{\prime} \left[ 2g \left( y_{1} - y \right) \right]^{-\frac{3}{2}} \cdot \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{-\frac{1}{2}} \\
&= \frac{g \left( y^{\prime} \right)^{2} }{\left[ 2g \left( y_{1} - y \right) \right]^{\frac{3}{2}} \sqrt{1 + \left( y^{\prime} \right)^{2}}}
```

**Term 3**

```{math}
y^{\prime} A B^{\prime} &= y^{\prime} \cdot \left[ 2 g \left( y_{1} - y \right) \right]^{-\frac{1}{2}} \cdot \left\{- y^{\prime} y^{\prime \prime} \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{-\frac{3}{2}} \right\} \\
&= - \frac{\left( y^{\prime} \right)^{2} y^{\prime \prime}}{\sqrt{2 g \left( y_{1} - y \right)} \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{\frac{3}{2}}}
```

Term 1 und 3 lassen sich vereinfachen:

```{math}
(\text{1}) + (\text{3}) &= \small{\frac{y^{\prime \prime}}{\sqrt{2 g \left( y_{1} - y \right)}} \left( \frac{1}{\sqrt{1 + \left( y^{\prime} \right)^{2}}} - \frac{\left( y^{\prime} \right)^{2}}{\left( 1 + \left( y^{\prime} \right)^{2} \right) \sqrt{1 + \left( y^{\prime} \right)^{2}}} \right)} \\
&= \small{\frac{y^{\prime \prime}}{\sqrt{2 g \left( y_{1} - y \right)}} \left( \frac{\left( 1 + \left( y^{\prime} \right)^{2} \right)}{\left( 1 + \left( y^{\prime} \right)^{2} \right) \sqrt{1 + \left( y^{\prime} \right)^{2}}} - \frac{\left( y^{\prime} \right)^{2}}{\left( 1 + \left( y^{\prime} \right)^{2} \right) \sqrt{1 + \left( y^{\prime} \right)^{2}}} \right)} \\
&= \small{\frac{y^{\prime \prime}}{\sqrt{2 g \left( y_{1} - y \right)}} \frac{1 \ccancel{\red}{+ \left( y^{\prime} \right)^{2} - \left( y^{\prime} \right)^{2}}}{\left( 1 + \left( y^{\prime} \right)^{2} \right) \sqrt{1 + \left( y^{\prime} \right)^{2}}}} \\
&= \small{\frac{y^{\prime \prime}}{\sqrt{2 g \left( y_{1} - y \right)} \left( 1 + \left( y^{\prime} \right)^{2} \right)^{\frac{3}{2}}}}
```

Womit der zweite Summant $\frac{\mathrm{d}}{\mathrm{d} x} \left( \frac{\partial F}{\partial y^{\prime}} \right)$ der Euler-Lagrange-Gleichung zu

$$\small{\frac{\mathrm{d}}{\mathrm{d} x} \left( \frac{\partial F}{\partial y^{\prime}} \right) = \frac{g \left( y^{\prime} \right)^{2} }{\left[ 2g \left( y_{1} - y \right) \right]^{\frac{3}{2}} \sqrt{2 g \left( y_{1} - y \right)}} + \frac{y^{\prime \prime}}{\sqrt{2 g \left( y_{1} - y \right)} \left( 1 + \left( y^{\prime} \right)^{2} \right)^{\frac{3}{2}}}}$$

wird. Wir können nun alles was wir bis dato berechnet haben in die Euler-Lagrange-Gleichung einsetzen.


$$\frac{\partial F}{\partial y} = \frac{\mathrm{d}}{\mathrm{d} x} \left( \frac{\partial F}{\partial y^{\prime}} \right)$$

$$\small{\frac{g \sqrt{1 + \left( y^{\prime} \right)^{2}}}{\left[ 2g \left( y_{1} - y \right) \right]^{\frac{3}{2}}} = \frac{g \left( y^{\prime} \right)^{2} }{\left[ 2g \left( y_{1} - y \right) \right]^{\frac{3}{2}} \sqrt{2 g \left( y_{1} - y \right)}} + \frac{y^{\prime \prime}}{\sqrt{2 g \left( y_{1} - y \right)} \left( 1 + \left( y^{\prime} \right)^{2} \right)^{\frac{3}{2}}}}$$

Um die DGL auf eine handhabbare Form zu bringen, wollen wir die Brüche auf einen gemeinsamen Nenner bringen. Hierfür multiplizieren wir beide Seiten mit

$$\sqrt{2g} \left( y_{1} - y \right)^{\frac{3}{2}} \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{\frac{3}{2}}.$$

Dadurch entsteht der folgende Ausdruck.

$$\small{\frac{g \sqrt{1 + \left( y^{\prime} \right)^{2}} \sqrt{2g} \left( y_{1} - y \right)^{\frac{3}{2}} \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{\frac{3}{2}}}{\left[ 2g \left( y_{1} - y \right) \right]^{\frac{3}{2}}}} = \small{\frac{g \left( y^{\prime} \right)^{2} \sqrt{2g} \left( y_{1} - y \right)^{\frac{3}{2}} \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{\frac{3}{2}}}{\left[ 2g \left( y_{1} - y \right) \right]^{\frac{3}{2}} \sqrt{2 g \left( y_{1} - y \right)}} + \frac{y^{\prime \prime} \sqrt{2g} \left( y_{1} - y \right)^{\frac{3}{2}} \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{\frac{3}{2}}}{\sqrt{2 g \left( y_{1} - y \right)} \left( 1 + \left( y^{\prime} \right)^{2} \right)^{\frac{3}{2}}}}$$

````{admonition} Kürzen
:class: hint

$$\small{\frac{\ccancel{\red}{g} \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{\frac{1}{2}} \ccancel{\purple}{\sqrt{2g}} \ccancel{\orange}{\left( y_{1} - y \right)^{\frac{3}{2}}} \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{\frac{3}{2}}}{\ccancel{\orange}{\left( y_{1} - y \right)^{\frac{3}{2}}} \ccancel{\purple}{\sqrt{2g}} \, 2 \ccancel{\red}{g}}} = $$

$$\small{\frac{\ccancel{\purple}{g} \left( y^{\prime} \right)^{2} \ccancel{\red}{\sqrt{2g}} \ccancel{\orange}{\left( y_{1} - y \right)^{\frac{3}{2}}} \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{\ccancel{\green}{\frac{3}{2}}}}{2 \ccancel{\purple}{g} \ccancel{\red}{\sqrt{2g}} \ccancel{\orange}{\left( y_{1} - y \right)^{\frac{3}{2}}} \ccancel{\green}{\left[ 1 + \left( y^{\prime} \right)^{2} \right]^{\frac{1}{2}}}} + \frac{y^{\prime \prime} \ccancel{\red}{\sqrt{2g}} \left( y_{1} - y \right)^{\ccancel{\orange}{\frac{3}{2}}} \ccancel{\purple}{\left[ 1 + \left( y^{\prime} \right)^{2} \right]^{\frac{3}{2}}}}{\ccancel{\red}{\sqrt{2g}} \ccancel{\orange}{\left( y_{1} - y \right)^{\frac{1}{2}}} \ccancel{\purple}{\left( 1 + \left( y^{\prime} \right)^{2} \right)^{\frac{3}{2}}}}}$$
````

$$\frac{1}{2} \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{2} = \frac{1}{2} \left( y^{\prime} \right)^{2} \left[ 1 + \left( y^{\prime} \right)^{2} \right] + y^{\prime \prime} \left( y_{1} - y \right)$$

Im nächsten Schritt können wir nun noch $\frac{1}{2} \left[ 1 + \left( y^{\prime} \right)^{2} \right]$ auf die andere Seite bringen und ausklammern.

$$0 = y^{\prime \prime} \left( y_{1} - y \right) + \frac{1}{2} \left[ 1 + \left( y^{\prime} \right)^{2} \right] \left[ - \left( 1 + \ccancel{\red}{\left( y^{\prime} \right)^{2}} \right) + \ccancel{\red}{\left( y^{\prime} \right)^{2}} \right] \quad \vert \cdot \left( -2 \right)$$

$$\boxed{0 = - 2 y^{\prime \prime} \left( y_{1} - y \right) + \left[ 1 + \left( y^{\prime} \right)^{2} \right]}$$

Diese nichtlineare Differentialgleichung 2. Ordnung von $y(x)$ müssen wir im nächsten Abschnitt lösen, um die explizite Bahnform zu erhalten.

````{admonition} Warum verschwindet $g$ in der DGL?
:class: note

$g$ ist lediglich eine Skalierung der Zeit. Die Bahn selbst ist unabhängig von $g$.\
$\Rightarrow$ $g$ bestimmt, wie schnell wir die Bahn hinunter rutschen, hat aber selbst keinen Einfluss auf die optimale Bahn.
````

## Vereinfachen der DGL


## Lösen der DGL


