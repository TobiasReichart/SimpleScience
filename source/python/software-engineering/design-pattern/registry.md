# Das Registry Pattern

Oft kommt es vor, dass wir Fallunterscheidungen vornehmen müssen, damit je nach Anwendungsfall die richtige Opteration ausgeführt wird und der Code sich so verhält, wie wir die Logik implementiert haben. Damit wir in solchen Fällen keine `if/elif`-Kaskaden bauen und den Code unnötig kompliziert wird, wollen wir im folgenden das **Registry Pattern** Schritt für Schritt entwickeln.

>Wir speichern Varianten nicht als Kontrollfluss (`if/elif`), sondern als Zuordnung (Mapping) von Namen zu Implementierungen.

Das klingt im ersten Moment abstrakt... Deshalb nutzen wir ein sehr einfaches Praxisbeispiel, das sich komplett ohne mathematischen Kontext versteht.

## Praxisbeispie: Text-Transformationen

Wir möchten eine Funktion `transform(text, name)`, die abhängig von `name` unterschiedliche Transformationen auf text anwendet, z. B.:

- `"upper"` $\rightarrow$ Großbuchstaben
- `"lower"` $\rightarrow$ Kleinbuchstaben
- `"strip"` $\rightarrow$ Leerzeichen außen entfernen
- `"snake"` $\rightarrow$ Leerzeichen durch `_` ersetzen

Diese Arten von Operationen sind in der Praxis extrem häufig: Labels normalisieren, Dateinamen standardisieren, Spaltennamen vereinheitlichen, etc.

### Der naive Ansatz: `if/elif`

Dieser Ansatz ist funktionsfähig und bei einzelnen Abfragen oft auch die pragmatischere Lösung. Es gibt jedoch einen Punkt (den jeder Entwickler für sich selbst definiert) an dem diese Lösung nicht mehr praktikabel ist.

**Das Problem**: Der Ansatz skaliert schlecht.\
Bei 10, 20 oder mehr Fällen, wird die Funktion schwer zu überblicken.

- Jeder neue Fall bedeutet: **bestehende Kernlogik anfassen**.
- Mehrere Personen, die gleichzeitig erweitern, führen leicht zu Merge-Konflikten.
- Tests hängen an einer großen Schaltzentrale statt an klaren Bausteinen.

Wir möchten erreichen, dass der Kern stabil bleibt und Erweiterungen "von außen" möglich sind.

```{code-block} python
:caption: naiver Ansatz für Text-Transformation
:name: code-registry-naive
:linenos:

def transform(text: str, name: str) -> str:
    if name == "upper":
        return text.upper()
    elif name == "lower":
        return text.lower()
    elif name == "strip":
        return text.strip()
    elif name == "snake":
        return text.replace(" ", "_")
    else:
        raise ValueError(f"Unbekannte Transformation: {name}")
```

Über den **Steuerparameter** `name` wird je nach Wert eine andere Opteration ausgeführt.\
Für unbekannte Werte werfen wir einen Fehler (das ist gut, weil stilles "Nichts tun" gefährlich wäre).

## Die Kernidee hinter der Registry

Statt\
"Wenn `name` so ist, dann tu dies…"\
wollen wir nun\
"`name` ist ein Schlüssel, hinter dem eine Funktion liegt."

Formal ist das ein Wörterbuch (*Dictionary*):

$$\text{Registry:} \quad \text{str} \mapsto \text{Funktion}$$

Wir haben also links einen Namen, der eindeutig auf ein Stück Code verweist, welcher die gewünschte Operation ausführt.

## Implementierung der Registry auf unser Beispiel

Wir wollen nun das Beispiel aus {numref}`code-registry-naive` nach dieser Idee umbauen. Hierfür müssen wir zunächst jede Funktionalität in eine eigene Funktion packen.

### 1. Funktionalität in einzelne Funktionen

Jede Variante wird nun eine **eigenständige, testbare Einheit**. So besitzt jede Funktion eine klare Aufgabe, die leicht zu verstehen ist. Dabei ist die Signatur `text: str -> str` jeder Funktion gleich. Dadurch verhindern wir, dass wir später Fehler durch einen anderen erwarteten Typ auslösen.

```{code-block} python
:caption: Text-Transformationen in einzelnen Funktionen
:name: code-registry-funktions
:linenos:

def to_upper(text: str) -> str:
    return text.upper()

def to_lower(text: str) -> str:
    return text.lower()

def strip_outer(text: str) -> str:
    return text.strip()

def to_snake(text: str) -> str:
    return text.replace(" ", "_")
```

```{hint}
Registry funktioniert am besten, wenn alle registrierten Funktionen eine **konsistente Schnittstelle** besitzen.
```

### 2. Definieren einer Registry (Dictionary)

Nun bauen wir ein Dictionary, dass jeder Funktion aus {numref}`code-registry-funktions` einen eindeutigen Schlüssel zuweist.

```{code-block} python
:caption: Registry für Text-Transformationen
:linenos:

REGISTRY: dict[str, callable] = {
    "upper": to_upper,
    "lower": to_lower,
    "strip": strip_outer,
    "snake": to_snake,
}
```

Ein Aufruf `REGISTRY["upper"]` liefer nun **die Funktion** `to_upper` und nicht das Ergebnis.

```{note}
Funktionen sind in Python "First-Class Objects".\
Also **Entitäten**, die wir wie Standardvariablen behandeln können: speichern, weitergeben, aus Dictionaries holen.
```

Bildlich gesprochen ist unsere `REGISTRY` ein Telefonbuch, in dem `name` wie auch im echten Telefonbuch der Name ist und die Telefonnummer, die wir anrufen, eine Funktion ist.

### 3. Auswahl-Funktion für den Aufruf der Operationen

Abschließend brauchen wir jetzt noch eine Funktion, die die passende Funktion aus der Registry holt und diese auf den übergebenen Text anwendet.

```{code-block} python
:caption: Auswahl-Funktion
:linenos:

def transform(text: str, name: str) -> str:
    try:
        func = REGISTRY[name]
    except KeyError:
        raise ValueError(f"Unbekannte Transformation: {name}") from None

    return func(text)
```

In dieser Funktion holen wir mit `func = REGISTRY[name]` die passende Funktion aus der Registry. Falls `name` nicht existiert, werfen wir einen eigenen Fehler, der semantisch besser passt.\
Am Ende rufen wir die Funktion mit dem Übergebenen Parameter auf und geben das Ergebnis zurück.

```{important}
Hier steckt die gesamte Dynamik in nur zwei Schritten:

1. auswählen (Lookup)
2. ausführen (call)
```

### Registrybasierte Text-Transformation

Die Text-Transformation-Datei sollte nun wie folgt aussehen.

```{code-block} python
:caption: Registrybasierte Text-Transformation
:name: code-registry-lsg
:linenos:

REGISTRY: dict[str, callable] = {}

# --- Auswahlfunktion ---
def transform(text: str, name: str) -> str:
    try:
        func = REGISTRY[name]
    except KeyError:
        raise ValueError(f"Unbekannte Transformation: {name}") from None

    return func(text)

# --- Text-Transformationen ---
def to_upper(text: str) -> str:
    return text.upper()

REGISTRY["upper"] = to_upper

# ---
def to_lower(text: str) -> str:
    return text.lower()

REGISTRY["lower"] = to_lower

# ---
def strip_outer(text: str) -> str:
    return text.strip()

REGISTRY["stip_outer"] = strip_outer

# ---
def to_snake(text: str) -> str:
    return text.replace(" ", "_")
    
REGISTRY["snake"] = to_snake
```

Im grunde ist es hier den eigenen Präferenzen überlassen, ob man unter jeder Funktion, diese in einer leer initialisierten `REGISTRY` registrieren möchte, oder ob die Registrierung einmalig für alle Funkktionen oder in einer Mischform geschieht.\
Der Hauptvorteil bei der hier Verwendeten Variante besteht darin, dass so beim entfernen von Funktionen das löschen des Eintrags nicht vergessen werden kann.

```{admonition} Typische Stopersteine
:class: note

**1. Alle registrierten Funktionen sollten dieselbe Signatur besitzen.**\
    Wenn eine registrierte Funktion andere Parameter entgegen nimmt, als die anderen registrierten Funktionen, ist das ein **Designfehler**.\
    $\Rightarrow$ Eine Registry verwaltet Varianten derselben Art, nicht beliebige Funktionen.

**2. Sinnvolle Fehlermeldungen**\
    Unbekannte Keys sollten nicht stillschweigend ignoriert werden. "Silent failure" ist gefährlich, da so falsche Ergebnisse ohne Warnung geliefert werden.\
    $\Rightarrow$ Klare Exceptions sind kein "nice to have", sondern für die Handhabung unabdingbar.

**3. Namenskonventionen**\
    Wenn Keys später in Konfigurationsdateien stehen, sollten sie:\
    - kurz, stabil, eindeutig\
    - nicht von Implementierungsdetails abhängen\
    - nicht zu "kreativ" benannt sein

**4. Registry als globales Chaos vermeiden**\
    Eine Registry ist eine zentrale Struktur, die\
    - pro nur eine "Kategorie" verwaltet. $\rightarrow$ pro "Kategorie" eine eigene Registry\
    - klare Zuständigkeiten besitzt.\
    - nicht global alles verwalten soll.
```

## Selbst-Registrierung mit Decorator

Wenn wir in {numref}`code-registry-lsg` jede Funktion **manuell** über eine eigene Registry-Zuweisung (z. B. in den Zeilen 16, 22, 28 und 34) registrieren, ist das zwar transparent, aber auch fehleranfällig.\
Wir können einen Eintrag vergessen, einen Schlüssel vertippen oder aus Versehen denselben Namen doppelt vergeben. Solche Fehler fallen oft erst spät auf und im ungünstigsten Fall erst dann, wenn eine bestimmte Variante tatsächlich ausgewählt wird.

Um genau diese Klasse von Problemen zu reduzieren, nutzen wir **Decorator**, die die Funktion **direkt beim Definieren** registrieren. Das bedeutet, dass sobald die Funktion im Code auftaucht, ist sie automatisch korrekt in der Registry eingetragen und dass ohne zusätzlichen "Nachtrag" darunter.

---

Ein Decorator ist in Python eine Funktion, die eine andere Funktion entgegennimmt und (meist) wieder zurückgibt. Oft packt der Decorator zusätzliche Logik "drumherum".

1. Wir schreiben eine Funktion `register`, die als Parameter den Schlüssel (`key`) der zu registrierende Funktion erhält.
2. In `register` definieren wir eine weitere Funktion `decorate`, die die zu dekorierende Funktion als Objekt übergeben bekommt (z. B. `to_upper`). Die Funktion `decorate` muss durch `register` zurück gegeben werden.
3. Die Funktion `decorate` überprüft, ob die Funktion schon registriert ist und wirft einen Fehler oder registriert diese.
4. Die Funktion `decorate` gibt die übergebene Funktion wieder zurück, damit diese noramal nutzbar bleibt.

```{code-block} python
:caption: Registry-Decorator
:linenos:

REGISTRY: dict[str, callable] = {}

def register(name: str):
    def deco(func):
        if name in REGISTRY:
            raise ValueError(f"Doppelter Name in Registry: {name}")
        REGISTRY[name] = func
        return func
    return deco
```

Damit können wir jetzt so schreiben:

```{code-block} python
:caption: Nutzung des Registry-Decorators
:linenos:

@register("upper")
def to_upper(text: str) -> str:
    return text.upper()
```

Mit dem Decorator erzwingen wir einen konsistenten Ablauf:

- **Keine vergessene Registrierung**: Wenn die Funktion existiert, wird sie registriert.
- **Kein "zweiter Pflegeort"**: Wir müssen nicht an zwei Stellen arbeiten (Funktion + Registry-Zeile).
- **Doppelte Namen werden sofort erkannt**: Der Fehler entsteht direkt beim Import/Start, nicht erst zur Laufzeit "irgendwann".

```{important}
Die Registrierung passiert in dem Moment, in dem Python den Funktionskopf verarbeitet, also typischerweise beim Import des Moduls.
```