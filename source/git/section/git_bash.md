# Grundlagen der Git Bash

```{hint}
Diese Anleitung verwendet die **Git-Bash unter Windows**.\
Alle gezeigten Befehle gelten jedoch auch für macOS, da es sich um standardisierte Unix-Befehle handelt.\
Lediglich die Pfadangaben unterscheiden sich:

- Unter **Windows** beginnen Pfade mit Laufwerksbuchstaben (z. B. /c/Users/...).
- Unter **macOS** beginnen Pfade mit /Users/<Benutzername>/....

Die Befehle (`pwd`, `cd`, `ls`, `mv`, `cp`, `touch`, `mkdir`, `rm`, etc.) funktionieren systemübergreifend identisch.
```

In der Git-Bash lassen sich alle grundlegenden Dateiverwaltungs- und Navigationsbefehle der Unix-Shell ausführen.\
Die Schriftgröße in der Git-Bash kann jederzeit mit {kbd}`Strg` + {kbd}`Mausrad` angepasst werden.

In {numref}`git-bash` ist die Git-Bash im Ausgangszustand dargestellt. Standardmäßig wird hier eine einzelne Eingabezeile angezeigt.

```{code-block} console
:caption: Git-Bash: leere Bash
tobia@Tobis-PC MINGW64 ~
```
Die einzelnen Bestandteile bedeuten:

- `tobia` $\rightarrow$ Name des aktuell eingeloggten Benutzers
- `Tobis-PC` $\rightarrow$ Name des Computers
- `MINGW64` $\rightarrow$ Bezeichnet die von Git-Bash verwendete Kommandozeilenumgebung (Minimalist GNU for Windows 64-bit). Dabei handelt es sich um eine Open-Source-Sammlung von Entwicklungswerkzeugen, mit denen sich native 64-Bit-Windows-Anwendungen erstellen lassen.
- `~` $\rightarrow$ Symbolisiert das aktuelle Verzeichnis. Die Tilde steht in Unix-Systemen für das Benutzerverzeichnis (Home-Verzeichnis).

## Arbeitsverzeichnis abfragen

Das **aktuelle Arbeitsverzeichnis** kann mit dem Befehl `pwd` (*print working directory*) abgefragt werden.
Der Befehl wird nach der Eingabe mit {kbd}`Enter` ausgeführt und gibt den vollständigen Pfad zum aktuellen Verzeichnis zurück.

```{code-block} console
:caption: Git-Bash: pwd
tobia@Tobis-PC MINGW64 ~
$ pwd
/c/Users/tobia
```
In diesem Beispiel zeigt Git-Bash an, dass wir uns im Verzeichnis `/c/Users/tobia` befinden.
Die Tilde `~`, die in der Standardanzeige sichtbar ist, ist eine Abkürzung für genau dieses Benutzerverzeichnis.

(git_navigieren)=
## Navigieren

Mit dem Befehl `cd` (change directory) kannst du zwischen Verzeichnissen wechseln.

- Wird nur `cd` eingegeben, gelangt man direkt zurück ins Benutzerverzeichnis (`~`).
- Gibt man hinter `cd` einen **absoluten Pfad** an, wechselt man in das entsprechende Verzeichnis.

```{code-block} console
:caption: Git-Bash: Ordner aufrufen
tobia@Tobis-PC MINGW64 ~
$ cd /d/Python/Skripte
$ pwd
/d/Python/Skripte
```

**Wechsel ins übergeordnete Verzeichnis**

Um nun in das Verzeichnis `Python`, also den **Übergeordneten Ordner** zu wechseln, kann der Befehl `cd ..` verwendet werden.

```{code-block} console
:caption: Git-Bash: Übergeordneter Ordner
tobia@Tobis-PC MINGW64 /d/Python/Skripte
$ cd ..
$ pwd
/d/Python
```
**Wechsel in Unterordner (relativer Pfad)**

Befindet man sich bereits im gewünschten Verzeichnis, genügt die Angabe des **relativen Pfads** zum Unterordner.\
Hier also der Befehl `cd Skripte`, da wir uns bereits im Verzeichnis `Python` befinden und `Skripte` ein Unterordner von `Python` ist.

```{code-block} console
:caption: Git-Bash: Unterordner aufrufen
tobia@Tobis-PC MINGW64 /d/Python
$ cd Skripte
$ pwd
/d/Python/Skripte
```

## Inhalt des aktuellen Ordners abfragen

Mit dem Befehl `ls` (*list*) wird der gesamte Inhalt des aktuellen Verzeichnisses angezeigt.

```{code-block} console
:caption: Git-Bash: Ordnerinhalt anzeigen
tobia@Tobis-PC MINGW64 /d/Python
$ ls
Skripte/  test.py
```

In diesem Beispiel befindet sich im Verzeichnis `/d/Python` ein Ordner `Skripte/` und eine Datei `test.py`.

Die **Farbmarkierungen** im Output geben zusätzliche Hinweise auf die Art der Datei:

```{list-table} Farben in der Git-Bash
:header-rows: 1
:name: git-bash-farben

* - Farbe
  - Bedeutung
  - Beispiel
* - **Blau**
  - Verzeichnis (Ordner)
  - `Skripte/`
* - **Weiß**
  - Normale Datei
  - `text.txt`
* - **Grün**
  - Ausführbare Datei / Programm
  - `programm.exe`, `script.sh`
* - **Hellblau**
  - Symbolische Verknüpfung (Symlink)
  - `link → Ziel`
* - **Rot**
  - Archiv oder komprimierte Datei
  - `data.zip`, `backup.tar.gz`
* - **Gelb**
  - Geräte- oder Spezialdatei
  - (selten in Git-Bash)
```

Der Befehl `ls` kann mit verschiedenen **Optionen** kombiniert werden, um detailliertere Informationen anzuzeigen:

```{list-table} Wichtige Optionen für ls
:header-rows: 1
:name: git-bash-ls-optionen

* - Befehl
  - Beschreibung
* - `ls`
  - Listet die Dateinamen im aktuellen Verzeichnis auf.
* - `ls -l`
  - Zeigt eine **detaillierte Liste** mit Berechtigungen, Besitzer, Dateigröße und Änderungsdatum.
* - `ls -a`
  - Zeigt **alle Dateien**, auch versteckte (beginnen mit `.`).
* - `ls -lh`
  - Wie `ls -l`, aber mit **lesbaren Größenangaben** (KB, MB, GB statt Byte).
* - `ls -R`
  - Listet den Inhalt **rekursiv**, also auch in allen Unterordnern.
* - `ls -t`
  - Sortiert die Ausgabe nach **Änderungszeit** (neueste Dateien zuerst).
```



## Verschieben von Elementen

Mit dem Befehl `mv` (*move*) lassen sich Dateien oder Ordner verschieben.\
Die Syntax lautet:

```{code-block} console
:caption: Git-Bash: Elemente verschieben (allgemeiner Syntax)
mv [Quelle] [Ziel]
```
- `[Quelle]` $\rightarrow$ das Element, das verschoben werden soll
- `[Ziel]` $\rightarrow$ das Zielverzeichnis oder der neue Name
```{important}
**Achtung**: Befinden sich Leerzeichen im Pfad oder Namen, müssen diese mit einem Backslash (\ ) maskiert werden.
```
```{code-block} console
:caption: Git-Bash: Elemente in Unterverzeichnis verschieben
tobia@Tobis-PC MINGW64 /d/Python
$ ls
Skripte/  test.py

$ mv test.py Skripte
$ ls
Skripte/

$ cd Skripte
$ ls
test.py
```
Analog zum Wechseln in übergeordnete Verzeichnisse mit `cd ..` kann auch beim Verschieben `..` verwendet werden.
```{code-block} console
:caption: Git-Bash: Elemente in Übergeordneten Ordner verschieben
tobia@Tobis-PC MINGW64 /d/Python/Skripte
$ ls
test.py

$ mv test.py ..
$ ls


$ cd ..
$ ls
Skripte/  test.py
```
Mit `mv` lassen sich Dateien und Verzeichnisse auch **umbenennen**, indem als Ziel ein neuer Name angegeben wird.
```{code-block} console
:caption: Git-Bash: Elemente umbenennen
tobia@Tobis-PC MINGW64 /d/Python
$ ls
Skripte/  test.py

$ mv Skripte Ordner
$ mv test.py versuch.py
$ ls
Ordner/  versuch.py
```

## Dateien in Ordner kopieren

Mit dem Befehl `cp` (*copy*) lassen sich Dateien oder Ordner kopieren.\
Die Syntax lautet:
```{code-block} console
:caption: Git-Bash: Elemente kopieren (allgemeiner Syntax)
cp [Quelle] [Ziel]
```
- `[Quelle]` $\rightarrow$ das Element, das kopiert werden soll
- `[Ziel]` $\rightarrow$ das Zielverzeichnis oder der neue Name

```{hint}
- Standardmäßig funktioniert `cp` nur für Dateien.
- Soll ein ganzer **Ordner** kopiert werden, muss die Option `-r` (*recursive*) angegeben werden.
```
```{code-block} console
:caption: Git-Bash: Datei in Unterverzeichnis kopieren
tobia@Tobis-PC MINGW64 /d/Python
$ ls
Ordner/  versuch.py

$ cp versuch.py Ordner
$ ls
Ordner/  versuch.py

$ ls Ordner
versuch.py
```
Statt eines Verzeichnisses kann als Ziel auch ein neuer Dateiname angegeben werden.
```{code-block} console
:caption: Git-Bash: Datei kopieren und umbenennen
tobia@Tobis-PC MINGW64 /d/Python
$ cd Ordner
$ ls
versuch.py

$ cp versuch.py test.py
$ ls
test.py  versuch.py
```
Auch hier kann – wie bei `mv` – `..` verwendet werden.
```{code-block} console
:caption: Git-Bash: Datei in übergeordneten Ordner kopieren
tobia@Tobis-PC MINGW64 /d/Python
$ cd Ordner
$ ls
test.py  versuch.py

$ ls ..
Ordner/  versuch.py

$ cp test.py ..
$ ls ..
Ordner/  test.py  versuch.py
```
Um einen gesamten Ordner inklusive Inhalt zu kopieren, muss die Option `-r` angegeben werden:
```{code-block} console
:caption: Git-Bash: Ordner rekursiv kopieren
tobia@Tobis-PC MINGW64 /d/Python/Ordner
$ cd ..
$ ls
Ordner/  test.py  versuch.py

$ cp -r Ordner Backup
$ ls
Backup/  Ordner/  test.py  versuch.py

$ cd Backup
$ ls
test.py  versuch.py
```

## Elemente Anlegen

**Dateien erstellen mit touch**

Der Befehl `touch` erstellt eine neue leere Datei oder aktualisiert das Änderungsdatum einer bestehenden Datei.
```{code-block} console
:caption: Git-Bash: Datei erstellen
tobia@Tobis-PC MINGW64 /d/Python
$ ls
Backup/  Ordner/  test.py  versuch.py

$ touch readme.txt
$ ls
Backup/  Ordner/  readme.txt  test.py  versuch.py
```
Falls `readme.txt` schon existiert, bleibt der Inhalt unverändert, nur das Änderungsdatum wird aktualisiert.

**Ordner erstellen mit mkdir**

Mit dem Befehl `mkdir` (*make directory*) wird ein neuer Ordner erzeugt.
```{code-block} console
:caption: Git-Bash: Ordner erstellen
tobia@Tobis-PC MINGW64 /d/Python
$ ls
Backup/  Ordner/  readme.txt  test.py  versuch.py

$ mkdir leerer\ Ordner
$ ls
 Backup/   Ordner/  'leerer Ordner'/   readme.txt   test.py   versuch.py
```
```{hint}
- Durch das Hintereinanderschreiben von Dateinamen oder Ordnernamen, können auch mehrere gleichzeitig erstellt werden.
- Mit der Option `-p` lassen sich auch verschachtelte Ordner erstellen. *Bsp.* `$ mkdir -p Projekte/Python/Skripte`
```
## Löschen von Elementen

Mit dem Befehl `rm` (*remove*) lassen sich Dateien und Ordner dauerhaft löschen.\
Die Syntax lautet:
```{code-block} console
:caption: Git-Bash: Elemente löschen (allgemeiner Syntax)
rm [Optionen] [Element(e)]
```
```{important}
- Gelöschte Dateien können nicht ohne Weiteres wiederhergestellt werden.
- Sei vorsichtig bei `rm -r`, da damit ganze Ordnerstrukturen verschwinden können.
```
**Dateien löschen**
```{code-block} console
:caption: Git-Bash: Einzelne Datei löschen
tobia@Tobis-PC MINGW64 /d/Python
$ ls
 Backup/   Ordner/  'leerer Ordner'/   readme.txt   test.py   versuch.py

$ rm test.py
$ ls
 Backup/   Ordner/  'leerer Ordner'/   readme.txt   versuch.py
```
```{code-block} console
:caption: Git-Bash: Mehrere Dateien löschen
tobia@Tobis-PC MINGW64 /d/Python
$ ls
 Backup/   Ordner/  'leerer Ordner'/   readme.txt   versuch.py

$ rm readme.txt versuch.py
$ ls
 Backup/   Ordner/  'leerer Ordner'/
```
**Leere Ordner löschen**
```{code-block} console
:caption: Git-Bash: Leeren Ordner löschen
tobia@Tobis-PC MINGW64 /d/Python
$ ls
 Backup/   Ordner/  'leerer Ordner'/

$ rmdir leerer\ Ordner
$ ls
Backup/  Ordner/
```
`rmdir` funktioniert nur für leere Ordner.

**Ordner mit Inhalt rekursiv löschen**

Um einen gesamten Ordner inklusive Inhalt zu entfernen, wird die Option `-r` (*recursive*) benötigt:
```{code-block} console
:caption: Git-Bash: Ordner rekursiv löschen
tobia@Tobis-PC MINGW64 /d/Python
$ ls
Backup/  Ordner/

$ ls Backup
test.py  versuch.py

$ rm -r Backup
$ ls
Ordner/
```

## Hinweise und Schnellnavigation

```{note}
- `clear` $\rightarrow$ löscht den Inhalt der Konsole
- `mv` $\rightarrow$ Verschieben & Umbenennen
- `cp` $\rightarrow$ Kopieren & Duplizieren (`cp -r`: Ordner mit Inhalt)
- `cd` $\rightarrow$ Navigieren
- `rm` $\rightarrow$ löschen (`rmdir`: leere Ordner, `rm -r`: Ordner mit Inhalt)
- `touch` $\rightarrow$ Dateien erstellen
- `mkdir` $\rightarrow$ Ordner erstellen (`-p`: Verschachtelte Struktur)
- `..` $\rightarrow$ Übergeordnete Struktur
```

- Kopiern von Inhalten in die Zwischenablage: {kbd}`Strg` + {kbd}`einfg`
- Einfügen von Inhalten in die Konsole: {kbd}`Shift` + {kbd}`einfg`
- Mit den beiden Pfeiltasten {kbd}`↑` und {kbd}`↓` kann durch die bereits verwendeten Befehle 
- Durch die {kbd}`Tab`-Taste kann die Autovervollständigung verwendet werden und durch erneutes Drücken von {kbd}`Tab` können Optionen angezeigt werden.