(Fourierreihe)=
# Fourierreihe

Wie eingangs beschrieben dienen Transformationen dazu, Funktionen in neue Räume zu überführen, in denen sich ihre Eigenschaften klarer offenbaren. Bevor wir jedoch zu allgemeinen und abstrakteren Transformationen übergehen, lohnt sich der Blick auf eine besonders intuitive Variante, die den Grundstein für fast alle späteren Methoden legt: die **Fourier-Reihe**.

Der französische Mathematiker und Physiker **Jean Baptiste Joseph Fourier** stellte sich zu Beginn des 19. Jahrhunderts die Frage, ob sich jede periodische Funktion als Summe von unendlich vielen Sinus- und Kosinus-Schwingungen darstellen lässt. Sinus- und Kosinusfunktionen sind uns aus der Natur bestens vertraut:

```{figure} ../../../_static/plots/analysis/transformationen/fourier-reihe/kreisfunktionen.png
:align: center
:width: 60%

Geometrische Interpretation von Sinus und Kosinus
```

Sie beschreiben Schwingungen, Wellen und Oszillationen, alles grundlegende Bewegungsformen vieler physikalischer Systeme.

Die Fourier-Reihen eignen sich ideal als Startpunkt für die Reise durch alle möglichen Arten von Transformationen, da sie
- mit uns bekannten und vertrauten Funktionen arbeiten (Sinus und Kosinus),
- eine periodische Funktion in orthogonale Anteile zerlegt (ein Prinzip, das in fast allen Transformationen wiederkehrt),
- verbindet unmittelbar den Zeitbereich mit dem Frequenzbereich und macht die energetische Struktur eines Signals sichtbar.

Damit erfüllt die Fourier-Reihe denselben Zweck wie jede Transformation:\
Sie überführt eine komplexe Abhängigkeit in eine Darstellung, in der ihre Struktur einfacher, oft sogar verblüffend klar hervortritt.

**Zerlegung in harmonische Komponenten**

Um die Grundidee unmittelbar sichtbar zu machen, betrachten wir zwei typische periodische Funktionen:\
Eine achsensymmetrischen Rechteckfunktion und eine punktsymmetrische Sägezahnfunktion.

Mit dem folgenden Slider lässt sich die Anzahl der berücksichtigten Schwingungen $N$ verändern.\
So wird sichtbar, wie beide Funktionen aus ihren harmonischen Bausteinen entstehen.