# Installation und Einrichtung von Git

```{attention}
**Hinweis**: Die folgenden Schritte zur Installation von git dienen ausschließlich der Orientierung. Installationsroutinen, Systemvoraussetzungen und Benutzeroberflächen können je nach Betriebssystem und Version variieren.  

Vor der Durchführung lies bitte meinen {ref}`Haftungsausschluss <disclaimer>`. Ich übernehme keine Verantwortung für eventuelle Schäden oder Fehlkonfigurationen.  
```

## Windows

1. Lade zunächst den Git-Installer von der offiziellen Website herunter:

    [https://git-scm.com/downloads](https://git-scm.com/downloads)

    Wähle dort **Windows** und anschließend den Installer, der zu deiner Windows-Version passt.

2. Öffne danach deinen **Downloads-Ordner** und starte den Installer per Doppelklick.

3. Während der Installation werden verschiedene Optionen angeboten. In den meisten Fällen kannst du die **Standard-Einstellungen** übernehmen.<br>
    Nur an den folgenden Stellen habe ich Änderungen vorgenommen:

```{figure} bilder/1-installation_components.png
:align: center
:width: 50%
Installation: Select Components
```
```{figure} bilder/2-installation_editor.png
:align: center
:width: 50%
Installation: Choosing the default editor used by Git
```
```{figure} bilder/3-installation_branch.png
:align: center
:width: 50%
Installation: Adjusting the name of the initial branch in new repositories
```
*Screenshot des Installationsassistenten von git, Version 2.51.0-64, Quelle: git-scm.com*

4. Nach erfolgreicher Installation befindet sich nun ein **Git-Bash-Icon** auf dem Desktop. Mit einem Doppelklick öffnest du die Git-Bash und kannst Git direkt verwenden.

```{figure} bilder/4-installation_git-bash.png
:align: center
:width: 50%
:name: git-bash
Git Bash
```
*Screenshot: Git Bash (Windows 11), Stand 09/2025*

## Mac

coming soon

## Userdaten hinterlegen

In Git wird jede Änderung am Projekt als Commit gespeichert. Jeder Commit enthält neben den eigentlichen Änderungen auch **Metadaten**, z. B.:

- Autor (Name und E-Mail)
- Zeitpunkt der Änderung
- Commit-Nachricht

Das Hinterlegen von Name und E-Mail ist notwendig, damit eindeutig nachvollziehbar bleibt, wer welche Änderung durchgeführt hat.

Gerade bei der Zusammenarbeit in Teams ist diese Information unverzichtbar, da sie Transparenz schafft und Verantwortlichkeiten klar erkennbar macht. Auch in Einzelprojekten ist es hilfreich, die eigene Arbeit lückenlos dokumentiert zu haben

**Name eintragen**:

```{code-block} console
:caption: Git Bash: Username hinterlegen
tobia@Tobis-PC MINGW64 ~
$ git config --global user.name "dein Name"
```

**Überprüfung des Namen**:

```{code-block} console
:caption: Git-Bash: Username testen
tobia@Tobis-PC MINGW64 ~
$ git config --global user.name
dein Name
```

**E-Mail eintragen**:

```{code-block} console
:caption: Git-Bash: E-Mail hinterlegen
tobia@Tobis-PC MINGW64 ~
$ git config --global user.email "deine@email.com"
```
**Überprüfung der E-Mail-Adresse**:

```{code-block} console
:caption: Git-Bash: E-Mail testen
tobia@Tobis-PC MINGW64 ~
$ git config --global user.email
deine@email.com
```
Wenn die Eingaben korrekt waren, zeigt die Konsole deinen Namen bzw. deine E-Mail-Adresse an.