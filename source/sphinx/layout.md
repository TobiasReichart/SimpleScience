# Layout, Themes & Design

Hier soll es nun um die Darstellung unserer Sphinx-Dokumentation gehen. Es sollen Theme-Auswahl, Design-Optionen, eigene CSS/JS-Dateien, Templates sowie grundlegende MyST/Sphinx-Mechaniken, die für das Layout relevant sind behandelt werden.\
Ziel ist eine **konsistente**, **wartbare und publikationsfähige** Oberfläche, die sowohl für die lokale Entwicklung als auch für den späteren Deploy (z.B. GitHub Pages) einsetzbar ist.

## Theme Konzept

Ein **Theme** beschreibt in Sphinx die Gesamtheit aus:

- HTML-Struktur (Templates),
- CSS (Layout, Typografie, Farben),
- optional JavaScript (Navigation, Suchverhalten, Interaktion),
- sowie theme-spezifische Konfigurationen in `conf.py`.

Damit entscheidet das Theme nicht nur über "Farben", sondern über zentrale UX-Eigenschaften wie:

- Navigationsstruktur und Verhalten (z. B. einklappende Menüs),
- Breite des Inhaltsbereichs,
- Darstellung von Codeblöcken und Hinweisboxen,
- Responsivität auf kleinen Bildschirmen.

```{note}

Ein Theme ist eine **Darstellungsschicht**.\
Inhalte (`.md` / `.rst`) bleiben unverändert. Das Theme definiert lediglich, **wie** sie gerendert werden.
```

## Read-the-Docs Theme

Das Theme **Read-the-Docs** wurde bereits eingang im Abschnitt {ref}`Theme anpassen` für die aktuelle Dokumentation gesetzt. Es eignet sich hervorragend für technische Dokumentationen oder Lehrmaterial.

(theme-optionen)=
### Theme-Optionen

Themes bieten häufig zusätzliche Optionen, die über `html_theme_options` konfiguriert werden. Diese Optionen steuern das Verhalten der Navigation, die Tiefe der Menüstruktur und teilweise Layout-Details.\
Eine ausführliche Beschreibung aller Funktionen, die das Theme bietet, findet sich unter dem folgenden Link:\
[https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html](https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html)

Es bietet sich an, diese Einstellungen unter der Variable `html_theme` vorzunehmen.\
In diesem Projekt wurden die folgenden Einstellungen gesetzt:

```{code-block} python
:caption: Theme-Optionen (Read the Docs)
:linenos:

# -- Theme Einstellungen -----------------------------------------------------
html_theme = "sphinx_rtd_theme" # default: "alabaster"

html_theme_options = {
    "collapse_navigation": False,               # Navigationsmenüs nicht einklappen
    "navigation_depth": -1,                     # alle Ebenen anzeigen (-1 = unbegrenzt)
    "sticky_navigation": False,                 # Navigation scrollt nicht mit
    "includehidden": True,                      # Hidden toctree-Einträge anzeigen
    "prev_next_buttons_location": "bottom",     # Position der Navigationsbuttons
    "style_nav_header_background": "#2980B9", # Hintergrundfarbe der Kopfzeile
    "style_external_links": True,               # Externe Links markieren
    "body_max_width": "none",                   # HTML-Layout auf Bildschirmbreite skalieren
}

html_show_sourcelink = False  # Quelltext-Button ausblenden
html_css_files = []           # Liste für eigene Styles
```

- `collapse_navigation` Steuert, ob Navigationspunkte standardmäßig eingeklappt werden\
  `True` $\rightarrow$ Alle Ebenen der Navigation bleiben sichtbar\
  `False` $\rightarrow$ Unterpunkte werden standardmäßig verborgen und erst bei Interaktion sichtbar
- `navigation_depth` Legt fest, wie viele Ebenen der Dokumentationshierarchie in der Navigation angezeigt werden\
  positive Zahl (`1`, `2`, `3`, …): maximale Tiefe\
  `-1`: unbegrenzte Tiefe
- `sticky_navigation` Steuert, ob die Navigationsleiste beim Scrollen "mitwandert"\
  `True` $\rightarrow$ Navigation bleibt immer sichtbar\
  `False` $\rightarrow$ Navigation scrollt normal mit dem Dokument
- `includehidden` bestimmt, ob Toctree-Einträge mit `:hidden:` dennoch in der Navigation erscheinen\
  `True` $\rightarrow$ Auch versteckte Toctrees tauchen in der Navigation auf\
  `False` $\rightarrow$ Versteckte Toctrees bleiben vollständig unsichtbar
- `prev_next_buttons_location` Legt die Position der „Zurück“-/„Weiter“-Buttons fest\
  "top", "bottom", "both", None (deaktiviert)
- `style_nav_header_background` Setzt die Hintergrundfarbe der oberen Navigationskopfzeile\
  akzeptiert alle gültigen CSS-Farbwerte
- `style_external_links` Markiert externe Links visuell\
  `True` $\rightarrow$ externe Links werden kenntlich gemacht\
  `False` $\rightarrow$ externe und interne Links erscheinen gleich
- `body_max_width` Steuert die maximale Breite des Inhaltsbereichs\
  Standard: feste Maximalbreite\
  "none": volle Browserbreite
- `html_show_sourcelink` Blendet den „View page source“-Link aus\
  `True` $\rightarrow$ kein Quelltext-Link\
  `False` $\rightarrow$ Link zur reST/Markdown-Quelle sichtbar
- `html_css_files` Liste eigener CSS-Dateien, die zusätzlich eingebunden werden (bewusst leer initialisiert)


```{hint}

Theme-Optionen sind **theme-spezifisch**.\
Wenn später ein anderes Theme verwendet wird, kann ein Teil dieser Optionen wirkungslos werden oder andere Namen besitzen.\
Für eine langfristig stabile Dokumentation sollten **kritische Layout-Regeln** eher über eigene CSS-Dateien gesteuert werden.
```

## Hinweisboxen

Hinweisboxen (engl. *Admonitions*) sind strukturierte Hervorhebungen, die Inhalte gezielt einordnen. Sie trennen **Kernaussagen** vom Kontext, markieren **Warnungen** oder geben **praktische Tipps**. Sie sind ein zentrales Stilmittel, um Lesefluss und Verständlichkeit zu erhöhen.\
Sphinx unterstützt sowohl vordefinierte Box-Typen (z.B. `note`, `warning`) als auch frei benannte Boxen über `admonition`.

### Standard-Boxen und ihre Bedeutung

Die am häufigsten verwendeten Boxen sind:

- `note` $\rightarrow$ sachliche Zusatzinformation / Einordnung
- `tip` $\rightarrow$ praktischer Hinweis, Best Practice
- `hint` $\rightarrow$ sanfter Hinweis (oft kleiner als tip)
- `warning` $\rightarrow$ wichtige Warnung, potenzielles Fehlverhalten
- `caution` $\rightarrow$ ähnlich warning, oft etwas „weicher“
- `error` $\rightarrow$ klarer Fehlerzustand oder zwingendes Problem
- `important` $\rightarrow$ hoher Stellenwert, unbedingt beachten
- `attention` $\rightarrow$ starke Hervorhebung, z. B. Sicherheitsaspekt

Um eine Hinweisbox zu verwenden muss ein **fenced code blocks** verwendet werden, wobei die Variable `<Type>` mit dem gewünschten Box-Typ ersetzt werden muss.

````{code-block} markdown
:caption: Syntax der Hinweisboxen
:linenos:

```{<Type>}

Das ist der Inhalt der Hinweisbox.
```
````

```{figure} ../_static/img/sphinx/layout/hinweisbox-standard.png
:align: center
:width: 100%

Hinweisbox <Type> = attention
```

### Eigenen Titel setzen

Standardboxen haben bereits einen Titel (z.B. "Hinweis", "Warnung").\
Wenn wir einen **eigenen Titel** möchten, kann statt dem gewünschten Type der Hinweisbox für die Variable `<Type>`, `admonition` gesetzt werden.

````{code-block} markdown
:caption: Admonition mit eigenem Titel
:linenos:

```{admonition} Einordnung
:class: note

Dieser Text nutzt den Stil von `note`, trägt aber einen eigenen Titel.
```
````

```{figure} ../_static/img/sphinx/layout/hinweisbox-eigene-titel.png
:align: center
:width: 100%

Hinweisbox mit eigenem Titel nach dem Style von note
```

Wichtig ist hier das Prinzip:

- `admonition` bestimmt den **Titel**
- `:class:` bestimmt den **Style-Typ** (z.B. `note`, `warning`, `tip`)

Damit können wir sehr präzise formulieren, *warum* etwas wichtig ist, ohne auf generische Überschriften angewiesen zu sein.

### Styling der Hinweisboxen bearbeiten.

Standard-Themes liefern bereits ein funktionales Design. In der Praxis lohnt es sich jedoch, die Boxen optisch an das eigene Layout anzupassen. So können beispielsweise abgerundete Ecken realisiert werden.

Sphinx erzeugt Hinweisboxen im HTML als Container mit CSS-Klassen wie:

- `div.admonition` (*Basisklasse* für alle Boxen)
- `div.admonition.note`, `div.admonition.warning`, `div.admonition.tip`, … (*spezifische Typen*)

Damit lassen sich Boxen entweder:

- **global** (alle Typen gleichzeitig) oder
- **selektiv** (nur bestimmte Boxarten)

über CSS anpassen.

**1. CSS-Datei anlegen und ablegen**

Eigene Styles sollten in Sphinx immer im statischen Verzeichnis `_static` liegen, da dieses beim Build automatisch in die HTML-Ausgabe übernommen wird.

Empfohlene Struktur:

```{code-block} none
:caption: Typischer Ablageort für das favicon.ico
:emphasize-lines: 6

Sphinx-Projekt
├ build/
└ source/
  ├ _static
  │ └ style/
  │   └ hinweisboxen_layout.css
  ├ conf.py
  └ index.md
```

Diese Trennung ist nicht zwingend, erhöht aber die Wartbarkeit, da alle Style-Anpassungen gesammelt in einem definierten Ordner liegen.


**2. CSS-Regeln definieren**

In der `hinweisboxen_layout.css` fügen wir zunächst folgende Basisregeln ein:

```{code-block} css
:caption: Einheitlicher Rahmen und Rundungen für Hinweisboxen
:linenos:

div.admonition {
  border-radius: 5px;              /* alle Ecken (oben & unten) abrunden */
  overflow: hidden;                /* Inhalt an die Rundung "anpassen" */
  border: 1px solid rgba(0,0,0,.08);
}
```

- `border-radius: 5px;`\
  Rundet die Ecken der Hinweisbox mit einem Radius von `5px` ab.
- `overflow: hidden;`\
  Verhindert, dass Inhalte innerhalb der Box (z.B. der Titelbereich oder Hintergrundflächen) über die abgerundeten Ecken hinausragen.\
  Diese Zeile ist besonders wichtig, weil Themes häufig eigene Hintergründe oder Titelbalken verwenden. Ohne `overflow: hidden` kann es passieren, dass die Box "rund" ist, der Inhalt aber an den Ecken weiterhin "kantig" sichtbar bleibt.
- `border: 1px solid rgba(0,0,0,.08);`\
  Zeichnet einen sehr dezenten Rahmen.

```{note}

Diese Änderung verändert ausschließlich die **Darstellung** der Boxen.\
Die semantische Funktion (`note`, `warning`, `tip`, …) bleibt vollständig erhalten.
```

**3. CSS-Datei in `conf.py` einbinden**

Damit Sphinx die CSS-Datei beim HTML-Build lädt, muss sie in `conf.py` registriert werden.\
Hierfür kann die CSS-Datei einfach in die unter {ref}`theme-optionen` initialisierte `html_css_files` Liste eingehängt werden

```{code-block}
:caption: Hinweisbox CSS in html_css_files-Liste einhängen
:linenos:

html_css_files.append("style/hinweisboxen_layout.css") # Anpassen des HTML-Styles der Hinweisboxen
```

Dabei ist zu beachten, dass der Pfad `"style/hinweisboxen_layout.css"` relativ zu `_static` ist.

Nach dem nächsten Build (oder nach dem Speichern bei aktivem `sphinx-autobuild`) sollten alle Hinweisboxen sichtbar verändert sein.

```{important}

Hinweisbox mit abgerundeten Ecken
```

## Direktiven

In MyST-Markdown werden Sphinx-Direktiven ebenfalls mit **fenced code blocks** geschrieben. Eine Direktive beginnt dabei mit drei Backticks und wird ebenfalls mit drei Backticks beendet:

````{code-block} markdown
:caption: Direktiven in MyST-Markdown
:linenos:

```{figure}
...
```
````

**Grundregel**

- **Öffnen** einer Direktive: ` ``` `  
- **Schließen** derselben Direktive: ` ``` `

Der gesamte Inhalt zwischen diesen Markierungen gehört zur Direktive. Dabei muss für das Öffnen und Schließen einer Direktive immer die gleiche Anzahl an Backticks verwendet werden.

### Verschachtelte Direktiven

Sollen **Direktiven ineinander verschachtelt** werden (z.B. eine `figure` innerhalb einer `only`-Direktive), müssen **mehr Backticks** verwendet werden, um die Ebenen eindeutig zu trennen.

Beispiel:

`````{code-block} markdown
:caption: Verschachtelte Direktiven
:linenos:

````{only} html
```{figure} ../_static/img/example.svg
:width: 80%
```
```` 
`````

Dabei gilt die zentrale Regel:\
**Jede äußere Ebene benötigt mehr Backticks als die innere Ebene.**

- innere Direktive: drei Backticks
- nächste Direktive: vier Backticks
- nächste Direktive: fünf Backticks
- usw.

Wichtig zu beachten ist, dass die Direktiven auch in der Reihenfolge geschlossen werden müssen, in der sie geöffnet wurden.\
So kann MyST eindeutig erkennen, wo eine Direktive beginnt und endet.

```{admonition} Merkhilfe
:class: tip

Je tiefer eine Direktive verschachtelt ist, desto **mehr Backticks** werden benötigt.\
Geöffnet und geschlossen wird immer mit **derselben Anzahl** an Backticks.
```

(Optionen von Direktiven)=
### Optionen von Direktiven

Der `:option:`-Parameter

Viele Sphinx-Direktiven, darunter auch `figure`, `table` oder `code-block` unterstützen Optionen, mit denen das Verhalten und die Darstellung des jeweiligen Objekts gesteuert werden.\
Optionen werden unmittelbar nach der Direktive angegeben und besitzen die allgemeine Form:

```{code-block} markdown
:caption: Optionen in Direktiven
:linenos:

:option: wert
```

Am Beispiel der `figure`-Direktive:

````{code-block} markdown
:caption: Beispielhafte Verwendung von Optionen in der figure-Direktive
:linenos:

```{figure} ../_static/img/mermaid/venv.svg
:width: 90%
:align: center
:name: fig-venv

Virtuelle Python-Umgebung
```
````
Dabei gilt:

- jede Option steht in einer **eigenen Zeile**,
- Optionen beginnen immer mit einem **Doppelpunkt**,
- die Reihenfolge der Optionen ist **beliebig**,
- nicht gesetzte Optionen verwenden **Standardwerte**.

```{note}

Welche Optionen verfügbar sind, hängt von der jeweiligen Direktive ab.\
Nicht jede Direktive unterstützt dieselben Parameter.
```

## Favicon der Dokumentation

Ein Favicon ist ein kleines Symbol, das von Webbrowsern unter anderem in:

- der Tab-Leiste,
- der Lesezeichenansicht,
- sowie in der Browser-Historie

angezeigt wird.\
Es dient der visuellen Identifikation einer Website.

Auch wenn ein Favicon keinen inhaltlichen Beitrag leistet, trägt es wesentlich zu einem professionellen Gesamteindruck bei.

### Ablageort statischer Ressourcen

In Sphinx werden statische Dateien wie Bilder, Stylesheets oder Icons im Verzeichnis `_static` abgelegt. Dieses Verzeichnis wird beim HTML-Build automatisch eingebunden und in die Ausgabestruktur übernommen.

```{code-block} none
:caption: Typischer Ablageort für das favicon.ico
:emphasize-lines: 5

Sphinx-Projekt
├ build/
└ source/
  ├ _static
  │ ├ favicon.ico
  │ ├ img
  │ └ style
  ├ conf.py
  └ index.md
```

Das Favicon wird dabei **nicht direkt** im Dokument **referenziert**, sondern zentral über die Sphinx-Konfiguration eingebunden.

```{hint}

Für die Erstellung einer `.ico`-Datei ist im Abschnitt **Werkzeuge & Methoden** der Programmcode eines eigenen kleinen ico-Converters gezeigt und die Programmierung beschrieben.\
siehe: {ref}`ico-converter`
``` 

### Einbindung des Favicons in `conf.py`

Die Einbindung erfolgt über die Variable `html_favicon` in der Datei `conf.py`.\
Es bietet sich an, die Variable `html_favicon` direkt unter der bereits vorhandenen Variable `html_static_path` zu platzieren.

```{code-block} python
:caption: Favicon in der conf.py verlinken
:linenos:

html_static_path = ["_static"]
html_favicon = "_static/favicon.ico"
```

Dabei ist zu beachten:

- der Pfad ist relativ zum `source`-Verzeichnis,
- gängige Formate sind `.ico`, `.png` oder `.svg`,
- das Favicon wird ausschließlich in **HTML-Ausgaben** verwendet.

Beim nächsten HTML-Build wird das Icon automatisch in den `<head>`-Bereich jeder Seite eingebunden.

---

Nach einem erfolgreichen Build erscheint das Favicon:

- im Browser-Tab neben dem Seitentitel,
- in gespeicherten Lesezeichen,
- in der Verlaufsliste des Browsers.

```{hint}

Änderungen am Favicon werden von Browsern häufig **stark gecacht**.\
Wird ein neues oder geändertes Favicon nicht angezeigt, kann es erforderlich sein,

- den Browser-Cache zu leeren,
- die Seite mit einem **Hard Reload** neu zu laden\
  (z. B. {kbd}`Strg` + {kbd}`F5` unter Windows/Linux oder {kbd}`Cmd` + {kbd}`Shift` + {kbd}`R` unter macOS),
- oder die Seite testweise in einem **privaten Browserfenster** zu öffnen.

Das Verhalten ist browserabhängig und stellt keinen Fehler der Sphinx-Konfiguration dar.
```