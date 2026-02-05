# Mathematik

Sphinx unterstützt mathematische Notation vollständig über **LaTeX-Syntax**, die zur Laufzeit durch **MathJax** im Browser gerendert wird. Dabei wird zwischen **Inline-Mathematik** und **abgesetzten Formelblöcken** unterschieden.

(Konfiguration MathJax)=
## Konfiguration

Damit alle im folgenden beschriebenen Funktionen zuverlässig arbeiten, sind die folgenden Einstellungen in der `conf.py` erforderlich:

```{code-block} python
:caption: Konfiguration von MathJax
:linenos:

# -- MathJax ----------------------------------------------------------------
# Optionen speziell für die Mathe-Verarbeitung (dollarmath/amsmath)
extensions.append("sphinx.ext.mathjax")           # MathJax für Matheformeln

myst_dmath_allow_labels = True  # erlaubt \label{} und \ref{} innerhalb von $$...$$
myst_dmath_allow_space  = True  # erlaubt $x = y$ auch mit Leerzeichen nach dem ersten $
myst_dmath_allow_digits = True  # erlaubt $3x$ (Ziffer direkt nach $) statt Fehler

mathjax3_config = {
    "loader": {"load": ["[tex]/color"]},
    "tex": {
        "packages": {"[+]": ["color"]},
        "macros": {
            "red":    ["{\\color[RGB]{214,39,40} #1}", 1],     # D62728
            "blue":   ["{\\color[RGB]{31,119,180} #1}", 1],    # 1F77B4
            "green":  ["{\\color[RGB]{44,160,44} #1}", 1],     # 2CA02C
            "orange": ["{\\color[RGB]{255,127,14} #1}", 1],    # FF7F0E
            "purple": ["{\\color[RGB]{148,103,189} #1}", 1],   # 9467BD
            "cyan":   ["{\\color[RGB]{23,190,207} #1}", 1],    # 17BECF
            "teal":   ["{\\color[RGB]{42,161,152} #1}", 1],    # 2AA198
            "gray":   ["{\\color[RGB]{110,110,110} #1}", 1],   # 6E6E6E
        },
        "inlineMath": [
            ["$", "$"],       # $ ... $ als Inline-Math
            ["\\(", "\\)"],   # \( ... \) ebenfalls
        ],
        "displayMath": [
            ["$$", "$$"],     # $$ ... $$ als Display-Math
            ["\\[", "\\]"],   # \[ ... \] ebenfalls
        ],
    },
}
```

Diese Optionen sorgen dafür, dass:
- MathJax generell aktiviert wird,
- Gleichungen sauber referenzierbar sind,
- natürlich geschriebene Mathematik nicht zu Parserfehlern führt,
- wir später Gleichungen {ref}`Einfärben <Einfärben mathematischer Ausdrücke>` können
- und PDFs sauber aussteuern können.

## Inline-Mathematik

Inline-Mathematik wird verwendet, um kurze mathematische Ausdrücke innerhalb eines Fließtexts darzustellen.

```{code-block} markdown
:caption: Inline-Mathematik
:linenos:

Die Energie ist gegeben durch $E = mc^2$.
```

Gerendert erscheint der Ausdruck direkt im Textfluss:
> Die Energie ist gegeben durch $E = mc^2$.

Inline-Mathematik eignet sich für:

- einzelne Variablen,
- kurze Formeln,
- mathematische Symbole im Satz.

```{note}
Inline-Mathematik sollte **sparsam** eingesetzt werden.\
Längere oder strukturierte Ausdrücke beeinträchtigen die Lesbarkeit und gehören in einen Formelblock.
```

## Abgesetzte Formelblöcke mit $$ ... $$

Für größere mathematische Ausdrücke oder Gleichungen wird Display-Math verwendet. In MyST-Markdown geschieht dies über doppelte Dollarzeichen:

```{code-block} markdown
:caption: Abgesetzte Formelblöcke ($$)
:linenos:

$$
E = mc^2
$$
```

Diese Schreibweise erzeugt eine zentrierte, eigenständige Gleichung.

````{admonition} Gerendertes Ausgabe
:class: note

$$E = mc^2$$
```` 

## Die `math`-Direktive

Neben der Dollar-Syntax unterstützt Sphinx explizit die math-Direktive:

````{code-block} markdown
:caption: math-Direktive
:linenos:

```{math}
E = mc^2
```
````

````{admonition} Gerendertes Ausgabe
:class: note

```{math}
E = mc^2
```
````

Diese Schreibweise ist funktional äquivalent zu `$$ ... $$`, bietet jedoch:

- klarere Semantik,
- bessere Lesbarkeit im Quelltext,
- saubere Abgrenzung in komplexen Dokumenten.

Für umfangreiche mathematische Abschnitte ist die `{math}`-Direktive die robustere Wahl.

### Mehrzeilige Formeln und `align`

Für mehrere Gleichungen oder Ausrichtung an Gleichheitszeichen kann die LaTeX-Umgebung `align` genutzt werden:

````{code-block} markdown
:caption: math-Direktive
:linenos:

```{math}
\begin{align}
E &= mc^2 \\
\sqrt{x^{2} + y^{2}} &= r
\end{align}
```
````

Dabei gilt:

- `&` markiert die Ausrichtungsstelle,
- `\\` erzeugt einen Zeilenumbruch.

Diese Form ist besonders geeignet für Herleitungen und Systeme von Gleichungen.

````{admonition} Gerendertes Ausgabe
:class: note

```{math}
\begin{align}
E &= mc^2 \\
\sqrt{x^{2} + y^{2}} &= r
\end{align}
```
````

(Einfärben mathematischer Ausdrücke)=
## Einfärben mathematischer Ausdrücke

Im Abschnitt {ref}`Konfiguration MathJax` haben wir bereits Farben definiert, die der **Standardfarbpalette von Matplotlib** entsprechen. Diese Liste ist beliebig erweiterbar.

Das Einfärben von Formeln ist besonders nützlich, um:

- Variablen hervorzuheben,
- Terme zu unterscheiden,
- didaktische Akzente zu setzen.

Die Farben können direkt in mathematischen Ausdrücken genutzt werden:

```{code-block} markdown
:caption: eingefärbte Formel
:linenos:

$$
E = \red{m} \blue{c}^2
$$
```

$$E = \red{m} \blue{c}^2$$

Oder in Inline-Mathematik:

```{code-block} markdown
:caption: eingefärbte Inline-Mathematik
:linenos:

Die Masse $\green{m}$ bestimmt die Energie.
```

> Die Masse $\green{m}$ bestimmt die Energie.

## Lokale Einbindung von MathJax

Für die Darstellung mathematischer Ausdrücke in Sphinx wird wie eingangs beschrieben standardmäßig **MathJax** verwendet. In der Voreinstellung bindet Sphinx MathJax über ein externes **Content Delivery Network** (*CDN*) ein.\
Ein CDN ist ein verteiltes Netz aus Servern, das dazu dient, statische Webinhalte (z.B. JavaScript-Bibliotheken, Stylesheets oder Bilder) effizient an Endnutzer auszuliefern. Statt Inhalte ausschließlich von einem zentralen Ursprungsserver bereitzustellen, werden identische Kopien auf weltweit verteilten Servern zwischengespeichert und von dort ausgeliefert.

Für viele Anwendungsfälle ist dies ausreichend, jedoch nicht optimal, wenn Reproduzierbarkeit, Offline-Nutzung oder Datenschutz eine Rolle spielen.

Eine lokale Einbindung von MathJax bietet mehrere Vorteile:
- **Reproduzierbarkeit**: Die Dokumentation ist unabhängig von externen Servern und Versionsänderungen.
- **Offline-Fähigkeit**: Die HTML-Dokumentation funktioniert vollständig ohne Internetverbindung.
- **Langzeitstabilität**: Die Darstellung mathematischer Formeln bleibt über Jahre konsistent.
- **Datenschutz & Compliance**: Es werden keine externen Ressourcen nachgeladen.

Besonders das Laden externer Ressourcen über CDNs ist aus datenschutzrechtlicher Sicht problematisch, da bereits beim Laden einzelner Ressourcen eine **Datenübertragung an Dritte** stattfindet.

Zentrale Punkte sind:

- **IP-Adressen gelten als personenbezogene Daten**\
    Nach der DSGVO können IP-Adressen eine Identifizierung von Personen ermöglichen und unterliegen daher dem Datenschutzrecht.
- **Unkontrollierte Datenverarbeitung**\
    Als Website-Betreiber besteht kein direkter Einfluss darauf,
    - welche Daten gespeichert werden,
    - wie lange sie gespeichert werden,
    - in welchen Ländern die Verarbeitung erfolgt.
- **Drittstaatentransfers**\
    Viele große CDN-Anbieter betreiben Server außerhalb der EU. Damit kann es zu Datenübertragungen in Länder kommen, die kein angemessenes Datenschutzniveau gewährleisten.
- **Fehlende informierte Einwilligung**\
    CDN-Ressourcen werden häufig bereits beim Seitenaufruf geladen, bevor Nutzer eine Einwilligung erteilen können.

Aus diesen Gründen sollte spätestens bei der {ref}`Veröffentlichung <Sphinx Veröffentlichen>` der Sphinx-Dokumentation eine lokale Einbindung von MathJax erfolgen.

### Technische Umsetzung

**1. Downloaden von MathJax**

Um MathJax lokal in Sphinx verwenden zu können, muss es zunächst heruntergeladen werden. Dies kann entweder über **npm** (*Node Package Manager*) geschehen oder über die dazugehörige Website und deren Datenbank:\
[https://www.npmjs.com/package/mathjax](https://www.npmjs.com/package/mathjax)

**npm** ist das **zentrale Paket- und Distributionssystem für JavaScript-Software**. Es erfüllt eine ähnliche Rolle wie **pip** im **Python-Ökosystem**, wobei die zugehörige Paketdatenbank über die Website [npmjs.com](https://www.npmjs.com) zugänglich ist.

Auf [https://www.npmjs.com/package/mathjax](https://www.npmjs.com/package/mathjax) sind unter dem Reiter **Versions** alle bisher entwickelten Versionen (auch Testversionen) hinterlegt. Hier kann nun die gewünschte Version ausgewählt werden.\
Sphinx verwendet jedoch MathJax ausschließlich zur **Client-seitigen Darstellung** mathematischer Formeln im Browser. Dafür ist **MathJax 3.x** die empfohlene Version, aus folgenden Gründen:

- **Modulare Architektur**: deutlich kleinerer und schneller ladender Code
- **Verbesserte Performance** gegenüber MathJax 2.x
- **Aktive Wartung** (2.x gilt als veraltet)
- **Stable-Ökosystem** (4.x befindet sich derzeit in einer grundlegenden Umstrukturierung und ist zum aktuellen Zeitpunkt weder breit etabliert noch offiziell von Sphinx unterstützt)
- **Explizite Unterstützung durch Sphinx** (Standardkonfigurationen zielen auf 3.x)

Für neue Dokumentationen ist MathJax 3.x daher Stand der Technik und faktisch gesetzt.

Über die Version kann nun die **komprimierte Archivdatei** (`.tgz`) geladen werden.\
Beispiel für Version 3.2.2: [https://registry.npmjs.org/mathjax/-/mathjax-3.2.2.tgz](https://registry.npmjs.org/mathjax/-/mathjax-3.2.2.tgz)

Die URL setzt sich dabei zusammen aus:

- `registry.npmjs.org` $\rightarrow$ zentrale npm-Registry
- `mathjax` $\rightarrow$ Paketname
- `3.2.2` $\rightarrow$ konkrete, fest versionierte Veröffentlichung
- `.tgz` $\rightarrow$ Distributionsarchiv (kurzform für `.tar` und `.gz`)

Dieser Link ist **keine Webseite**, sondern ein direkter, versionsspezifischer Download.

**2. Entpacken und Ablegen von MathJax**

Die nun geladene verpackte Datei (hier: `mathjax-3.2.2`) kann nun mit gängigen Mitteln (Windows: 7-Zip, Mac: Doppelklick) entpackt werden.\
Der entpackte Ordner sollte nun die folgende Struktur aufweisen:
```{code-block} none
:caption: Ordnerstruktur mathjax-3.x.x.tar
:emphasize-lines: 2

package
├ es5
│ └ ...
├ LICENSE
├ package.json
└ README.md
```

In der Praxis genügt es, ausschließlich den Ordner `es5` zu übernehmen, da dieser die für den Browser optimierten Builds enthält.\
Hierfür muss dieser in den `_static`-Ordner des Sphinx-Projekts verschoben werden.

```{code-block} none
:caption: es5-Ordner in Sphinx-Projekt ablegen
:emphasize-lines: 7

Sphinx-Projekt
├ build
├ source
│ ├ _static
│ │ └ js
│ │   └ mathjax
│ │     └ es5
│ ├ _templates
│ ├ conf.py
│ └ index.rst
├ make.bat
└ Makefile
```

**3. Einbindung von MathJax in `conf.py`**

Nachdem MathJax lokal im Projekt abgelegt wurde, muss Sphinx explizit mitgeteilt werden, welche MathJax-Datei beim Rendern der HTML-Dokumentation zu laden ist.\
Dies geschieht über die Konfigurationsvariable `mathjax_path` in der Datei `conf.py`.

Der angegebene Pfad wird dabei relativ zum statischen Verzeichnis (`html_static_path`) interpretiert und in die erzeugten HTML-Seiten eingebunden.

Voraussetzung ist, dass der Ordner `_static` in der Konfiguration registriert ist (sollte der Fall sein):

```{code-block} python
:caption: _static-Ordner registrieren
:linenos:

html_static_path = ["_static"]
```

Anschließend kann der Pfad zur lokal abgelegten **MathJax-Datei** gesetzt werden:\
(vorzugsweise im Abschnitt der sonstigen Konfiguration von MathJax)

```{code-block} python
:caption: lokales MathJax einbinden
:linenos:

mathjax_path = "js/mathjax/es5/tex-chtml-full.js"  # lokales MathJax
```

Die Datei `tex-chtml-full.js` enthält den **vollständigen TeX-Parser** sowie den **HTML-CSS-Renderer** und deckt damit den üblichen Funktionsumfang für mathematische Formeln in Sphinx vollständig ab.\
Beim Erzeugen der HTML-Dokumentation bindet Sphinx MathJax nun **lokal aus dem Projektverzeichnis** ein. Es werden **keine** externen Server kontaktiert und **keine** zusätzlichen Netzwerkanfragen ausgelöst.