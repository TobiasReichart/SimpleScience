# Sphinx

Sphinx ist ein leistungsstarkes und flexibles **Open-Source-Tool**, das vor allem für die Erstellung von Dokumentationen verwendet wird (*siehe* [https://www.sphinx-doc.org/en/master/](https://www.sphinx-doc.org/en/master/)).\
Es wurde ursprünglich für die **Python-Dokumentation** entwickelt, hat sich jedoch schnell als eine vielseitige Lösung für alle Arten von **technischen** und **benutzerorientierten Dokumentationen** etabliert.

**Was ist Sphinx?**

Dabei ist Sphinx ein Dokumentationsgenerator, der in Python geschrieben wurde. Es nutzt **reStructuredText** (kurz: *reST*), eine einfache und leicht verständliche Auszeichnungssprache, um strukturierte Dokumentation zu erstellen.\
In meinen Projekten nutze ich jedoch ein Add-on, mit dem stattdessen **MyST Markdown** verwendet werden kann und damit die gleiche Syntax, die auch in Jupyter Book eingesetzt wird. Das Add-on versteht jedoch beide Syntaxen und kann somit sowohl reST als auch MyST Markdown verarbeiten.\
Das Besondere an Sphinx ist die Möglichkeit, Dokumente in verschiedene Formate zu exportieren, einschließlich HTML und PDF. Dies macht es zu einer idealen Wahl für Projekte, die eine leicht zugängliche Web-Dokumentation sowie druckbare Formate benötigen

**Warum Sphinx verwenden?**

Sphinx bietet viele Vorteile, die es zu einem bevorzugten Werkzeug für die Erstellung von Dokumentationen machen:

- **Automatische Generierung von Inhaltsverzeichnissen**:\
    Sphinx erstellt automatisch ein Inhaltsverzeichnis (TOC) basierend auf der Struktur der reST- oder Markdown-Dateien.
- **Einfaches Erstellen von Verlinkungen**:\
    Sphinx ermöglicht das einfache Erstellen von internen und externen Links, um die Navigation innerhalb der Dokumentation zu vereinfachen.
- **Verschiedene Ausgabeformate**:\
    Dokumentation kann in verschiedenen Formaten wie **HTML, PDF, LaTeX, EPUB** und mehr exportiert werden.
- **Erweiterungen und Anpassbarkeit**:\
    Dank seiner Erweiterbarkeit ist Sphinx mit einer Vielzahl von Plugins und Erweiterungen an alle spezifischen Bedürfnisse anpassbar.
- **Unterstützung für Quellcode-Dokumentation**:\
    Sphinx eignet sich hervorragend für die Dokumentation von Softwareprojekten, da es nahtlos mit Tools wie `autodoc` zusammenarbeitet, um Python-Code automatisch zu dokumentieren.

**Wie funktioniert Sphinx?**

Sphinx verwendet eine einfache Ordnerstruktur, in der alle Inhalts-Dateien enthalten sind. Der Aufbau der Sphinx-Dokumentation basiert auf einer index-Datei, die als Einstiegspunkt fungiert und die Struktur der gesamten Dokumentation definiert. Mit der richtigen Konfiguration und einer geeigneten reST- oder md-Syntax können **Seiten hinzugefügt, Verlinkungen erstellt, Quellcode eingebunden** und sogar **mathematische Formeln mit TeX-Syntax** darstellt werden.

Im Rahmen von SimpleScience wird Sphinx für die Bereitstellung der Internetpresenz über **GitHub Pages** verwendet.

```{toctree}
:maxdepth: 1
:caption: Inhaltsverzeichnis

section/installation
section/struktur-navigation
section/schreiben
section/mathematik
section/tabellen
section/abbildungen
section/mermaid
section/code
section/layout
section/veroeffentlichen
section/pdf
```