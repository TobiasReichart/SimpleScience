(Nummerierung und Referenzen)=
# Nummerierung und Referenzen


In technischen und wissenschaftlichen Texten ist es essenziell, auf Inhalte eindeutig und stabil verweisen zu können.\
Sphinx stellt hierfür ein konsistentes System aus **globaler Nummerierung**, **Referenzen** und **Ankern** bereit, das unabhängig von der Seitenstruktur funktioniert.

Wir wollen uns in diesem Abschnitt ansehen,

- wie Inhalte nummeriert werden,
- wie auf Abbildungen, Tabellen, Codeblöcke und Formeln verwiesen wird,
- und wie gezielt verlinkbare Anker gesetzt werden.

(Inhalte Verlinken)=
## Inhalte Verlinken

Grundsätzlich unterscheidet Sphinx zwischen zwei Arten von Verlinkungen:

1. **Strukturelle Verweise** auf Seiten oder Abschnitte
2. **Objektverweise** auf nummerierte Elemente wie Abbildungen, Tabellen oder Gleichungen

Beide Mechanismen sind eng miteinander verknüpft, verfolgen jedoch unterschiedliche Ziele.

### Verlinken von Seiten und Abschnitten

Über einer Überschrift kann durch den Syntax `(<Anker>)=` ein Anker gesetzt werden, der anschließend verlinkt werden kann. Der Verweis erfolgt dann über den Ankernamen.

```{code-block} markdown
:caption: Anker für Seiten und Abschnitte setzen
:linenos:

(Inhalte Verlinken)=
## Inhalte Verlinken

siehe Abschnitt {ref}`Inhalte Verlinken`
```

> siehe Abschnitt {ref}`Inhalte Verlinken`

```{note}
Anker sollten **sprechende, stabile Namen** besitzen\
(z. B. `fig-venv`, `eq-schwingung`, `sec-layout`).
```

(Globale Nummerierung von Objekten)=
## Globale Nummerierung von Objekten

Sphinx erlaubt es, **Abbildungen**, **Tabellen** und **Codeblöcke** automatisch zu nummerieren. Diese Nummerierung erfolgt **global für das gesamte Dokument** und ist unabhängig von der jeweiligen Inhaltsseite.

Die Konfiguration der Nummerierung erfolgt zentral in der Datei `conf.py`.

```{code-block} python
:caption: Globale Nummerierung aktivieren
:linenos:

# -- Layout- und Stilmittel -------------------------------------------------
# Nummerierung von Bidern, Tabellen und Codeblöcken
numfig = True # Nummerierung von Bildern Tabellen etc. aktivieren

numfig_format = {               # Benennung von Abbildung -> Abb, Tabelle -> Tab, etc. ändern
    "figure": "Abb. %s:",       # Bilder: Bsp.: Abb. 1:
    "table": "Tab. %s:",        # Tabellen: Bsp.: Tab. 1:
    "code-block": "Code %s:"    # Codeblöcke: Bsp.: Code 1:
}
```

Mit dieser Konfiguration erhalten alle **Abbildungen**, **Tabellen** und **Codeblöcke** eine fortlaufende Nummerierung. Die Bezeichnungen werden dabei bewusst an die im deutschsprachigen, wissenschaftlichen Kontext üblichen Abkürzungen angepasst.

## Referenzieren von Abbildungen, Tabellen und Codeblöcken

### Abbildungen (`figure`)

Eine Abbildung wird mit einem expliziten Namen versehen, um sie verlinken zu können.

````{code-block} markdown
:caption: Abbildungen referenzieren
:linenos:

```{figure} ../../_static/img/Logo/Logo-black.png
:width: 40%
:align: center
:name: logo

Logo
```

siehe {numref}`logo`
````

```{admonition} Gerendertes Ausgabe
:class: note

```{figure} ../../_static/img/Logo/Logo-black.png
:width: 40%
:align: center
:name: logo

Logo
```

siehe {numref}`logo`

- `{numref}` erzeugt **nummerierte Verweise**
- `{ref}` würde lediglich den Titel referenzieren.


### Tabellen (`table`)

Analog zu Abbildungen

````{code-block} markdown
:caption: Abbildungen referenzieren
:linenos:

```{table} Parameter der Schwingung
:name: tab-parameter
:align: center

| Parameter | Bedeutung |
|----------|-----------|
| $a$        | Amplitude |
| $\omega$        | Kreisfrequenz |
```

siehe {numref}`tab-parameter`
````

````{admonition} Gerendertes Ausgabe
:class: note

```{table} Parameter der Schwingung
:name: tab-parameter
:align: center

| Parameter | Bedeutung |
|----------|-----------|
| $a$        | Amplitude |
| $\omega$        | Kreisfrequenz |
```

siehe {numref}`tab-parameter`
````

### Codeblöcke (`code-block`)

Auch Codeblöcke können referenziert werden:

````{code-block} markdown
:caption: Abbildungen referenzieren
:linenos:

```{code-block} python
:name: code-fft
:caption: fft

def fft(x):
    ...
```

siehe {numref}`code-fft`
````

````{admonition} Gerendertes Ausgabe
:class: note

```{code-block} python
:name: code-fft
:caption: fft

def fft(x):
    ...
```

siehe {numref}`code-fft`
````

### Referenzieren von Formeln

Für mathematische Ausdrücke wird ein explizites Label gesetzt

````{code-block} markdown
:caption: Formeln referenzieren
:linenos:

```{math}
:label: eq-energie

E = mc^2
```

siehe Gleichung {eq}`eq-energie`
````



```{math}
:label: eq-energie

E = mc^2
```

siehe Gleichung {eq}`eq-energie`


Sphinx erzeugt dabei automatisch `(1)`.

```{note}
Die Referenzierung von Gleichungen erfolgt über `{eq}`,\
nicht über `{numref}` oder `{ref}`.

Die Formeln sollten nicht mit Dollarmath definiert werden. Dies kann unter Umständen zum nicht erkennen des Labels führen.
```

## Unterschiede der Referenztypen

```{list-table} Unterschiede der Referenztypen
:align: center
:header-rows: 1

* - Typ
  - Zweck
* - `{ref}`
  - Abschnitts- oder Objektverweise
* - `{numref}`
  - nummerierte Objekte (Abb., Tab., Code)
* - `{eq}`
  - mathematische Gleichungen
```

```{tip}
- Text & Struktur $\rightarrow$ `{ref}`
- Nummerierte Objekte $\rightarrow$ `{numref}`
- Gleichungen $\rightarrow$ `{eq}`
```