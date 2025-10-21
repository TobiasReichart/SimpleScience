# Git - Versionsverwaltung für Projekte

**Was ist Git?**

Git ist ein **Versionsverwaltungssystem**, das ursprünglich von [Linus Torvalds](https://de.wikipedia.org/wiki/Linus_Torvalds) (dem Entwickler des Linux-Kernels) entwickelt wurde.\
Git ermöglicht, den Entwicklungsstand eines Projektes über die Zeit nachzuvollziehen und Änderungen gezielt zu speichern. Jeder dieser gespeicherten Zustände wird als **Commit** bezeichnet. Man kann sich das wie eine Zeitmaschine vorstellen: Zu jedem Zeitpunkt lässt sich ein Projekt in den Zustand einer früheren Version zurückversetzen.

```{figure} bilder/Minimalbeispiel_main_branch.svg
:align: center
:width: 100%

Minimalbeispiel - Hauptzweig (main)
```
Ein zentrales Prinzip von Git ist das Arbeiten mit **Branches** (Zweigen).

- Der **main-Branch** (*früher master*) repräsentiert in der Regel die stabile Hauptversion des Projektes.
- Zusätzliche **Feature-Branches** ermöglichen es, neue Funktionen oder Korrekturen unabhängig zu entwickeln, ohne den Hauptstand zu verändern.
- Am Ende wird ein Branch über einen **Merge** mit dem **main-Branch** zusammengeführt. Dabei prüft Git automatisch, ob Änderungen konfliktfrei kombiniert werden können.

```{figure} bilder/branch_beispie_feature.svg
:align: center
:width: 100%

Branch-Beispiel – Feature-Entwicklung
```
Gerade bei der **Zusammenarbeit im Team** zeigt sich die Stärke von Git. Mehrere Personen können gleichzeitig am selben Projekt arbeiten, ohne sich gegenseitig zu überschreiben. Falls Änderungen an denselben Stellen auftreten, entstehen sogenannte **Konflikte**, die manuell aufgelöst werden müssen.

Git ist **kostenlos, plattformunabhängig** und hat sich inzwischen als Standard in der Softwareentwicklung etabliert.

**Wo liegt der Unterschied zu GitHub?**

Während **Git** ein lokales Werkzeug ist, das auf deinem Rechner arbeitet, ist **GitHub** eine Online-Plattform zum Hosten von Git-Repositories. Sie erweitert Git um zahlreiche nützliche Funktionen, wie

- Gemeinsames Arbeiten an Projekten über das Internet,
- Nachverfolgung von Aufgaben, Bugs und Ideen mit Issues,
- Strukturierte Einreichung und Diskussion von Code-Änderungen über Pull Requests,
- Unterstützung durch Diskussionen, Code-Reviews und Projektplanung,
- Einfache Möglichkeit, Projekte öffentlich zugänglich zu machen.

**Inhaltsverzeichnis**

```{toctree}
:maxdepth: 1

section/installation
section/git_bash
```