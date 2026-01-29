# Sphinx

Sphinx ist ein leistungsstarkes und flexibles **Open-Source-Tool** zur Erstellung strukturierter technischer Dokumentationen (*siehe* [https://www.sphinx-doc.org/en/master/](https://www.sphinx-doc.org/en/master/)).\
Ursprünglich für die **Python-Dokumentation** entwickelt, hat sich Sphinx inzwischen als vielseitige Lösung für unterschiedlichste **technische und benutzerorientierte Dokumentationen** etabliert.

**Was ist Sphinx?**

Sphinx ist ein in Python geschriebener **Dokumentationsgenerator**, der aus textbasierten Quelldateien eine konsistente, verlinkte Dokumentation erzeugt.\
Standardmäßig verwendet Sphin **reStructuredText** (kurz: *reST*), eine einfache und leicht verständliche Auszeichnungssprache, um strukturierte Dokumentation zu erstellen.

In meinen Projekten nutze ich jedoch ein Add-on, mit dem stattdessen **MyST Markdown** verwendet werden kann und damit die gleiche Syntax, die auch in *Jupyter Book* eingesetzt wird. Das Add-on versteht jedoch beide Syntaxen und kann somit sowohl reST als auch MyST Markdown verarbeiten.\
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

Eine Sphinx-Dokumentation basiert auf einer klaren Ordnerstruktur, in der alle Inhalte als Textdateien vorliegen.\
Die zentrale `index`-Datei fungiert als Einstiegspunkt und definiert über Toctrees die logische Struktur der gesamten Dokumentation.

Mit geeigneter Konfiguration können:

- neue Seiten eingebunden,
- Querverweise erstellt,
- Quellcode integriert,
- sowie mathematische Formeln mit TeX-Syntax dargestellt werden.

Im Rahmen von **SimpleScience** wird Sphinx zur Bereitstellung der Dokumentation über **GitHub Pages** eingesetzt.

```{toctree}
:maxdepth: 1
:caption: Inhaltsverzeichnis

section/installation
```