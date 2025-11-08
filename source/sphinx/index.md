# Sphinx

Sphinx ist ein leistungsstarkes und flexibles **Open-Source-Tool**, das vor allem für die Erstellung von Dokumentationen verwendet wird (siehe [https://www.sphinx-doc.org/en/master/](https://www.sphinx-doc.org/en/master/)).\
Es wurde ursprünglich für die **Python-Dokumentation** entwickelt, hat sich jedoch schnell als eine vielseitige Lösung für alle Arten von **technischen** und **benutzerorientierten Dokumentationen** etabliert.

```{toctree}
:maxdepth: 1
:caption: Inhaltsverzeichnis

section/installation
```

**Was ist Sphinx?**

Sphinx ist ein Dokumentationsgenerator, der in Python geschrieben wurde. Es nutzt **reStructuredText** (kurz: *reST*), eine einfache und leicht verständliche Auszeichnungssprache, um strukturierte Dokumentation zu erstellen.\
In meinen Projekten nutze ich jedoch ein Add-on, mit dem ich stattdessen **MyST Markdown** verwenden kann - die gleiche Syntax, die auch in Jupyter Book eingesetzt wird.\
Das Besondere an Sphinx ist die Möglichkeit, Dokumente in verschiedene Formate zu exportieren, einschließlich HTML, PDF und LaTeX. Dies macht es zu einer idealen Wahl für Projekte, die eine leicht zugängliche Web-Dokumentation sowie druckbare Formate benötigen

**Warum Sphinx verwenden?**

Sphinx bietet viele Vorteile, die es zu einem bevorzugten Werkzeug für die Erstellung von Dokumentationen machen:

- **Automatische Generierung von Inhaltsverzeichnissen**:\
    Sphinx erstellt automatisch ein Inhaltsverzeichnis (TOC) basierend auf der Struktur deiner reST- oder md-Dateien.
- **Einfaches Erstellen von Verlinkungen**:\
    Sphinx ermöglicht das einfache Erstellen von internen und externen Links, um die Navigation innerhalb der Dokumentation zu vereinfachen.
- **Verschiedene Ausgabeformate**:\
    Dokumentation kann in verschiedenen Formaten wie HTML, PDF, LaTeX, EPUB und mehr exportiert werden.
- **Erweiterungen und Anpassbarkeit**:\
    Dank seiner Erweiterbarkeit können Benutzer Sphinx mit einer Vielzahl von Plugins und Erweiterungen an ihre spezifischen Bedürfnisse anpassen.
- **Unterstützung für Quellcode-Dokumentation**:\
    Sphinx eignet sich hervorragend für die Dokumentation von Softwareprojekten, da es nahtlos mit Tools wie `autodoc` zusammenarbeitet, um Python-Code automatisch zu dokumentieren.

**Wie funktioniert Sphinx?**

Sphinx verwendet eine einfache Ordnerstruktur, in der alle Inhalts-Dateien enthalten sind. Der Aufbau der Sphinx-Dokumentation basiert auf einer index-Datei, die als Einstiegspunkt fungiert und die Struktur der gesamten Dokumentation definiert. Mit der richtigen Konfiguration und einer geeigneten reST- oder md-Syntax können Benutzer dann Seiten hinzufügen, Verlinkungen erstellen, Quellcode einbinden und sogar mathematische Formeln mit TeX-Syntax darstellen.

Im Rahmen von SimpleScience wird Sphinx für die Bereitstellung der Internetpresenz über GitHub verwendet.