# Aufgaben

## Kinematik in einer Dimension

### ICE-Fahrt zwischen München und Ingolstadt

In einer idealen Welt würde ein ICE den Hauptbahnhof München Richtung Ingolstadt HBF mit einer Beschleunigung von $0,4\,\mathrm{m/s}^2$ verlassen und für $162,5\,\mathrm{s}$ beschleunigen. Anschließend können die Passagiere die Reise bei der erreichten Geschwindigkeit für $17,22\,\mathrm{min}$ genießen. Nach einer Verzögerung von $-0,25\,\mathrm{m/s}^2$ kommt der Zug sanft in Ingolstadt zum stehen.

*Luftwiderstand, Reibung, Geschwindigkeitsbegrenzungen, Signale sowie andere Züge werden vernachlässigt. Die Bewegung wird als eindimensional betrachtet.*

a) Berechne für jede der drei Bewegungsphasen die Zeitdauer, die Beschleunigung und die zurückgelegte Strecke. Gib zusätzlich die maximale Reisegeschwindigkeit des Zuges an.

b) Zeichne das Beschleunigungs-Zeit-Diagramm, das Geschwindigkeits-Zeit-Diagramm und das Weg-Zeit-Diagramm für die gesamte Fahrt.

c) Wie weit liegen München HBF und Ingolstadt HBF auseinander? Wie lange wäre ein ICE in einer idealen Welt ohne Güterzüge und fehlende Überholmöglichkeit unterwegs?

### Paintball-Roulette

In einer Paintball-Anlage steht eine Gruppe von Personen dicht beisammen. Eine Person schießt einen Paintball senkrecht nach oben. 

Der Paintball verlässt den Lauf zum Zeitpunkt $t=0$ aus einer Höhe $y_{0}$ über dem Boden. Nach $t_\mathrm{T} = 6,0\,\mathrm{s}$
wird eine Person in derselben Gruppe von diesem Paintball getroffen, auf derselben Höhe $y_{0}$ (d. h. der Ball kommt nach $6\,\mathrm{s}$ wieder auf die Abschusshöhe zurück). Die Erdbeschleunigung sei konstant $g = 9,81\,\mathrm{m/s^2}$.

*Luftwiderstand und Reibung werden vernachlässigt. Der Paintball wird als Punktmasse betrachtet.*

a) Mit welcher Geschwindigkeit $v_{0}$ hat der Paintball den Lauf verlassen?

b) Welche maximale Höhe $y_{\text{max}}$ (über der Abschusshöhe) erreicht der Paintball?

c) Wie groß ist die Geschwindigkeit beim Auftreffen nach $6\,\mathrm{s}$ (Betrag und Richtung)?

d) Was ändert sich qualitativ mit Luftwiderstand?

### Zwei Steine von einer Brücke

Zwei Personen stehen auf einer Brücke in der Höhe $H$ über dem Boden. Die vertikale Koordinate $y$ sei nach unten positiv, der Ursprung befinde sich am Brückenrand ($y=0$).

Die Erdbeschleunigung sei konstant und betrage $g = 9,81\,\mathrm{m/s^2}$.

Zum Zeitpunkt $t=0\,\mathrm{s}$ lässt Person A einen Stein ohne Anfangsgeschwindigkeit fallen.
Nach einer Zeit $t_0>0\,\mathrm{s}$ wirft Person B einen zweiten Stein senkrecht nach unten mit Anfangsgeschwindigkeit $v_{0}$.

*Der Luftwiderstand wird in den Teilaufgaben a) und b) vernachlässigt.*

a) Stelle eine Gleichung auf, mit der der Zeitpunkt $t_{\text{ein}}>t_0$ bestimmt werden kann, zu dem der zweite Stein den ersten einholt. Eine explizite Lösung ist nicht erforderlich.

>Hinweis: *Einholen bedeutet, dass beide Steine zum selben Zeitpunkt dieselbe Ortskoordinate besitzen.*

b) Stelle eine Gleichung auf, mit der sich die Anfangsgeschwindigkeit $v_{0}$ bestimmen lässt, sodass der zweite Stein den ersten Stein zu einem Zeitpunkt $t>t_0$ einholt.

c) In der Realität wirkt auf beide Steine Luftwiderstand. Diskutiere qualitativ, ob der zweite Stein den ersten immer wie in a) und b) beschrieben einholen kann, wenn der Luftwiderstand berücksichtigt wird.\
Gehe dabei insbesondere auf den Begriff der **terminalen Geschwindigkeit** ein.

## Kinematik auf der Kreisbahn 

### Vereinsamung und Überholvorgänge

Drei Radfahrer fahren auf einer kreisförmigen, geschlossenen Rennstrecke mit dem Durchmesser $D = 100\,\mathrm{m}$.\
Alle drei starten gleichzeitig zum Zeitpunkt $t=0\,\mathrm{s}$ vom selben Startpunkt $\varphi(t=0\,\mathrm{s}) = 0\,\mathrm{rad}$ und bewegen sich in gleicher Fahrtrichtung mit konstanten Bahngeschwindigkeiten.

Die Geschwindigkeiten betragen:

$$v_{1} = 5\,\mathrm{m/s}, \qquad v_{2} = 7\,\mathrm{m/s}, \qquad v_{3} = 11\,\mathrm{m/s}.$$

Der Streckenumfang ist $U = \pi D$.

**Definition: Abstand auf der Kreisbahn**

Für zwei Fahrer $i$ und $j$ sei $d_{ij}(t)$ der kürzere Bogenabstand entlang der Bahn. Es gilt:

$$0 \le d_{ij}(t) \le \frac{U}{2}$$

Ein Fahrer $i$ gilt als vereinsamt, wenn sein Abstand zu beiden anderen Fahrern mindestens ein Drittel des Umfangs beträgt:

$$d_{ij}(t) \ge \frac{U}{3} \quad \text{für alle } j\neq i$$

a)  Wie oft überholt Fahrer 3 den Fahrer 1 in den ersten $T = 600\,\mathrm{s}$?\
Gib die Anzahl der Überholvorgänge als ganze Zahl an und erläutere kurz dein Vorgehen.

b) Bestimme den frühesten Zeitpunkt $t>0$, zu dem Fahrer 1 und Fahrer 3 wieder gleichzeitig am Startpunkt sind.

c) Bestimme, welcher Fahrer als erster vereinsamt und zu welchem Zeitpunkt dies erstmals geschieht.

d) Untersuche, ob es einen Zeitpunkt gibt, zu dem alle drei Fahrer gleichzeitig vereinsamt sind.\
Falls ja, bestimme den frühestmöglichen Zeitpunkt.\
Falls nein, begründe, warum ein solcher Zeitpunkt nicht existieren kann.

e) Angenommen, das Rennen würde unendlich lange fortgesetzt.\
Gibt es mehrere Zeitpunkte, zu denen alle drei Fahrer gleichzeitig vereinsamt sind?\
Untermauere deine Aussage mit einem kurzen, präzisen Argument.

```{hint}
- Für (a) und (b) ist die Betrachtung der Relativbewegung besonders effizient.
- Es empfiehlt sich, die Bewegung mit einer Winkelkoordinate $\varphi(t)$ oder mit Bogenlängen $s(t)$ zu beschreiben und die Kreisbahn als periodisch aufzufassen (Rechnen „modulo U“).
```