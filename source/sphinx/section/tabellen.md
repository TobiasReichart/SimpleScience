# Tabellen

Tabellen dienen der strukturierten Darstellung diskreter Informationen.\
Typische Anwendungsfälle sind:

- Parameterübersichten
- Vergleichstabellen
- Mess- und Ergebnisdarstellungen
- Klassifikationen oder Zuordnungen

Sphinx unterstützt mehrere Tabellentypen, die sich in **Komplexität**, **Lesbarkeit im Quelltext** und **Gestaltungsfreiheit** unterscheiden. Die Wahl der passenden Tabellenform ist daher kein Stil-, sondern ein konzeptioneller Entwurfsschritt.

## Einfache Tabellen mit `list-table`

Für die meisten Dokumentationen ist die `list-table`-Direktive die empfohlene Standardlösung.\
Sie ist gut lesbar im Quelltext, stabil im HTML- und PDF-Export und ausreichend flexibel für typische Anwendungsfälle.

````{code-block} markdown
:caption: Einfache Tabelle mit list-table
:linenos:

```{list-table} Parameterübersicht
:align: center
:header-rows: 1

* - Parameter
  - Bedeutung
  - Einheit
* - $a$
  - Amplitude
  - m
* - $\omega$
  - Kreisfrequenz
  - rad/s
```
````

Eigenschaften:

- jede Tabellenzeile beginnt mit `*`
- Spalten werden mit `-` getrennt
- `:align:` richtet die Tabelle aus (left, center, right)
- `:header-rows:` definiert Kopfzeilen
- die erste Zeile nach der Direktive ist die **Caption**

Nur Tabellen mit Caption werden nummeriert und können über `{numref}` referenziert werden.

````{admonition} Gerendertes Ausgabe
:class: note

```{list-table} Parameterübersicht
:align: center
:header-rows: 1

* - Parameter
  - Bedeutung
  - Einheit
* - $a$
  - Amplitude
  - m
* - $\omega$
  - Kreisfrequenz
  - rad/s
```
````

Um innerhalb einer Zelle einen Zeilenumbruch zu erzeugen, muss mit einem Backslash `\` ein Zeilenumbruch erzwungen werden und in der nächsten Zeile auf gleicher Einrückungsebene weiter geschrieben werden.

```{important}
Sobald Tabellen:

- verbundene Zellen benötigen
- unterschiedliche Spaltenbreiten erzwingen sollen
- oder sehr komplexe Layouts abbilden

stößt `list-table` konzeptionell an Grenzen.
```