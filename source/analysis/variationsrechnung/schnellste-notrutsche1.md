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
- Die Höhe $y$ ist nach oben positiv: $y_{B} < y_{A}$\
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

$$E_{\text{kin}} + E_{\text{pot}} = \frac{1}{2} m v^{2} + m g y = m g y_{A}$$

*Da der Körper aus der Ruhe startet, gilt für*\
$y_{A}: \, v_{1} = 0 \Rightarrow E_{\text{kin}} = 0 \Rightarrow E_{\text{ges}} = E_{\text{pot}}$

$$\frac{1}{2} m v^{2} = m g \left( y_{A} - y \right)$$

Das Teilchen wandelt seine potenzielle Energie direkt in kinetische Energie um.

Ein winziges Wegstück $\mathrm{d}S$ auf einer beliebigen Kurve lässt sich über den Satz des Pythagoras ausdrücken. Wenn wir die Kurve als Funktion $y(x)$ betrachten, gilt:

$$\mathrm{d}S = \sqrt{\mathrm{d} x^{2} + \mathrm{d} y^{2}} = \sqrt{1 + \left( y^{\prime}(x) \right)^{2}} \, \mathrm{d} x$$

Um die Gesamtfahrzeit $T$ zu berechnen, nutzen wir den Zusammenhang zwischen Geschwindigkeit, Weg und Zeit. Da wir die Form der Kurve noch nicht kennen, wissen wir zunächst nicht, wie sich die Zeit $t$ verhält. Wir wissen jedoch, dass die Geschwindigkeit $v$ an jedem Punkt der Bahn durch die Energieerhaltung festgelegt ist.

$$v(y) = \sqrt{2 g \left( y_{A} - y(x) \right)} = \frac{\mathrm{d} S}{\mathrm{d}t}$$

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

$$S(x) = S_{1} + \int_{x_{A}}^{x} \sqrt{1 + \left( y^{\prime}(x) \right)^{2}} \, \mathrm{d}x$$

ist. Damit liegt der Startpunkt bei $x=x_{A}$ und $S=S_{1}$

Damit können wir nun das Zeitfunktional $T$ aufstellen.
````

$$T[y] = \int_{x_{A}}^{x_{B}} \underbrace{\frac{\sqrt{1 + \left( y^{\prime}(x) \right)^{2}}}{\sqrt{2 g \left( y_{A} - y(x) \right)}}}_{F(x, \, y, \, y^{\prime})} \, \mathrm{d}x$$

***Hinweis***: *Der Integrand $F(x, \, y, \, y^{\prime})$ hängt nicht explizit von $x$ ab. Damit würde die* ***Beltrami Identität*** *(benannt nach dem Mathematiker Eugenio Beltrami) gelten und eine zugehörige Erhaltungsgröße existieren (Emmy Noether). Da wir diese jedoch noch nicht kennen, müssen wir in diesem Abschnitt leider ohne sie auskommen.*

## Anwenden der Euler-Lagrange-Gleichung

Die Euler-Lagrange-Gleichung lautet:

$$\frac{\partial F}{\partial y} - \frac{\mathrm{d}}{\mathrm{d} x} \left( \frac{\partial F}{\partial y^{\prime}} \right) = 0$$

Den Integrand $F(y, \, y^{\prime})$ können wir auch schreiben als:

$$F(y, \, y^{\prime}) = \left[ 1 + \left( y^{\prime}(x) \right)^{2} \right]^{\frac{1}{2}} \cdot \left[ 2 g \left( y_{A} - y(x) \right) \right]^{-\frac{1}{2}}$$

Zunächst berechnen wir die beiden partiellen Ableitungen des Integranden $F$. Der Übersichtlichkeit wegen definieren wir $y \coloneqq y(x)$ und $y^{\prime} \coloneqq y^{\prime}(x)$.

```{math}
\begin{align}
\frac{\partial F}{\partial y} &= \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{\frac{1}{2}} \cdot \ccancel{\red}{\left(- \frac{1}{2} \right)} \left[ 2 g \left( y_{A} - y \right) \right]^{-\frac{3}{2}} \left(\ccancel{\red}{- 2}g \right) \\
\frac{\partial F}{\partial y} &= \frac{g \sqrt{1 + \left( y^{\prime} \right)^{2}}}{\left[ 2 g \left( y_{A} - y \right) \right]^{\frac{3}{2}}} = \frac{g \sqrt{1 + \left( y^{\prime} \right)^{2}}}{\left( 2 g \right)^{\frac{3}{2}} \left( y_{A} - y \right)^{\frac{3}{2}}} \\
\frac{\partial F}{\partial y} &= \frac{ \ccancel{\red}{g} \sqrt{1 + \left( y^{\prime} \right)^{2}}}{ \sqrt{2^{2} \cdot 2} \sqrt{\ccancel{\red}{g^{2}} \cdot g} \, \left( y_{A} - y \right)^{\frac{3}{2}}} = \frac{ \sqrt{1 + \left( y^{\prime} \right)^{2}}}{ \sqrt{2^{3} g \frac{g^{2}}{g^{2}}} \, \left( y_{A} - y \right)^{\frac{3}{2}}}
\end{align}
```

$$\boxed{\frac{\partial F}{\partial y} = \frac{g \sqrt{1 + \left( y^{\prime} \right)^{2}}}{\left[ 2g \left( y_{A} - y \right) \right]^{\frac{3}{2}}}}$$

---

$$\frac{\partial F}{\partial y^{\prime}} = \ccancel{\red}{\frac{1}{2}} \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{-\frac{1}{2}} \cdot \ccancel{\red}{2} y^{\prime} \cdot \left[ 2 g \left( y_{A} - y \right) \right]^{-\frac{1}{2}}$$

$$\boxed{\frac{\partial F}{\partial y^{\prime}} = \frac{y^{\prime}}{\sqrt{2 g \left( y_{A} - y \right)} \cdot \sqrt{1 + \left( y^{\prime} \right)^{2}}}}$$

Die nächste Ableitung $\frac{\mathrm{d}}{\mathrm{d} x}$, die wir nun berechnen müssen, ist nun eine sehr aufwändige Ableitung. Es lohnt sich daher die Ableitung aufzuteilen und Schritt für Schritt zu berechnen. Dafür definieren wir

$$\frac{\mathrm{d}}{\mathrm{d} x} \left( \frac{\partial F}{\partial y^{\prime}} \right): \quad \frac{\partial F}{\partial y^{\prime}} = y^{\prime} \cdot A(x) \cdot B(x)$$

mit

$$A(x) = \left[ 2 g \left( y_{A} - y \right) \right]^{-\frac{1}{2}} \quad \text{und} \quad B(x) = \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{-\frac{1}{2}},$$

wobei $A \coloneqq A(x)$ und $B \coloneqq B(x)$.

Damit ergibt die Ableitung

$$\frac{\mathrm{d}}{\mathrm{d} x} \left( \frac{\partial F}{\partial y^{\prime}} \right) = \underbrace{y^{\prime \prime} A B}_{\text{Term 1}} + \underbrace{y^{\prime} A^{\prime} B}_{\text{Term 2}} + \underbrace{y^{\prime} A B^{\prime}}_{\text{Term 3}}$$

````{admonition} Nebenrechnung
:class: hint

```{math}
\frac{\mathrm{d}}{\mathrm{d} x} A &= \ccancel{\red}{- \frac{1}{2}} \left[ 2g \left( y_{A} - y \right) \right]^{-\frac{3}{2}} \cdot \ccancel{\red}{-2} g y^{\prime} \\
A^{\prime} &= g y^{\prime} \left[ 2g \left( y_{A} - y \right) \right]^{-\frac{3}{2}}
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
y^{\prime \prime} A B &= y^{\prime \prime} \cdot \left[ 2 g \left( y_{A} - y \right) \right]^{-\frac{1}{2}} \cdot \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{-\frac{1}{2}} \\
&= \frac{y^{\prime \prime}}{\sqrt{1 + \left( y^{\prime} \right)^{2}} \sqrt{2 g \left( y_{A} - y \right)}}
```

**Term 2**

```{math}
y^{\prime} A^{\prime} B &= y^{\prime} \cdot g y^{\prime} \left[ 2g \left( y_{A} - y \right) \right]^{-\frac{3}{2}} \cdot \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{-\frac{1}{2}} \\
&= \frac{g \left( y^{\prime} \right)^{2} }{\left[ 2g \left( y_{A} - y \right) \right]^{\frac{3}{2}} \sqrt{1 + \left( y^{\prime} \right)^{2}}}
```

**Term 3**

```{math}
y^{\prime} A B^{\prime} &= y^{\prime} \cdot \left[ 2 g \left( y_{A} - y \right) \right]^{-\frac{1}{2}} \cdot \left\{- y^{\prime} y^{\prime \prime} \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{-\frac{3}{2}} \right\} \\
&= - \frac{\left( y^{\prime} \right)^{2} y^{\prime \prime}}{\sqrt{2 g \left( y_{A} - y \right)} \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{\frac{3}{2}}}
```

Term 1 und 3 lassen sich vereinfachen:

```{math}
(\text{1}) + (\text{3}) &= \small{\frac{y^{\prime \prime}}{\sqrt{2 g \left( y_{A} - y \right)}} \left( \frac{1}{\sqrt{1 + \left( y^{\prime} \right)^{2}}} - \frac{\left( y^{\prime} \right)^{2}}{\left( 1 + \left( y^{\prime} \right)^{2} \right) \sqrt{1 + \left( y^{\prime} \right)^{2}}} \right)} \\
&= \small{\frac{y^{\prime \prime}}{\sqrt{2 g \left( y_{A} - y \right)}} \left( \frac{\left( 1 + \left( y^{\prime} \right)^{2} \right)}{\left( 1 + \left( y^{\prime} \right)^{2} \right) \sqrt{1 + \left( y^{\prime} \right)^{2}}} - \frac{\left( y^{\prime} \right)^{2}}{\left( 1 + \left( y^{\prime} \right)^{2} \right) \sqrt{1 + \left( y^{\prime} \right)^{2}}} \right)} \\
&= \small{\frac{y^{\prime \prime}}{\sqrt{2 g \left( y_{A} - y \right)}} \frac{1 \ccancel{\red}{+ \left( y^{\prime} \right)^{2} - \left( y^{\prime} \right)^{2}}}{\left( 1 + \left( y^{\prime} \right)^{2} \right) \sqrt{1 + \left( y^{\prime} \right)^{2}}}} \\
&= \small{\frac{y^{\prime \prime}}{\sqrt{2 g \left( y_{A} - y \right)} \left( 1 + \left( y^{\prime} \right)^{2} \right)^{\frac{3}{2}}}}
```

Womit der zweite Summant $\frac{\mathrm{d}}{\mathrm{d} x} \left( \frac{\partial F}{\partial y^{\prime}} \right)$ der Euler-Lagrange-Gleichung zu

$$\small{\frac{\mathrm{d}}{\mathrm{d} x} \left( \frac{\partial F}{\partial y^{\prime}} \right) = \frac{g \left( y^{\prime} \right)^{2} }{\left[ 2g \left( y_{A} - y \right) \right]^{\frac{3}{2}} \sqrt{2 g \left( y_{A} - y \right)}} + \frac{y^{\prime \prime}}{\sqrt{2 g \left( y_{A} - y \right)} \left( 1 + \left( y^{\prime} \right)^{2} \right)^{\frac{3}{2}}}}$$

wird. Wir können nun alles was wir bis dato berechnet haben in die Euler-Lagrange-Gleichung einsetzen.


$$\frac{\partial F}{\partial y} = \frac{\mathrm{d}}{\mathrm{d} x} \left( \frac{\partial F}{\partial y^{\prime}} \right)$$

$$\small{\frac{g \sqrt{1 + \left( y^{\prime} \right)^{2}}}{\left[ 2g \left( y_{A} - y \right) \right]^{\frac{3}{2}}} = \frac{g \left( y^{\prime} \right)^{2} }{\left[ 2g \left( y_{A} - y \right) \right]^{\frac{3}{2}} \sqrt{2 g \left( y_{A} - y \right)}} + \frac{y^{\prime \prime}}{\sqrt{2 g \left( y_{A} - y \right)} \left( 1 + \left( y^{\prime} \right)^{2} \right)^{\frac{3}{2}}}}$$

Um die DGL auf eine handhabbare Form zu bringen, wollen wir die Brüche auf einen gemeinsamen Nenner bringen. Hierfür multiplizieren wir beide Seiten mit

$$\sqrt{2g} \left( y_{A} - y \right)^{\frac{3}{2}} \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{\frac{3}{2}}.$$

Dadurch entsteht der folgende Ausdruck.

$$\small{\frac{g \sqrt{1 + \left( y^{\prime} \right)^{2}} \sqrt{2g} \left( y_{A} - y \right)^{\frac{3}{2}} \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{\frac{3}{2}}}{\left[ 2g \left( y_{A} - y \right) \right]^{\frac{3}{2}}}} = \small{\frac{g \left( y^{\prime} \right)^{2} \sqrt{2g} \left( y_{A} - y \right)^{\frac{3}{2}} \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{\frac{3}{2}}}{\left[ 2g \left( y_{A} - y \right) \right]^{\frac{3}{2}} \sqrt{2 g \left( y_{A} - y \right)}} + \frac{y^{\prime \prime} \sqrt{2g} \left( y_{A} - y \right)^{\frac{3}{2}} \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{\frac{3}{2}}}{\sqrt{2 g \left( y_{A} - y \right)} \left( 1 + \left( y^{\prime} \right)^{2} \right)^{\frac{3}{2}}}}$$

````{admonition} Kürzen
:class: hint

$$\small{\frac{\ccancel{\red}{g} \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{\frac{1}{2}} \ccancel{\purple}{\sqrt{2g}} \ccancel{\orange}{\left( y_{A} - y \right)^{\frac{3}{2}}} \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{\frac{3}{2}}}{\ccancel{\orange}{\left( y_{A} - y \right)^{\frac{3}{2}}} \ccancel{\purple}{\sqrt{2g}} \, 2 \ccancel{\red}{g}}} = $$

$$\small{\frac{\ccancel{\purple}{g} \left( y^{\prime} \right)^{2} \ccancel{\red}{\sqrt{2g}} \ccancel{\orange}{\left( y_{A} - y \right)^{\frac{3}{2}}} \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{\ccancel{\green}{\frac{3}{2}}}}{2 \ccancel{\purple}{g} \ccancel{\red}{\sqrt{2g}} \ccancel{\orange}{\left( y_{A} - y \right)^{\frac{3}{2}}} \ccancel{\green}{\left[ 1 + \left( y^{\prime} \right)^{2} \right]^{\frac{1}{2}}}} + \frac{y^{\prime \prime} \ccancel{\red}{\sqrt{2g}} \left( y_{A} - y \right)^{\ccancel{\orange}{\frac{3}{2}}} \ccancel{\purple}{\left[ 1 + \left( y^{\prime} \right)^{2} \right]^{\frac{3}{2}}}}{\ccancel{\red}{\sqrt{2g}} \ccancel{\orange}{\left( y_{A} - y \right)^{\frac{1}{2}}} \ccancel{\purple}{\left( 1 + \left( y^{\prime} \right)^{2} \right)^{\frac{3}{2}}}}}$$
````

$$\frac{1}{2} \left[ 1 + \left( y^{\prime} \right)^{2} \right]^{2} = \frac{1}{2} \left( y^{\prime} \right)^{2} \left[ 1 + \left( y^{\prime} \right)^{2} \right] + y^{\prime \prime} \left( y_{A} - y \right)$$

Im nächsten Schritt können wir nun noch $\frac{1}{2} \left[ 1 + \left( y^{\prime} \right)^{2} \right]$ auf die andere Seite bringen und ausklammern.

$$0 = y^{\prime \prime} \left( y_{A} - y \right) + \frac{1}{2} \left[ 1 + \left( y^{\prime} \right)^{2} \right] \left[ - \left( 1 + \ccancel{\red}{\left( y^{\prime} \right)^{2}} \right) + \ccancel{\red}{\left( y^{\prime} \right)^{2}} \right] \quad \vert \cdot \left( -2 \right)$$

$$\boxed{0 = - 2 y^{\prime \prime} \left( y_{A} - y \right) + \left( y^{\prime} \right)^{2} + 1}$$

Diese nichtlineare Differentialgleichung 2. Ordnung von $y(x)$ müssen wir im nächsten Abschnitt lösen, um die explizite Bahnform zu erhalten.

````{admonition} Warum verschwindet $g$ in der DGL?
:class: note

$g$ ist lediglich eine Skalierung der Zeit. Die Bahn selbst ist unabhängig von $g$.\
$\Rightarrow$ $g$ bestimmt, wie schnell wir die Bahn hinunter rutschen, hat aber selbst keinen Einfluss auf die optimale Bahn.
````

## Vereinfachen der DGL

Die DGL ist **autonom** (sie ist unabhängig von der Variable $x$). Das System "weiß" also nicht, an welchem $x$-Punkt es sich befindet.

$\Rightarrow$ Die Gleichung beschreibt also eine Beziehung zwischen der Höhe $y$, der Steigung $y^{\prime}$ und der Krümmung $y^{\prime \prime}$.

Wir wollen nun durch einen einfachen Trick die Ordnung der DGL von zwei auf eins reduzieren. Hierfür versuchen wir die Steigung $y^{\prime}$ als Funktion der Höhe $y$ darzustellen.

$$p \coloneqq p(y(x)) \coloneqq y^{\prime}$$

$$\Rightarrow y^{\prime \prime} = \frac{\mathrm{d}}{\mathrm{d} x} y^{\prime} = \frac{\mathrm{d}}{\mathrm{d} x} p(y(x)) \quad \underrightarrow{Kettenregel} \quad \frac{\mathrm{d}p}{\mathrm{d}y} \frac{\mathrm{d}y}{\mathrm{d}x} = p \frac{\mathrm{d}y}{\mathrm{d}x} \quad \text{mit} \quad p = y^{\prime} = \frac{\mathrm{d} y}{\mathrm{d} x}$$

Weil wir die zweite Ableitung $y^{\prime \prime}$ berechnen wollen, müssen wir $p$ nach $x$ ableiten. Da $p$ aber "offiziell" von $y$ abhängt, greift die Kettenregel.

$$y^{\prime \prime} = p \frac{\mathrm{d}p}{\mathrm{d}y}$$

Eingesetzt in die DGL wird diese zu

$$- 2 p \frac{\mathrm{d}p}{\mathrm{d}y} \, \left( y_{A} - y \right) + p^{2} + 1 = 0$$

Die Gleichung ist damit zwar nur noch eine DGL 1. Ordnung, aber weiterhin nichtlinear in $p$.\
Auffällig ist jedoch, dass $p$ nur in der Form $p^{2}$ und $p \frac{\mathrm{d}p}{\mathrm{d}y}$ vorkommt. Wobei gilt:

$$\frac{\mathrm{d}}{\mathrm{d} y} \left( p^{2} \right) = 2 p \frac{\mathrm{d} p}{\mathrm{d} y}$$

Es ist also naheliegend, die Substitution $w \coloneqq w(y) \coloneqq \left( p(y) \right)^{2}$ einzuführen.

$$\frac{\mathrm{d} w}{\mathrm{d} y} = 2 p \frac{\mathrm{d} p}{\mathrm{d} y} \quad \Rightarrow \quad p \frac{\mathrm{d} p}{\mathrm{d} y} = \frac{1}{2} \frac{\mathrm{d} w}{\mathrm{d} y}$$

Mit dieser Substitution schreiben wir unsere DGL nun in der Form:

$$0 = - \ccancel{\red}{2 \cdot \frac{1}{2}} \frac{\mathrm{d} w}{\mathrm{d} y} \left( y_{A} - y \right) + w + 1$$

oder Umgestellt

$$\frac{\mathrm{d} w}{\mathrm{d} y} - \frac{1}{y_{A} - y} w = \frac{1}{y_{A} - y} \quad \text{oder} \quad \boxed{\frac{\mathrm{d} w}{\mathrm{d} y} = \frac{1 + w}{y_{A} - y}}.$$

Und damit wurde aus einer nichtlinearen DGL 2. Ordnung eine lineare DGL 1. Ordnung.

## Lösen der DGL

Diese DGL können wir mit der bekannten Methode "Trennung der Variablen" lösen:

```{math}
\frac{\mathrm{d} w}{1 + w} &= \frac{\mathrm{d} y}{y_{A} - y} \\
\int \frac{1}{1 + w} \, \mathrm{d} w &= \int \frac{1}{y_{A} - y} \, \mathrm{d} y \\
\ln \left( 1 + w \right) &= - \ln \left( y_{A} - y \right) + \ln \left( C \right), \quad \text{mit } \, C > 0 \\
1 + w &= \frac{C}{y_{A} - y} \\
w &= \frac{C}{y_{A} - y} - 1, \quad \text{mit } \, w = p^{2} = \left( \frac{\mathrm{d} y}{\mathrm{d} x} \right)^{2} \\
\left( \frac{\mathrm{d} y}{\mathrm{d} x} \right)^{2} &= \frac{C - \left( y_{A} - y \right)}{y_{A} - y}
```

Wenn wir nun mit $u \coloneqq y_{A} - y$ substituieren, also der Falltiefe, mit $u > 0$, dann ist $y = y_{A} - u$ und 

$$\frac{\mathrm{d} y}{\mathrm{d} x} = \frac{\mathrm{d}}{\mathrm{d} x} \left( y_{A} - u(x) \right) = - \frac{\mathrm{d} u}{\mathrm{d} x}$$

Damit schreiben wir nun:

$$\left( - \frac{\mathrm{d} u}{\mathrm{d} x} \right)^{2} = \frac{C - u}{u}$$

Und wieder können wir diese Gleichung durch die Trennung der Variablen lösen.

$$- \frac{\mathrm{d} u}{\mathrm{d} x} = \pm \sqrt{\frac{C - u}{u}}$$

Wir können je nach Orientierung die positive oder negative Wurzel wählen.

An dieser Stelle lohnt es sich, kurz inne zu halten und sich die Wahl des Vorzeichens zu überlegen. Wir haben $u$ so definiert, dass dadurch die Falltiefe repräsentiert wird. Wir erwarten, dass $u$ mit zunehmendem $x$ auch wächst (je weiter wir nach rechts rutschen, desto weiter unten sind wir). Dadurch muss für die Steigung $\frac{\mathrm{d} u}{\mathrm{d} x} > 0$ gelten. Deshalb wählen wir die negative Wurzel und können so auf beiden Seiten das Minus kürzen.

```{math}
\ccancel{\red}{-} \frac{\mathrm{d} u}{\mathrm{d} x} &= \ccancel{\red}{-} \sqrt{\frac{C - u}{u}} \\
\mathrm{d} x &= \sqrt{\frac{u}{C - u}} \, \mathrm{d} u
```

An diesem Punkt angelangt, greifen wir zu einer trigonometrischen Substitution, um zwei zentrale Hürden der Integration zu überwinden: Erstens soll die rechnerisch unhandliche Wurzel eliminiert werden, und zweitens gilt es, die Singularitäten an den Intervallgrenzen zu umgehen.\
Die Struktur des Terms $\sqrt{u/ \left( C−u \right)}$​ legt nahe, eine Substitution zu wählen, die den Radikanden (den Ausdruck unter der Wurzel) in ein vollständiges Quadrat überführt. Hierfür bietet sich die Definition

$$u \coloneqq C \sin^{2} \left( \frac{\theta}{2} \right),$$

an. Über die Halbwinkelformeln lässt sich dieser Ausdruck auch linearisiert als

$$u = C \sin^{2} \left( \frac{\theta}{2} \right) = \frac{C}{2} \left( 1 - \cos \left( \theta \right) \right)$$

darstellen. Der entscheidende Vorteil dieser Wahl zeigt sich im Nenner der Wurzel:

$$C - u = C - C \sin^{2} \left( \frac{\theta}{2} \right) = C \left( 1 - \sin^{2} \left( \frac{\theta}{2} \right) \right) = C \cos^{2} \left( \frac{\theta}{2} \right).$$

Setzt man dies in den Wurzelterm ein, so vereinfacht sich dieser durch den trigonometrischen Pythagoras zu einer elementaren Tangensfunktion:

$$\sqrt{\frac{u}{C - u}} = \sqrt{\frac{\ccancel{\red}{C} \sin^{2} \left( \frac{\theta}{2} \right)}{\ccancel{\red}{C} \cos^{2} \left( \frac{\theta}{2} \right)}} = \frac{\sin \left( \frac{\theta}{2} \right)}{\cos \left( \frac{\theta}{2} \right)}$$

Um die Integration nach der neuen Variable $\theta$ durchzuführen, bestimmen wir zudem das zugehörige Differential $\mathrm{d} u$:

```{math}
\frac{\mathrm{d} u}{\mathrm{d} \theta} &= \frac{\mathrm{d}}{\mathrm{d} \theta} \left\{ \frac{C}{2} \left( 1 - \cos \left( \theta \right) \right) \right\} = 0 + \frac{C}{2} \sin \left( \theta \right) \\
\Leftrightarrow \quad \mathrm{d} u &= \frac{C}{2} \sin \left( \theta \right) \, \mathrm{d} \theta
```

Damit haben wir alle Komponenten vorbereitet, um die ursprüngliche Gleichung

$$\mathrm{d} x = \sqrt{\frac{u}{C - u}} \, \mathrm{d} u,$$

in eine direkt integrierbare Form überführen zu können.

$$\mathrm{d} x = \frac{\sin \left( \frac{\theta}{2} \right)}{\cos \left( \frac{\theta}{2} \right)} \cdot \frac{C}{2} \sin \left( \theta \right) \, \mathrm{d} \theta$$

Unter berücksichtigung der Identität

$$\sin \left( x \right) = 2 \sin \left( \frac{x}{2} \right) \cos \left( \frac{x}{2} \right)$$

vereinfacht sich die Differentialgleichung zu

$$\mathrm{d} x = \frac{\sin \left( \frac{\theta}{2} \right)}{\ccancel{\purple}{\cos \left( \frac{\theta}{2} \right)}} \cdot \frac{C}{\ccancel{\red}{2}} \ccancel{\red}{2} \sin \left( \frac{\theta}{2} \right) \ccancel{\purple}{\cos \left( \frac{\theta}{2} \right)} \, \mathrm{d} \theta = C \sin^{2} \left( \frac{\theta}{2} \right) \, \mathrm{d} \theta = \frac{C}{2} \left( 1 - \cos \left( \theta \right) \right) \, \mathrm{d} \theta.$$

Durch Integration erhalten wir nun die $x$-Koordinate in Abhängigkeit des Parameters $\theta$ (also eine parametrisierte Kurve).

```{math}
\int \, \mathrm{d} x &= \int \frac{C}{2} \left( 1 - \cos \left( \theta \right) \right) \, \mathrm{d} \theta \\
x(\theta) - x_{0} &= \frac{C}{2} \left( \theta - \sin \left( \theta \right) \right)
```

$$\Rightarrow \quad x(\theta) = \frac{C}{2} \left( \theta - \sin \left( \theta \right) \right) + x_{0}$$

Aus den beiden Definitionen $y = y_{A} - u$ und $u = \frac{C}{2} \left( 1 - \cos \left( \theta \right) \right)$ ist es uns möglich, $y(\theta)$ zu bestimmen.

$$y(\theta) = y_{A} - \frac{C}{2} \left( 1 - \cos \left( \theta \right) \right)$$

Durch die Integration haben wir die Parameterdarstellung der Kurve erhalten. Setzt man zur Vereinfachung $R = \frac{C}{2}$, so lauten die Koordinaten:

```{math}
x(\theta) &= R \left( \theta - \sin \left( \theta \right) \right) + x_{0} \\
y(\theta) &= - R \left( 1 - \cos \left( \theta \right) \right) + y_{A} \quad \text{mit } \theta \in \left[ 0, \, \theta_{2} \right]
```

Bei dieser Lösung handelt es sich um die **Parameterform einer Zykloide**.\
Geometrisch lässt sich diese Kurve als die Bahn beschreiben, die ein Punkt auf dem Rand eines Kreises mit dem Radius $R$ beschreibt, während dieser auf einer Geraden abrollt.

```{figure} ../../_static/plots/analysis/variationsrechnung/notrutsche1/beispiel.png
:align: center
:width: 100%

Der Zykloide als Lösung der Brachistochrone
```

Damit bestätigt sich für unser Notrutschenproblems, dass die Kurve des schnellsten Abstiegs (die sogenannte Brachistochrone) kein gerader Weg ist. Stattdessen sorgt die anfänglich stärkere Neigung der Zykloide für eine maximale Beschleunigung, während der flachere Auslauf am Ende den Übergang in die Horizontale erleichtert. Die Konstante $C$ und der Endwinkel $\theta_{2}$​ müssten nun lediglich noch über die Randbedingungen (Start- und Zielpunkt) bestimmt werden.

```{note}
Wir beschreiben die Bahn über den Parameter $\theta$, statt explizit mit $y(x)$. Das ist hier eine besonders gute Wahl, da die Steigung am Start der Bahn sehr hoch ist, die Bahn parametrisch aber glatt bleibt.
```

## Lösung mit Randbedingungen

Wir wollen jetzt die Parametrisierung

```{math}
x(\theta) &= R \left( \theta - \sin \left( \theta \right) \right) + x_{0} \\
y(\theta) &= - R \left( 1 - \cos \left( \theta \right) \right) + y_{A}
```

mit $\theta \in \left[ 0, \, \theta_{2} \right]$ so wählen, dass die Kurve durch

$$A = \left( x_{A}, \, y_{A} \right) \quad \land \quad B = \left( x_{B}, \, y_{B} \right)$$

läuft. Zunächst müssen wir den Startpunkt für $\theta = 0$ treffen. Setzen wir $\theta = 0$, dann ist $\sin \left( 0 \right) = 0$ und $\cos \left( 0 \right) = 1$, also

$$x(0) = x_{0} \quad \land \quad y(0) = y_{0}.$$

Damit ist die einfachste Wahl:

$$\boxed{x_{0} = x_{A} \quad \land \quad y_{0} = y_{A}}$$

Mit dieser Wahl ist $A$ automatisch erfüllt. Fpr die Enpunkte setzen wir $\theta = \theta_{2}$ und verlangen

$$x(\theta) = x_{B} \quad \land \quad y(\theta) = y_{B}.$$

Wenn wir jetzt die Differenzen als

$$\Delta x = x_{B} - x_{A} \quad \land \quad \Delta y = y_{B} - y_{A}$$

definieren, dann folgt:

$$\boxed{\Delta x = R \left( \theta_{2} - \sin \left( \theta_{2} \right) \right)} \quad \land \quad \boxed{\Delta y = - R \left( 1 - \cos \left( \theta_{2} \right) \right)}$$

Da unsere $\Delta y$ für wachsende $\theta$ zunehmend negativer wird $\left( \Delta y(\theta) < 0 \right)$ $\Rightarrow$ Zielpunkt liegt tiefer als Startpunkt. Setzen wir

$$L \coloneqq x_{B} - x_{A} = \Delta x \quad \land \quad \Delta H \coloneqq y_{A} - y_{B} = - \Delta y > 0.$$

Durch die Definition $H \coloneqq y_{A} - y_{B}$ (mit $y_{A} > y_{B}$) transformieren wir das Koordinatensystem in eine rein geometrische Betrachtung der Höhendifferenz. Damit entfällt das negative Vorzeichen aus der ursprünglichen Parametrisierung, und wir arbeiten mit rein positiven Beträgen für die geometrischen Abmessungen der Notrutsche.

Damit werden unsere Gleichungen besonders sauber:

```{math}
L &= R \left( \theta_{2} - \sin \left( \theta_{2} \right) \right) \\
H &= R \left( 1 - \cos \left( \theta_{2} \right) \right)
```

An dieser Stelle stehen wir vor einem System aus zwei Gleichungen für die Unbekannten $R$ (Radius des Rollkreises) und $\theta_{2}$​ (Endwinkel). Da $\theta_{2}$​ sowohl linear als auch innerhalb einer Winkelfunktion auftritt, handelt es sich um **transzendente Gleichungen**. Diese lassen sich nicht geschlossen nach den Unbekannten auflösen.

**Der Trick:**\
Um $R$ und $\theta_{2}$​ zu bestimmen, bildet man sinnvollerweise das Verhältnis aus Länge und Höhe:

$$\frac{L}{H} = \frac{\ccancel{\red}{R} \left( \theta_{2} - \sin \left( \theta_{2} \right) \right)}{\ccancel{\red}{R} \left( 1 - \cos \left( \theta_{2} \right) \right)} = \frac{\theta_{2} - \sin \left( \theta_{2} \right)}{1 - \cos \left( \theta_{2} \right)}$$

Diese Gleichung hängt nur noch von der Unbekannten $\theta_{2}$​ ab und ist die zentrale Gleichung für $\theta_{2}$.

$$\boxed{f(\theta) \coloneqq \frac{\theta - \sin \left( \theta \right)}{1 - \cos \left( \theta \right)} - \frac{L}{H} = 0}$$

Sobald $\theta_{2}$​ (beispielsweise numerisch) bestimmt wurde, ergibt sich der Radius trivial aus

$$\boxed{R = \frac{H}{1 - \cos \left( \theta_{2} \right)} = \frac{L}{\theta_{2} - \sin \left( \theta_{2} \right)}}$$

Damit haben wir die Brachistochrone erfolgreich auf zwei Bestimmungsgleichungen reduziert, die die Geometrie der Rutsche ($L$ und $H$) mit den Parametern der Zykloide ($R$ und $\theta_{2}$​) verknüpfen.

Interessant ist hierbei, dass das Verhältnis von Fallhöhe zu horizontaler Distanz den Endwinkel $\theta_{2}$​ eindeutig festlegt. Dies bedeutet, dass die "Form" der optimalen Rutsche allein durch das Verhältnis der Endpunkte zueinander bestimmt wird, während der Radius $R$ lediglich als Skalierungsfaktor fungiert.