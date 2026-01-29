# Mathematik

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