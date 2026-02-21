# Aufgaben

Die folgenden Aufgaben vertiefen die Variationsrechnung als **Modellierungswerkzeug**.\
Aus einer klar formulierten Zielfunktion (*Weglänge*, *Laufzeit*, *Fläche*) wird über **Stationarität** eine mathematische Bedingung gewonnen, aus der sich die gesuchte Kurve oder der optimale Punkt ergibt. Der Schwerpunkt liegt dabei bewusst auf Methoden, die unmittelbar auf die **Lagrange-Mechanik** vorbereiten, ohne deren physikalische Begriffe (Kräfte, Impulse) bereits vorauszusetzen.

Die Aufgaben sind so gewählt, dass sie an **reale Phänomene** (*Atmosphäre*, *Navigation*, *Reflexion*, *Ressourcenbegrenzung*, *Simulation*) anknüpfen und zugleich das methodische Repertoire systematisch erweitern. Wir wollen nach diesem Übungsteil Variationsprobleme selbstständig aufstellen, lösen und physikalisch deuten können.\
Damit haben wir die Grundlagen geschaffen, um das Wirkungsprinzip der Lagrange-Mechanik als vertraute Verallgemeinerung wiederzuerkennen.

## 1. Gewichtete Weglänge in der Atmosphäre

```{rubric} Fermat-Prinzip im Gradientenindex $n(y)$ (Inversionswetterlage)
```

In einer geschichteten Atmosphäre sei der Brechungsindex nur höhenabhängig, $n = n(y)$.\
Eine Schallwelle verbindet zwei feste Punkte $A = \left( x_{A},\, y_{A} \right)$ und $B = \left( x_{B},\, y_{B} \right)$ in der $x$-$y$-Ebene. Wobei gilt $y_{A} = y_{B} = 0$ und $x_{A} = 0$.\
Wir beschreiben die Strahlbahn als Graph $y(x)$ mit $x \in \left[ x_{A},\, x_{B} \right]$.\
Nach dem Fermat-Prinzip ist die realisierte Bahn stationär bezüglich der optischen Weglänge

$$\mathcal{L} = \int n\, \mathrm{d}s$$

```{figure} ../../_static/img/analysis/variationsrechnung/inversionswetterlage.jpg
:align: center
:width: 70%

Aufgabenskizze - Gewichtete Weglänge in der Atmosphäre
```

**a) Modellierung und Funktional**

1. Begründe kurz, warum man die Strahlbahn als Funktion $y(x)$ modellieren darf (welche geometrische Annahme steckt dahinter?).

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

2. Leite aus dem Linienelement $\mathrm{d}s$ in kartesischen Koordinaten her, dass

$$\mathrm{d}s = \sqrt{1 + y^{\prime}(x)^{2}}$$

gilt, und formuliere daraus $\mathcal{L}[y]$ als Integral über $x$.

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

***Hinweis:*** *Es reicht nicht, die Formel nur hinzuschreiben. Zeige den Übergang von $\left( \mathrm{d}x, \mathrm{d}y \right)$ zu $\mathrm{d}s$ sauber*

**b) Euler–Lagrange-Gleichung**

Betrachte

$$\mathcal{L}[y] = \int_{x_{A}}^{x_{B}} L (y,\, y^{\prime})\, \mathrm{d}x, \quad L (y,\, y^{\prime}) = n(y) \sqrt{1 + y^{\prime 2}}$$

Stelle die Euler–Lagrange-Gleichung

$$\frac{\partial L}{\partial y} - \frac{\mathrm{d}}{\mathrm{d} x} \left( \frac{\partial L}{\partial y^{\prime}} \right) = 0$$

für dieses konkrete $L (y,\, y^{\prime})$ **vollständig** auf (alle Ableitungen explizit ausrechnen und einsetzen).

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

**c) Eine konstante Größe**

Zeige aus der Gleichung aus (b), dass entlang einer Extremale die Größe

$$n(y) \frac{1}{\sqrt{1 + y^{\prime 2}}}$$

konstant ist.

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

***Hinweis:*** *Multipliziere die Euler–Lagrange-Gleichung aus (b) mit $y^{\prime}(x)$ und forme so um, dass die linke Seite als totale Ableitung $\frac{\mathrm{d}}{\mathrm{d}x} \left( \dots \right)$ geschrieben werden kann.*

**d) Winkelinterpretation und qualitative Physik (Inversion)**

Definiere den lokalen Winkel $\theta (x)$ zwischen Strahlrichtung und der $y$-Achse (Normalenrichtung zur Schichtung). Zeige den Zusammenhang zwischen $y^{\prime} (x)$ und $\theta (x)$ und interpretiere das Ergebnis aus (c) als Beziehung der Form

$$n(y) \cos \left( \theta \right) = \text{konstant} \quad \left( \text{oder äquivalent} \right)$$

Diskutiere anschließend qualitativ: Was passiert mit der Strahlrichtung, wenn $n(y)$ mit der Höhe zunimmt bzw. abnimmt (typisch bei Inversionslagen)?

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

## 2. Kürzester Weg zur Küstenlinie

```{rubric} Variationsproblem mit freiem Endpunkt auf $\Gamma$ (Anlandepunkt frei wählbar)
```

Ein Boot befindet sich im Punkt $A = \left (x_{A},\, y_{A} \right)$ im Meer. Die Küstenlinie sei eine glatte Kurve $\Gamma$ in der Ebene.\
Das Boot soll einen Punkt $P \in \Gamma$ ansteuern, um dort anzulanden.\
**Welcher Anlandepunkt** $P$ wird gewählt, wenn das Boot die **zurückzulegende Strecke minimieren** soll?

```{figure} ../../_static/img/analysis/variationsrechnung/kuestenlinie.jpg
:align: center
:width: 70%

Aufgabenskizze - Kürzester Weg zur Küstenlinie
```

Wir modellieren die Fahrtroute als glatte Kurve $\mathbf{r}(t) = \left( x(t),\, y(t) \right)$ mit $t \in \left[ 0, 1 \right]$, Startbedingung $\mathbf{r}(0) = A$ und Endpunktbedingung $\mathbf{r}(1) = P \in \Gamma$ (der Endpunkt ist also nicht fest, sondern darf auf $\Gamma$ variieren).

**a) Modellierung als Variationsproblem**

Formuliere die zu minimierende Weglänge als Funktional

$$S[\mathbf{r}] = \int_{t=0}^{1} \left\lVert \mathbf{r}^{\prime}(t) \right\rVert\, \mathrm{d}t.$$

Erläutere kurz, warum dieses Funktional unabhängig von der konkreten Parametrisierung der Kurve ist (solange $\mathbf{r}$ regulär ist).

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

**b) Extremalen im Inneren**

Zeige: Jede Extremale der Weglänge im freien Bereich (also fern der Küstenlinie) ist eine **Gerade**.

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

***Hinweis:*** *wähle eine geeignete Parametrisierung, z. B. $x$ als Parameter und $y=y(x)$, oder argumentiere geometrisch über "kürzeste Verbindung".*

**c) Freier Endpunkt auf $\Gamma$: Bedingung am Anlandepunkt**

Sei $\mathbf{t}$ der Tangentialvektor an die Küstenlinie $\Gamma$ im Anlandepunkt $P$. Leite eine notwendige Bedingung her, die am optimalen Anlandepunkt gelten muss, wenn der Endpunkt auf $\Gamma$ frei verschiebbar ist.

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

***Hinweis:*** *Eine kleine Variation des Endpunkts entlang der Kurve kann als Verschiebung $\delta \mathbf{r}(1)$ in Tangentialrichtung $\mathbf{t}$ aufgefast werden. Überlege, welchen Term die Variation $\delta S$ dadurch erhält.*

**d) Geometrische Interpretation**

Interpretiere das Ergebnis aus (c) geometrisch. In welchem Winkel trifft die optimale Fahrtroute die Küstenlinie?

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

**e) Konkretes Beispiel (Rechnen + Skizzieren)**

Betrachte als Küstenlinie die Gerade

$$\Gamma: \quad y = 0$$

und den Startpunkt $A = \left(0,\, a \right)$ mit $a>0$.

1. Bestimme den optimalen Anlandepunkt $P = \left( p,\, 0 \right)$ und die minimale Strecke.

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

2. Überprüfe, dass die Bedingung aus (c) und (d) erfüllt ist.

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

3. Skizziere die Situation (Koordinatensystem, $A$, $\Gamma$, $P$).

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

**f) Zielgebiet statt Zielkurve**

Wie ändert sich die Bedingung aus (c), wenn das Boot nicht auf einer Kurve $\Gamma$, sondern irgendwo in einem Gebiet $\Omega$ (z. B. einer Küstenzone) ankommen darf?

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

## 3. Reflexion als Variationsproblem

```{rubric} Variationsprinzip mit Knickbedingung (optimaler Bandenpunkt)
```

Ein idealer Billardtisch werde in der Ebene modelliert. Eine Bande wird durch eine Gerade $\Gamma$ beschrieben (spiegelnde Reflexion ohne Energieverlust).\
Eine Kugel startet in $A$ und soll nach genau **einem** Bandenkontakt in $B$ ankommen. Der Bandenkontaktpunkt $P$ ist frei wählbar auf $\Gamma$.\
Gesucht ist der "optimale" Bandenkontakt im Sinne einer stationären Weglänge.

```{figure} ../../_static/img/analysis/variationsrechnung/reflexion.jpg
:align: center
:width: 70%

Aufgabenskizze - Reflexion als Variationsproblem
```

Zur Vereinfachung sei die Bande die $x$-Achse

$$\Gamma: \quad y = 0,$$

und die Punkte $A = \left (x_{A},\, y_{A} \right)$, $B = \left (x_{B},\, y_{B} \right)$ liegen im Halbraum $y>0$.

**a) Reduktion auf ein Ein-Parameter-Problem**

Parametrisiere den Bandenkontaktpunkt durch

$$P = \left (x,\, 0 \right), \quad x \in \mathbb{R}.$$

Stelle die gesamte Weglänge

$$S(x) = \left\lvert AP \right\rvert + \left\lvert PB \right\rvert$$

als explizite Funktion von $x$ dar.

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

**b) Stationarität am Bandenkontaktpunkt**

Leite die notwendige Bedingung für einen stationären Weg durch die Foderung $S^{\prime}(x) = 0$ her. Forme die resultierende Bedingung so um, dass sie sich geometrisch interpretieren lässt.

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

***Hinweis:*** *Es ist hilfreich, Terme der Form $\frac{a - x_{A}}{\left\lvert AP \right\rvert}$ bzw. $\frac{a - x_{B}}{\left\lvert PB \right\rvert}$ als Projektionen von Einheitsrichtungsvektoren zu erkennen.*

**c) Reflexionsgesetz als Konsequenz der Stationarität**

Definiere den Einfallswinkel $\theta_{\mathrm{e}}$ und den Ausfallswinkel $\theta_{\mathrm{a}}$ jeweils als Winkel zwischen dem Bewegungssegment und der Normalen an die Bande (also zur $y$-Achse). Zeige, dass die Stationaritätsbedingung aus (b) äquivalent zum Reflexionsgesetz ist.

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

**d) Bildmethode (Spiegelpunkt)**

Konstruiere den Spiegelpunkt $B^{\prime}$ von $B$ an der Bande $\Gamma$. Zeige, dass der optimale Bandenkontaktpunkt $P$ genau der Schnittpunkt der Geraden $AB^{\prime}$ mit $\Gamma$ ist. Interpretiere daraus erneut das Reflexionsgesetz.

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

**e) Konkretes Zahlenbeispiel**

Wähle $A = \left(0,\, 2 \right)$, $B = \left(6,\, 1 \right)$.

1. Bestimme den optimalen Bandenkontaktpunkt $P = \left (x^{*},\, 0 \right)$ analytisch.

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

2. Berechne die minimale Weglänge $S(x^{*})$

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

3. Überprüfe anhand einer Skizze oder kurzer Rechnung, dass Einfalls- und Ausfallswinkel gleich sind.

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

## 4. Maximale Weidefläche

```{rubric} Variationsproblem mit Nebenbedingung (feste Zaunlänge)
```

Ein gerader Fluss verläuft entlang der $x$-Achse. Eine Weidefläche soll **auf einer Seite des Flusses** eingezäunt werden. Der Fluss selbst bildet eine natürliche Grenze und muss **nicht** eingezäunt werden. Die beiden Zaunenden liegen fest bei

$$A = \left( 0,\, 0 \right), \quad B = \left( L,\, 0 \right), \quad \left( L>0 \right).$$

```{figure} ../../_static/img/analysis/variationsrechnung/weideflaeche.jpg
:align: center
:width: 70%

Aufgabenskizze - Maximale Weidefläche
```

Der Zaun bildet eine glatte Kurve $y(x) \geq 0$ für $x \in \left[ 0,\, L \right]$, die $A$ und $B$ verbindet. Die verfügbare Zaunlänge sei fest vorgegeben:

$$S[y] = \int_{0}^{L} \sqrt{1 + y^{\prime}(x)^{2}}\, \mathrm{d}x = S_{0}$$

Gesucht ist die Kurve $y(x)$, die die **eingeschlossene Fläche**

$$A[y] = \int_{0}^{L} y(x)\, \mathrm{d}x$$

maximiert.

**a) Problemformulierung**

1. Begründe kurz, warum $A[y]$ den Flächeninhalt zwischen Zaun und Fluss beschreibt.

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

2. Erkläre, warum die Bedingung $S[y] = S_{0}$ eine Nebenbedingung im Sinne der Variationsrechnung ist.

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

**b) Variationsansatz mit Multiplikator**

Formuliere ein neues Funktional

$$J[y] = A[y] - \lambda \left( S[y] - S_{0} \right)$$

mit einem (zunächst unbekannten) konstanten Multiplikator $\lambda$, sodass Extremale von $J[y]$ genau Kandidaten für das ursprüngliche Problem liefern.\
Schreibe $J[y]$ als Integral der Form

$$J[y] = \int_{0}^{L} F(y,\, y^{\prime})\, \mathrm{d}x + \mathrm{Konst.}$$

und gib $F(y,\, y^{\prime})$ explizit an.

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

**c) Euler–Lagrange-Gleichung und Form der Lösung**

1. Stelle die Euler–Lagrange-Gleichung zu $F(y,\, y^{\prime})$ auf und vereinfache sie so weit wie möglich.

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

2. Zeige, dass die Extremalen Kreisbögen sind (verwende an einer passenden Stelle eine trigonometrische Substitution oder leite eine geometrisch äquivalente Form her).

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

***Hinweis:*** *Es genügt zunächst zu zeigen, dass die Krümmung konstant ist.*

**d) Randbedingungen und Geometrie**

Die Endpunkte sind fest: $y(0) = 0$ und $y(L) = 0$.

1. Bestimme daraus die Lage des Kreisbogens\
(z. B. Mittelpunkt und Radius in Abhängigkeit von $\lambda$).

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

2. Beschreibe, welchen Teil eines Kreises der Zaun darstellt\
(z. B. "Kreisbogen oberhalb der $x$-Achse").

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

**e) Bestimmung des Multiplikators aus der Zaunlänge**

Nutze die Bedingung $S[y] = S_{0}$ um $\lambda$ (oder den Radius $R$) zu bestimmen.\
Gib die maximale Fläche $A_{\max}$ als Funktion von $L$ und $S_0$ an.

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

**f) Spezialfall "Halbkreis"**

Unter welcher Beziehung zwischen $S_{0}$ und $L$ ergibt sich als Lösung genau ein Halbkreis?

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

## 5. Numerische Strahloptik

```{rubric} diskretisiertes Fermat-Prinzip und Minimierung (Ray-Tracing im Brechungsindexfeld)
```

In einer geschichteten Atmosphäre sei der Brechungsindex höhenabhängig, $n = n(y)$.\
Eine Schallwelle soll zwei Punkte $A = \left( x_{A},\, y_{A} \right)$ und $B = \left( x_{B},\, y_{B} \right)$ verbinden.\
Statt die Strahlbahn $y(x)$ kontinuierlich zu bestimmen, soll sie **numerisch** über eine Diskretisierung als Optimierungsproblem berechnet werden ("Ray-Tracing aus Fermat").

```{figure} ../../_static/img/analysis/variationsrechnung/inversionswetterlage.jpg
:align: center
:width: 70%

Aufgabenskizze - Gewichtete Weglänge in der Atmosphäre
```

Wir betrachten ein gleichmäßig unterteiltes Intervall $\left[ x_{A},\, x_{B} \right]$ mit

$$x_{i} = x_{A} + i \Delta x, \quad i = 0, \dots, N, \quad \Delta x = \frac{x_{B} - x_{A}}{N},$$

und beschreiben die Strahlbahn durch die Stützwerte

$$y_{i} \approx y(x_{i}), \quad y_{0} = y_{A}, \quad y_{N} = y_{B},$$

wobei nur $y_{1}, \dots, y_[N-1]$ unbekannt sind.

**a) Diskretes optisches Weglängen-Funktional**

Leite eine sinnvolle diskrete Näherung $\mathcal{L}_{d}$ der optischen Weglänge $\mathcal{L}=\int n\, \mathrm{d} s$ durch das Approximieren der Bahn zwischen den Stützstellen als Polydonzug her.

Arbeite mit dem Ansatz:

- Segmentlänge

$$\Delta s_{i} = \sqrt{ \left( \Delta x \right)^{2} + \left( y_{i+1} - y_{i} \right)^{2}},$$

- Brechungsindex auf dem Segment als Mittelwert

$$n_{i} = n \left( \frac{y_{i} + y_{i+1}}{2} \right).$$

Formuliere damit $\mathcal{L}_{d} \left( y_{1},\dots, y_{N-1} \right)$ explizit als Summe.

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

**b) Stationaritätsbedingungen (diskrete Euler–Lagrange-Gleichungen)**

Leite die Bedingungen für ein Extremum her:

$$\frac{\partial \mathcal{L}_{d}}{\partial y_{k}}=0,\qquad k=1,\dots,N-1.$$

1. Bestimme $\frac{\partial \mathcal{L}_{d}}{\partial y_{k}}$ explizit

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

***Hinwei:*** *Achte darauf, dass $y_{k}$ nur in zwei Summanden vorkommt: Segment $k-1$ und Segment $k$.*

2. Gib die resultierende Gleichung für jedes $k$ in einer möglichst kompakten Form an.

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

***Hinweis:*** *Es lohnt sich, erst $\frac{\partial \Delta s_{i}}{\partial y_{k}}$ und $\frac{\partial n_{i}}{\partial y_{k}}$ separat zu berechnen.*

**c) Numerische Minimierung (Algorithmusidee)**

Beschreibe ein Verfahren, mit dem die Gleichungen aus (b) numerisch lösbar wären.

- Wähle entweder Gradientenverfahren (iteratives Update der $y_{k}$) oder ein Newton-Verfahren (linearisiere um einen aktuellen Schätzwert).
- Formuliere einen sinnvollen Startwert (z. B. Gerade zwischen $A$ und $B$).
- Diskutiere kurz, wann Konvergenz zu erwarten ist und welche Probleme auftreten können (z. B. zu großes Schrittmaß, schlechte Initialisierung).

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

**d) Konkretes Testmodell und qualitative Interpretation**

Verwende als Beispiel (Atmosphäre/Schichtung)

$$n(y) = n_{0} \left( 1 + \alpha y \right), \qquad \lvert \alpha y \rvert \ll 1.$$

1. Entscheide ohne Rechnung, ob qualitativ eine nach oben oder nach unten gekrümmte Strahlbahn für $\alpha > 0$ bzw. $\alpha < 0$ zu erwarten ist.\
Begründe das mit Fermat "Strahl läuft lieber dort, wo es optisch günstiger ist".

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

2. Skizziere (schematisch) den erwarteten Unterschied der numerischen Lösung gegenüber der Geraden $AB$.

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```

**e) Vergleich "diskret" vs. "kontinuierlich"**

Erkläre kurz, warum die diskreten Stationaritätsbedingungen aus (b) im Grenzfall $N \rightarrow \infty$ zur kontinuierlichen Euler–Lagrange-Gleichung aus Aufgabe 1 führen (inhaltlich, keine vollständige Grenzwertrechnung nötig).

```{dropdown} Lösung
:icon: check-circle

Lösung folgt...
```