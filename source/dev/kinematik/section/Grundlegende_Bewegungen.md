# Grundlegende Bewegungen

Wer Bewegungen aufmerksam beobachtet, erkennt schnell ein erstaunlich stabiles Muster:\
Ein Körper, der sich bewegt, ändert seinen Bewegungszustand nicht von selbst. Ebenso bleibt ein Körper, der ruht, in Ruhe, solange nichts seine Bewegung verändert. Diese alltägliche Erfahrung bildet den Ausgangspunkt der Kinematik.

## Der Ort als Funktion der Zeit

Ein Körper befindet sich zu jedem Zeitpunkt an einem bestimmten Ort. Ändert sich dieser Ort mit fortschreitender Zeit, so sprechen wir von Bewegung. Wir können also die Bewegung eines Körpers beschreiben, indem wir zu jedem Zeitpunkt notieren, an welchem Ort sich der Körper befunden hat. Bewegung lässt sich daher auf eine einzige Zuordnung zurückführen:
```{centered} **Den Ort als Funktion der Zeit.**
```

### Der Begriff des Ortes

Der Ort eines Körpers ist keine Strecke und keine Bewegung, sondern eine Koordinate. In einer Dimension genügt uns zur Beschreibung des Ortes eine einzelne Zahl, die angibt, wo sich der Körper relativ zu einem gewählten Bezugspunkt befindet. Diese Zahl kann positiv oder negativ sein und trägt damit eine klare geometrische Information:\
Sie beschreibt die Lage des Körpers entlang einer Achse.

```{figure} ../../../_static/plots/mechanik/kinematik/01_Ort.png
:align: center
:width: 60%

Position eines Körpers zu unterschiedlichen Zeitpunkten
```

Wichtig ist dabei die Unterscheidung zwischen Ort und zurückgelegtem Weg. Zwei Körper können sich am gleichen Ort befinden, obwohl sie völlig unterschiedliche Wege dorthin zurückgelegt haben. In der Kinematik interessiert uns zunächst ausschließlich der momentane Ort eines Körpers und nicht dessen Vorgeschichte.

### Wahl des Koordinatensystems

Um einen Ort angeben zu können, muss ein Koordinatensystem festgelegt werden.\
Hierfür benötigen wir folgende Informationen:

- einen Ursprung,
- eine Richtung, die als positiv definiert wird,
- sowie eine Längenskala.

Diese Wahl ist grundsätzlich frei. Die physikalische Bewegung eines Körpers ändert sich nicht dadurch, dass wir den Ursprung verschieben oder die Achse umdrehen. Dennoch ist diese Entscheidung nicht belanglos:\
Alle Ortsangaben beziehen sich stillschweigend auf das gewählte Koordinatensystem. Eine saubere kinematische Beschreibung setzt daher voraus, dass dieses implizite Bezugssystem klar ist und wir dieses für die gesamte Betrachtung verwenden und nicht wahllos unterschiedliche Koordinatensysteme verwenden.

### Zeit als unabhängige Variable

Bewegung zeigt sich erst, wenn wir die Zeit als unabhängige Variable hinzu nehmen. Deshalb behandeln wir die Zeit als eine kontinuierliche und unabhängige Variable, die den Ablauf der Bewegung parametrisiert. Der Körper „bewegt sich nicht durch die Zeit“, sondern seine Position ändert sich mit der Zeit.

Damit ist die Rollenverteilung eindeutig:
- Die Zeit $t$ ist der Parameter.
- Der Ort $x$ ist die davon abhängige Größe.

Diese Sichtweise ist entscheidend für alles, was folgt.

---

Wir können also Formal den Ort eines Körpers als Funktion der Zeit Schreiben

$$x = x(t)$$

```{important}
Diese Schreibweise bedeutet, dass wir jedem Zeitpunkt $t$ genau einen Ort $x$ zuordnen können.\
Die Funktion $x(t)$ enthält damit die vollständige Information über die Bewegung des Körpers in einer Dimension.
```

Je nach Art der Bewegung kann diese Funktion sehr unterschiedlich aussehen:

```{figure} ../../../_static/plots/mechanik/kinematik/02_Ort.png
:align: center
:width: 100%

unterschiedlicher Bewegungen
```

Die konkrete Form von $x(t)$ ist das zentrale Objekt der kinematischen Beschreibung.

Diese Darstellung wird als **Weg-Zeit-Diagramm** bezeichnet. Hierbei wird auf der horizontalen Achse die Zeit aufgetragen und auf der vertikalen Achse der Ort. Jeder Punkt in diesem Diagramm entspricht einer eindeutigen Position des Körpers zu einem bestimmten Zeitpunkt.

Dieses Diagramm ist die Bewegung in grafischer Form. Hier lassen sich bereits wichtige Eigenschaften ohne Rechnung erkennen:

- **Eine horizontale Linie beschreibt einen ruhenden Körper.**\
    Die Position des Körpers ist unabhängig von der Zeit.
- **Eine gerade Linie mit konstanter Steigung repräsentiert eine {ref}`gleichförmige Bewegung <gleichförmige Bewegung>`.**\
    Der Körper legt immer die gleiche Strecke zwischen Zeitpunkt $A$ und Zeitpunkt $B$ zurück, solange der Abstand zwischen den  beiden Zeitpunkten konstant ist.
- **Eine gekrümmte Linie deutet auf eine Änderung der Geschwindigkeit hin.**\
    Das Kriterium der {ref}`gleichförmigen Bewegung <gleichförmige Bewegung>` ist nicht mehr erfüllt.

Damit können wir aus dieser einfachen Darstellung bereits wertvolle Informationen über die Bewegung eines Körper herauslesen.

Zwischen den Zeitpunkten $t_{1}$ und $t_{2}$ ändert sich der Ort eines Körpers um

$$\Delta x = x(t_{2}) - x(t_{1})$$

in der Zeit

$$\Delta t = t_{2} - t_{1}.$$

**Beispielaufgabe: Endliche Ortsänderung $\Delta x$**

Ein Körper bewegt sich entlang der x-Achse. Zu den Zeitpunkten\
$t_{1} = 2,0\,\mathrm{s}, \qquad t_{2} = 7,0\,\mathrm{s}$\
befindet er sich an den Orten\
$x(t_{1})= -1,5\,\mathrm{m}, \qquad x(t_{2})= 8,0\,\mathrm{m}.$

1. Bestimme die endliche Ortsänderung $\Delta x$.
```{dropdown} Lösung
Per Definition gilt:\
$\Delta x = x(t_{2}) - x(t_{1}).$\
$\Delta x = 8,0\,\mathrm{m} - (-1,5\,\mathrm{m}) = 9,5\,\mathrm{m}.$
```
2. Bestimme das Zeitintervall $\Delta t$.
```{dropdown} Lösung
$\Delta t = t_{2} - t_{1} = 7,0\,\mathrm{s} - 2,0\,\mathrm{s} = 5,0\,\mathrm{s}.$
```
3. Interpretiere das Vorzeichen von $\Delta x$.
```{dropdown} Lösung
Da $\Delta x > 0$, hat sich der Ort in Richtung positiver $x$-Werte verändert. Das ist eine rein geometrische Aussage über die Koordinatenrichtung. Sie bedeutet nicht automatisch, dass sich der Körper während des gesamten Intervalls „nur nach rechts“ bewegt hat.\
Für diese Aussage sind mehr Informationen über den Verlauf $x(t)$ zwischen $t_{1}$ und $t_{2}$ nötig.
```

## Der Begriff der Geschwindigkeit

```{figure} ../../../_static/plots/mechanik/kinematik/01_Geschwidigkeit.png
:align: center
:width: 80%

Durchschnittsgeschwindigkeit
```

## Die Beschleunigung


## Sonderformen der Bewegung

(gleichförmige Bewegung)=
### Die Gleichförmige Bewegung


### Die gleichmäßig beschleunigte Bewegung


#### Der freie Fall (ohne Luftwiderstand)


## Der freie Fall (mit Luftwiderstand)

