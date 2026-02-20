# Unit-Tests

Unit Tests sind das präziseste Werkzeug, um sicherzustellen, dass Code korrekt, stabil und refaktorierbar bleibt. Die Grundidee ist simpel:\
Wir formulieren Erwartungen an kleine Code-Einheiten  \left(Units \right) und lassen diese Erwartungen automatisch prüfen.

Wir wollen uns das ganze an einem einfachen Beispiel verständlich anschauen. Hierfür bauen wir eine Funktion, die **zwei** Zahlen entgegen nimmt und uns die größere der beiden zurück gibt. Danach implementieren wir sie auf zwei Arten und schreiben Tests, die zeigen, dass beide Implementierungen für viele Eingaben **äquivalent** sind.

---

Bevor wir Tests schreiben, formulieren wir die gewünschte Eigenschaft der Funktion in Klartext. Das ist der Kern jeder Teststrategie:

- **Eingabe:** zwei reelle Zahlen $a, b$ (in Python z. B. `float` oder `int`)
- **Ausgabe:** die größere der beiden Zahlen
- **Randfälle:** Wenn `a == b`, ist das Ergebnis eindeutig (beide sind maximal). Wir legen fest: **wir geben konsistent `a` zurück**.

Damit ist klar: Wir testen **Verhalten**, nicht die Implementierung.

## Vorbereitung: pytest installieren und Projektstruktur

Für Unit Tests nutzen wir **pytest**, weil es:

- sehr leicht lesbare Tests erlaubt (`assert` statt viel Boilerplate),
- hilfreiche Fehlermeldungen liefert,
- Parametrisierung und Fixtures elegant unterstützt.

### Installation

Die Installation erfolgt über den Python-Paketmanager `pip` im Terminal.

```{code-block} console
:caption: Installation von pytest
:linenos:

python -m pip install pytest
```

### Sinnvolle Projektstruktur

Das Ziel ist hinter der Projektstruktur ist, dass wir den Produktionscode und Tests trennen, aber leicht importierbar halten.

```{code-block} none
:caption: Sinnvolle Projektstruktur

project/
├ src/
│ └ max.py
└ tests/
  └ test_max_if.py
```

## `max`-Funktion mit `if`-Anweisung

Wir wollen nun in der Datei `max.py` die erste Version unserer max-Funktion implementieren.\
Hierfür prüfen wir schlicht über eine `if`-Abfrage, welche der beiden Zahlen `a` und `b` größer ist und geben die größere von beiden mit `return` zurück.

```{code-block} python
:caption: max-Funktion (Implementierung mit if-Anweisung)
:linenos:

def max_if(a: int | float, b: int | float) -> int | float:
    if a >= b:
        return a
    return b
```

wir verwenden `>=` statt `>`, da wir so für den Fall `a == b` (beide sind eindeutig "die größere Zahl") konsistent `a` zurück geben.

## Erste Unit-Tests

Bis hierhin haben wir eine Funktion `max_if(a, b)`, die aus zwei Zahlen die größere zurückgeben soll.

Was wir jetzt wollen, ist nicht nur ein *Gefühl* (*"funktioniert schon"*), sondern einen **mechanischen, wiederholbaren Beweis im Code**:

Wenn jemand später

- etwas am Code ändert (*Refactoring*),
- oder wenn wir die Funktion erweitern,
- oder wenn wir die Funktion in einem größeren Projekt verwenden,

sollen wir **in Sekunden** prüfen können, ob das Verhalten noch korrekt ist.

>$\Rightarrow$ Genau dafür sind Unit Tests da.

### Gedankengang vor dem ersten Test

Bevor wir den ersten Test schreiben, stellen wir uns drei sehr einfache Fragen:

1. Was soll herauskommen?\
    Beispiel: `max_if(21, 42)` soll `42` liefern.

2. Welche Fälle sind typisch?\
    Typisch ist "eine Zahl ist größer als die andere" – in beiden Richtungen.

3. Welche Randfälle gibt es?\
    - Gleichheit: `a == b`
    - negative Zahlen
    - Null\
        (Später: Floats, NaN, Infinities, …)

Wenn wir diese Fragen beantwortet haben, können wir Tests so schreiben, dass sie **genau dieses Verhalten absichern**.

### Das Schlüsselwort `assert`

`assert` ist eine Python-Anweisung, die eine Bedingung überprüft.

- Wenn die Bedingung **wahr** ist, passiert nichts (der Test läuft weiter).
- Wenn die Bedingung **falsch** ist, bricht Python ab und wir bekommen einen Fehler (`AssertionError`).

```{code-block} python
:caption: Besipiel für assert
:linenos:

assert 2 + 2 == 4   # OK
assert 2 + 2 == 5   # Fehler: AssertionError
```

Wir können mit `assert` also Sätze formulieren und Python testet, ob diese Sätze **wahr** oder **falsch** sind.\
Für Unit Tests ist `assert` genau das Richtige, weil wir ständig Sätze der Form prüfen wollen:

> "Für diese Eingabe erwarte ich genau diese Ausgabe."

Und das ist exakt eine Bedingung.

### Unser erster Test

Wir legen die Tests in eine Datei, z. B. `tests/test_max.py`.\
In dieser Datei schreiben wir Test-Funktionen.

**Wichtig**: Bei pytest gelten die Konventionen

- **Test-Dateien** beginnen mit `test_...`
- **Testfunktionen** beginnen mit `test_...`

Pytest sucht automatisch nach diesen Benennungen und führt die Tests aus.

```{code-block} python
:caption: Erste Unit Tests mit pytest (Beispiele)
:linenos:

from src.max import max_if

def test_max_if_basic_examples():
    # Typischer Fall: b ist größer als a
    assert max_if(3, 7) == 7

    # Typischer Fall: a ist größer als b
    assert max_if(7, 3) == 7

    # Randfall: Gleichheit (Konvention: bei a == b geben wir a zurück)
    assert max_if(5, 5) == 5


def test_max_if_negative_numbers():
    # Auch mit negativen Zahlen muss die Funktion korrekt arbeiten
    assert max_if(-2, -5) == -2
    assert max_if(-5, -2) == -2
```

**Was passiert hier gedanklich?**

- Jede Zeile assert `max_if(...) == ...` ist eine kleine Aussage:
    - "Wenn ich diese Eingabe gebe, muss diese Ausgabe kommen."
- Wenn nur eine dieser Aussagen falsch ist, ist die Funktion (oder unsere Spezifikation) an dieser Stelle nicht erfüllt.

So wird aus einer vagen Idee (*"sollte funktionieren"*) ein prüfbarer Vertrag.

### Tests durchführen

Wenn die Konsole im Projektordner geöffnet ist, kann mit dem Befehl

```{code-block} console
:caption: Durchführen von pytest-Tests
:linenos:

python -m pytest
```

das Ausführen der Tests gestartet werden. Dabei passiert Folgendes:

1. pytest sucht nach Dateien, die `test_*.py` heißen.
2. pytest importiert diese Dateien.
3. pytest sucht darin Funktionen, die mit `test_` beginnen.
4. pytest führt jede Testfunktion aus.
5. Sobald ein `assert` fehlschlägt, wird der Test als fehlgeschlagen markiert, und pytest zeigt dir:
    - welche Zeile,
    - welche Werte,
    - und welche Bedingung nicht erfüllt war.

Das ist ein enormer Vorteil gegenüber *"ich drucke mal ein paar Werte aus"*.

````{admonition} Konsolen Output
:class: terminal-output

```{code-block} console

====================================== test session starts ======================================
platform win32 -- Python 3.13.7, pytest-8.4.2, pluggy-1.6.0
rootdir: <Pfad>
plugins: anyio-4.11.0, cov-7.0.0
collected 2 items

tests\test_max_if.py ..                                                                    [100%]

======================================= 2 passed in 0.03s =======================================
```
````

### Warum mehrere `asserts` in einem Test

wir könnten auch jeden einzelnen Fall in eine eigene Testfunktion packen. Beides ist erlaubt.

Die Entscheidung ist didaktisch:

- In einer Einführungsphase ist es oft gut, mehrere `asserts` in einem Test zu bündeln, wenn sie thematisch zusammengehören ("Basic Examples").
- Später ist es oft besser, Tests feiner zu schneiden, um Fehlermeldungen noch präziser zu machen.

pytest stoppt übrigens nicht beim ersten fehlgeschlagenen Test der gesamten Suite, sondern markiert den Test als fail und macht mit den anderen weiter.

### Parametrisierung von Tests

Wenn wir viele ähnliche Tests haben, wollen wir nicht alles mit Copy-Paste schreiben. Hier kommt ein wichtiges pytest-Werkzeug ins Spiel: **Parametrisierung**.

Die Idee:

>Wir schreiben einmal die Testlogik und geben viele Testfälle als Daten dazu.

Dazu sieht man eine Zeile mit `@...` direkt über einer Funktion. Das ist ein **Decorator**.

#### Was ist ein Decorator

Ein Decorator ist in Python eine Konstruktion, die eine Funktion **verändert oder erweitert**, ohne dass wir ihren Code anfassen müssen.

```{code-block} python
:caption: Decorator (formal)
:linenos:

@irgendwas
def meine_funktion(...):
    ...
```

Wir können uns das vorstellen wie:\
"Nimm diese Funktion und wende vor dem Ausführen noch eine Zusatzlogik darauf an."

Im Kontext von pytest bedeutet das, dass `@pytest.mark.parametrize(...)` pytest sagt:\
"Führe diese Testfunktion mehrfach aus. Jeweils mit anderen Eingabewerten.“

Wir müssen Decorator an dieser Stelle nicht im tiefen Python-Sinne verstehen. Für Unit Tests reicht dieses mentale Modell völlig:\
Decorator = Anweisung an pytest, wie die Testfunktion ausgeführt werden soll.

#### Parametrisierter Test für `max_if`

```{code-block} python
:caption: Parametrisierte Tests mit pytest
:linenos:

import pytest
from src.max import max_if

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (3, 7, 7),
        (7, 3, 7),
        (5, 5, 5),
        (-2, -5, -2),
        (0, 0, 0),
    ],
)
def test_max_if_parametrized(a, b, expected):
    assert max_if(a, b) == expected
```

Bei dieser Implementierung passiert nun folgendes:

- `"a,b,expected"` sind die Parameter-Namen.
- Die Liste darunter enthält Testfälle als Tupel:
    - `(a, b, expected)`
- pytest ruft die Testfunktion mehrfach auf, z. B. so:
    1. `test_max_if_parametrized(a=3, b=7, expected=7)`
    2. `test_max_if_parametrized(a=7, b=3, expected=7)`
    3. `test_max_if_parametrized(a=5, b=5, expected=5)`\
        …

Und jedes Mal prüft `assert`, ob die Erwartung erfüllt ist.

```{admonition} Typische Denkfehler
:class: error

**1. "Ich teste die Implementierung"**

Falsch: Tests sollten Verhalten testen.\
Beispiel: Du testest nicht "wurde der if-Zweig genommen", sondern: "kommt bei dieser Eingabe der richtige Wert raus?"

**2. "Ich teste nur einfache Fälle"**

Das ist der häufigste Anfängerfehler.\
Besser ist: **typische Fälle + Randfälle**.

**3. "Ich verlasse mich auf Print-Ausgaben"**

Print ist gut zum Debuggen, aber nicht als Qualitätsstrategie.\
Unit Tests sind automatisierbar und wiederholbar.
```

## `max`-Funktion mit Mathematischer Formel

Bisher haben wir den Maximalwert mit einer `if`-Abfrage bestimmt. Das ist klar, direkt und in der Praxis absolut sinnvoll.\
Jetzt machen wir etwas, das in Mathematik und Physik oft vorkommt.

>Wir ersetzen eine Fallunterscheidung durch eine geschlossene Formel.

Das ist interessant, weil Formeln oft leichter zu analysieren, zu optimieren oder in größere Herleitungen einzubauen sind.\
Mathematisch kann der größere Wert zweier Zahlen mit der Formel

$$M \left(a,b \right) = \frac{a + b + \left| a - b \right|}{2}$$

bestimmt werden.\
Diese Gleichung liefert für $a, b \in \mathbb{R}$ stets den größeren der beiden Werte, also

$$M \left(a, b \right) = \max \left(a, b \right)$$

```{figure} ../../_static/img/python/unit-test/max-formula.jpg
:align: center
:width: 100%

Grafische Veranschaulichung der Formel
```

````{dropdown} Mathematischer Beweis der Formel
:icon: info

**Beweis mittels Fallunterscheidung**

Der Betrag $\left| a − b \right|$ kodiert genau die Information, welche der beiden Zahlen größer ist. Daher führen wir eine Fallunterscheidung durch.

**Fall 1: $a \ge b$**

Dann gilt $a - b \ge 0$ und somit

$$\left| a - b \right| = a - b.$$

Wenn wir dies nun in die Definition von $M \left( a, b \right)$ einsetzen, ergibt sich

$$M \left( a, b \right) = \frac{a + b + \left( a - b \right)}{2} = \frac{2a}{2} = a.$$

Für den betrachteten Fall $a \ge b$ ist $\max \left( a, b \right) = a$.\
$\Rightarrow$ Die Formel liefert also den korrekten Maximalwert.

**Fall 2: $a < b$**

Dann gilt $a - b < 0$ und damit

$$\left| a - b \right| = - \left(a - b \right) = b - a.$$

Eingesetzt in die Definition $M \left( a, b \right)$:

$$M \left( a, b \right) = \frac{a + b + \left( b - a \right)}{2} = \frac{2b}{2} = b.$$

Für den betrachteten Fall $b > a$ gilt $\max \left( a, b \right) = b$.\
$\Rightarrow$ Auch hier liefert die Formel exakt den Maximalwert.

**Schlussfolgerung**

Die beiden Fälle $a \ge b$ und $a < b$ decken alle möglichen reellen Zahlenpaare ab. Damit gilt insgesamt:

$$
\boxed{\frac{a + b + \left| a - b \right|}{2} = \max \left( a, b \right) \quad \text{für alle } a, b \in \mathbb{R}}
$$

```{admonition} Interpretation der Formel
:class: note

Der Term $\frac{1}{2} \left( a + b \right)$ bildet den arithmetischen Mittelwert.\
Der Term $\frac{1}{2} \left( \left| a - b \right| \right)$ addiert genau die halbe Differenz in Richtung des größeren Wertes.

$\Rightarrow$ Dadurch wird der Mittelwert systematisch auf den Maximalwert verschoben.

```
````

```{code-block} python
:caption: max-Funktion als Formel-Implementierung
:linenos:

def max_formula(a: int | float, b: int | float) -> float:
    return (a + b + abs(a - b)) / 2
```

Diese Implementierung können wir nun auch in der Datei `src/max.py` ablegen.

```{hint}
In Python erzeugt `/` immer eine Gleitkommazahl (`float`).\
Das bedeutet:

- `max_if(5, 2)` ergibt `5`
- `max_formula(5, 2)` ergibt `5.0`

Numerisch sind diese Werte gleich (`5.0 == 5` ist `True`), aber der Typ ist anders. Das ist kein "Bug", aber ein Punkt, den man bewusst kennen sollte.
```

### Tests für `max_formula`

Wir beginnen wieder mit einfachen Bespielen. Wir testen das Verhalten wieder mit konkreten Fällen, bevor wir systematisch werden.\
Der Test kann in einer neuen Datei `tests/test_max_formula.py` abgelegt werden.

```{code-block} python
:caption: Beispielbasierte Tests für max_formula
:linenos:

from src.max import max_formula

def test_max_formula_basic_examples():
    assert max_formula(3, 7) == 7
    assert max_formula(7, 3) == 7
    assert max_formula(5, 5) == 5
```

`max_formula(...)` liefert wie erwähnt immer einen `float`-Wert. `7 == 7.0` funktioniert, weil Python diesen Vergleich mit `True` bewertet.\
Sobald wir jedoch echte Fließkommazahlen testen, kann `==` gefährlich werden (Rundungsfehler). Darum führen wir jetzt das richtige Werkzeug ein.

---

Computer speichern `float`-Zahlen nicht exakt (binäre Darstellung). Viele Dezimalzahlen können nicht genau dargestellt werden, z. B. `0.1`.

Deshalb kann so etwas passieren:

- mathematisch: $0,1 + 0,2 = 0,3$
- in floating point: `0.1 + 0.2` ist nicht exakt `0.3`

```{code-block} python
:caption: Besipiel für addition mit floats
:linenos:

assert 0.1 + 0.2 == 0.3   # Fehler: AssertionError
```

Wenn wir dann mit `==` testen, kann ein Test fälschlicherweise fehlschlagen.

Dieses Problem löst `pytest.approx`. Durch diesen Aufruf wird nicht auf exakte Gleichheit überprüft, sondern eine kleine numerische Abweichung als zulässig berücksichtigt.\
Damit schreiben wir robuste Tests für `float`.

### Parametrisierte Tests für `max_formula`

Hier folgt nun wieder der Gedanke: Gleiche Testlogik, viele Testfälle $\rightarrow$ Parametrisierung.

```{code-block} python
:caption: Parametrisierte Tests für max_formula (mit approx)
:linenos:

import pytest
from src.max import max_formula

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (3, 7, 7),
        (7, 3, 7),
        (5, 5, 5),
        (-2, -5, -2),
        (0, 0, 0),
        (0.1, 0.2, 0.2),
        (-0.1, -0.2, -0.1),
    ],
)
def test_max_formula_parametrized(a, b, expected):
    assert max_formula(a, b) == pytest.approx(expected)
```

Gedankengang dahinter:

- Wir wollen nicht, dass Tests bei korrektem Code wegen Rundung scheitern.
- `approx` macht den Test numerisch stabil.
- Gleichzeitig bleibt der Test inhaltlich präzise: wir prüfen weiterhin den erwarteten Wert.

Über den Befehl

```{code-block} console
:caption: Durchführen von pytest-Tests
:linenos:

python -m pytest
```

können nun alle Tests durchgeführt werden und wir sollten dieses Ergebniss erhalten:

````{admonition} Konsolen Output
:class: terminal-output

```{code-block} console

===================================== test session starts ======================================
platform win32 -- Python 3.13.7, pytest-8.4.2, pluggy-1.6.0
rootdir: <Pfad>
plugins: anyio-4.11.0, cov-7.0.0
collected 11 items

tests\test_max_formula.py ......                                                          [ 54%] 
tests\test_max_if.py .....                                                                [100%]

====================================== 11 passed in 0.06s ======================================
```
````

## Äquivalenztest beider Implementierungen

Wir wollen nun zeigen, dass beide Implementierungen (für "normale" Zahlen) dasselbe liefern.\
Das ist ein sehr mächtiges Muster, weil es später hilft bei:

- Refactoring (neue Version vs. alte Version)
- Optimierung (schnellere Version vs. Referenzversion)
- mathematischen Umformungen (Formel vs. Fallunterscheidung)

### Äquivalenztest über viele Werte

Wir testen systematisch über ein ganzes Gitter von Werten. Hierfür legen wir eine neue Datei `tests/test_equivalent_max.py` an und fügen den folgenden Test ein:


```{code-block} python
:caption: Äquivalenztest: max_if und max_formula liefern dasselbe Ergebnis
:linenos:

import pytest
from src.max import max_if, max_formula

def test_equivalence_many_values():
    for a in range(-100, 101):
        for b in range(-100, 101):
            assert max_formula(a, b) == pytest.approx(max_if(a, b))
```

Wir erzeugen hier viele Eingaben automatisch.
Für jedes Paar $\left( a, b \right)$ vergleichen wir:

- Referenz: `max_if(a,b)` (klar und leicht zu vertrauen)
- Kandidat: `max_formula(a,b)` (Formelumsetzung)

Wir verwenden hier `approx`, da `max_formula` `float` zurück gibt.\
Auch wenn die Werte bei Integers meistens exakt sind, ist `approx` das professionellere Muster, sobald Floats im Spiel sind.

Wird nun wiedermals ein Test mit dem Befehl

```{code-block} console
:caption: Durchführen von pytest-Tests
:linenos:

python -m pytest
```

gestartet, so sollten wieder alle Tests bestanden sein. Damit haben wir gezeigt, dass wir für den getesteten Zahlenbereich und die Überprüften Sonderfälle beide Funktionen Äquivalent verwenden können.

## Wie entwickeln wir Testfälle?

```{admonition} Testfälle entwickeln
:class: hint

**1. Typische Fälle (Standardverhalten)**\
    "normale" Inputs, die erwartbar sind\
    $a > b$ und $a < b$ 

**2. Randfälle (Grenzen und Sonderfälle)**\
    - Gleichheit ($a=b$)\
    - Null\
    - negative Werte\
    - sehr große Werte

**3. Systematische Tests (viele Werte automatisch)**\
    - Schleifen über Wertebereiche\
    - Parametrisierung mit vielen Fällen\
    - zufällige Tests (später)

**Regel:**\
Je mathematischer eine Funktion ist, desto sinnvoller sind systematische Tests.
```