(Virtuelle Umgebungen)=
# Virtuelle Umgebungen

## Motivation & Überblick

### Was ist eine „virtuelle Umgebung“?

Eine **virtuelle Umgebung** (engl. *virtual enviroment*) in Python ist eine **isolierte Laufzeitumgebung**, in der du Projekte unabhängig voneinander betreiben kannst.
Sie stellt sicher, dass jedes Projekt eigene Bibliotheken, Versionen und Abhängigkeiten verwendet und damit getrennt von der globalen Python-Installation ist.

Dadurch vermeidest du Versionskonflikte und stellst sicher, dass deine Software auch später unter denselben Bedingungen reproduzierbar ausgeführt werden kann.

```{mermaid}
:align: center
:caption: Isolierte Python-Umgebungen pro Projekt

flowchart LR
  subgraph SYS["Global Python Environment (System)"]
    PY[System-Python<br/>/usr/bin/python]
    subgraph V1["venv_project1/"]
      P1[bin/python]
      S1[lib/.../site-packages]
      P1 --> S1
    end
    subgraph V2["venv_project2/"]
      P2[bin/python]
      S2[lib/.../site-packages]
      P2 --> S2
    end
  end
```

> **Beispiel:**
> Ein älteres Projekt benötigt `NumPy==1.23`, ein neues Projekt `NumPy==2.0`.
> Ohne virtuelle Umgebung würden sich diese Versionen gegenseitig überschreiben.
> In einer venv laufen diese jedoch konfliktfrei nebeneinander.

```{important}

Virtuelle Umgebungen sind keine „virtuellen Maschinen“.\
Sie isolieren nur die Python-Abhängigkeiten, nicht das Betriebssystem oder die CPU.
```

### Probleme ohne eine "virtuelle Umgebung"

Ohne eine **venv** installierst du Pakete **global**. Das führt in der Praxis zu mehreren Problemen:

```{list-table} Typische Probleme ohne virtuelle Umgebung
:align: center
:header-rows: 1

* - Problem
  - Beschreibung
  - Beispiel
* - Versionskonflikte
  - Unterschiedliche Projekte benötigen\
    verschiedene Paketversionen.
  - Projekt A: `matplotlib==3.7`\
    Projekt B: `matplotlib==3.8`
* - Fehlende\
    Reproduzierbarkeit
  - Globale Updates verändern rückwirkend\
    alte Projekte.
  - Nach `pip install -U numpy`\
    funktioniert ein älterer Code\
    plötzlich nicht mehr.
* - Unklare\
    Abhängigkeiten
  - Ohne Isolierung ist nicht\
    nachvollziehbar, welche Pakete\
    ein Projekt tatsächlich benötigt.
  - „works on my machine“-Effekt
* - Administratorrechte
  - Systemweite Installationen benötigen\
    oft erhöhte Rechte.
  - Unter macOS/Linux:\
    `sudo pip install ...`
```

Virtuelle Umgebungen lösen diese Probleme, indem sie **pro Projekt** eine eigene Paketstruktur anlegen.

```{mermaid}
:align: center
:caption: Unterschiedliche Paketversionen pro Projekt

flowchart LR
  subgraph V["Virtuelle Umgebungen (pro Projekt isoliert)"]
    direction TB
    subgraph V1["venv_project1/"]
      direction TB
      P1[.venv/bin/python]
      S1[lib/pythonX.Y/site-packages]
      P1 --> S1
      A1[[Paket A v1.0]]
      B1[[Paket B v2.3]]
      S1 --> A1
      S1 --> B1
    end
    subgraph V2["venv_project2/"]
      direction TB
      P2[.venv/bin/python]
      S2[lib/pythonX.Y/site-packages]
      P2 --> S2
      A2[[Paket A v2.0]]
      C2b[[Paket C v1.4]]
      S2 --> A2
      S2 --> C2b
    end
  end
```

## Wie funktionieren virtuelle Umgebungen?

**Virtuelle Umgebungen** sind kein separates Betriebssystem, sondern eine logische Isolationsschicht innerhalb des Dateisystems. Beim Erstellen einer Umgebung wird eine vollständige Kopie der Python-Laufzeitstruktur angelegt, jedoch ohne die Systembibliotheken zu duplizieren. Dadurch enthält jede Umgebung ihren eigenen Interpreter und Paketpfad und bleibt vom Rest des Systems unabhängig.

### Prinzip: eigener `site-packages`-Ordner + angepasster `PATH`/Shebang

Das Herzstück einer virtuellen Umgebung ist ihr eigener `site-packages`-Ordner. In diesem Verzeichnis installiert `pip` **alle projektspezifischen Pakete**. Dadurch werden Bibliotheken lokal abgelegt und nicht in das globale Python-Verzeichnis geschrieben.

Wird eine virtuelle Umgebung aktiviert, ändert sich der Suchpfad von Python:

1. Der Interpreter innerhalb der venv (z. B. `.venv/bin/python`) wird bevorzugt.
2. Der `PATH` der Shell wird so angepasst, dass venv-Binaries (z. B. `pip`, `python`) zuerst gefunden werden.
3. Die globale Installation bleibt unberührt, ist aber temporär im Hintergrund.

```{mermaid}
:align: center
:caption: Trennung zwischen dem globalen System-Python und einer virtuellen Umgebung

flowchart TB
subgraph System["Globales System"]
PY_SYS[/usr/bin/python/]
SP_SYS[/usr/lib/pythonX.Y/site-packages/]
PY_SYS --> SP_SYS
end

subgraph VENV["Virtuelle Umgebung (.venv)"]
PY_VENV[.venv/bin/python]
SP_VENV[.venv/lib/pythonX.Y/site-packages/]
PY_VENV --> SP_VENV
A1[[numpy==1.24]]
A2[[matplotlib==3.8]]
SP_VENV --> A1
SP_VENV --> A2
end

PY_SYS -. "python → .venv/bin/python (PATH)" .-> PY_VENV
```

Die gestrichelte Linie soll zeigen, dass bei aktivierter venv der Befehl python im Terminal auf den lokalen Interpreter umgeleitet wird.

> **Beispiel**:
> Wenn du `pip install numpy` innerhalb einer aktivierten Umgebung ausführst, landet das Paket unter `.venv/lib/.../site-packages/` und nicht in `/usr/lib/pythonX.Y/site-packages/`.

### Aktivierung/Deaktivierung: was passiert technisch?

Die Aktivierung ist ein reiner **Shell-Vorgang**. Python selbst wird dabei nicht verändert.\
Beim Aufruf von source `source .venv/bin/activate` (*Linux/macOS*) oder `.venv\Scripts\Activate.ps1` (*Windows*) passiert Folgendes:

1. `PATH`**-Manipulation**:\
  Der Pfad zu `.venv/bin` bzw. `.venv\Scripts` wird an den Anfang der `PATH`-Variable gesetzt.\
  Damit zeigen Aufrufe wie `python` oder `pip` automatisch auf die **venv-Binaries**.
2. **Shell-Prompt-Anpassung**:
  In vielen Shells wird der Name der aktiven Umgebung links im Prompt angezeigt.\
  Bspw. `(venv) tobia@MacBook ~ $`
3. **Shebang-Umschaltung**:
  Skripte, die in dieser Umgebung installiert werden, erhalten in der ersten Zeile (`#!`) den Pfad zum **venv-Interpreter**.\
  Dadurch bleibt das Skript später auch außerhalb der aktiven Shell eindeutig zuordenbar.
4. **Deaktivierung**:
  Mit dem Befehl `deactivate` wird der ursprüngliche `PATH` wiederhergestellt.\
  $\rightarrow$ der Systeminterpreter wird wieder verwendet.

### Grenzen: keine CPU-/OS-Isolation (Abgrenzung zu Containern)

Virtuelle Umgebungen isolieren ausschließlich die **Python-Abhängigkeiten** und nicht die Hardware oder das Betriebssystem. Alle Prozesse laufen im gleichen Nutzerkontext und greifen auf dasselbe Dateisystem, denselben Speicher und dieselben Ressourcen zu.

Damit unterscheiden sie sich deutlich von **virtuellen Maschinen**:

```{list-table} Unterschied Virtuelle Umgebung vs. virtuelle Maschine
:align: center
:header-rows: 1

* - Aspekt
  - Virtuelle Umgebung\
    venv
  - Virtuelle Maschine
* - **Ziel**
  - Isolierte Python-Umgebung
  - Vollständiges Betriebssystem
* - **Ressourcenisolation**
  - Keine
  - Vollständig
* - **Startzeit**
  - <1 s
  - Minuten
* - **Typische Nutzung**
  - Python-Entwicklung
  - Test, parallele OS-Nutzung
```

## Schnelleinstieg mit `venv`

Virtuelle Umgebungen können direkt mit dem in Python integrierten Modul `venv` erstellt werden. Es ist ab **Python 3.3** standardmäßig enthalten und es wird somit keine zusätzliche Installation benötigt.

### Voraussetzungen (Python 3.x installiert)

Zunächst sollte geprüft werden, ob bereits Python installiert ist und pber die Konsole erreichbar ist.

```{code-block} console
:caption: Python-Version prüfen
:linenos:

python --version
```

>**Besipielausgabe**: *Python 3.12.6*

```{note}
Falls der Befehl nicht erkannt wird, muss der Python-Interpreter dem Systempfad hinzugefügt werden. Unter Windows kann dies bei der Installation über die Option "*Add Python to PATH*" erfolgen, unter macOS ist dies bei Homebrew-Installationen standardmäßig aktiviert.
```

### Umgebung erstellen

Jedes Projekt erhält in der Regel eine eigene virtuelle Umgebung, die meist im Projektverzeichnis als `.venv` abgelegt wird.

#### macOS

```{code-block} console
:caption: Virtuelle Umgebung erstellen (macOS)
:linenos:

python3 -m venv .venv
```

#### Windows

```{code-block} console
:caption: Virtuelle Umgebung erstellen (Windows)
:linenos:

python -m venv .venv
```
Nach dem Ausführen des Befehls wird der Ordner `.venv` angelegt, der die gesamte Umgebung enthält.

```{code-block} none
:caption: Struktur der virtuellen Umgebung (Windows)

.venv/
├ Scripts/
│ ├ activate
│ ├ deactivate
│ ├ pip.exe
│ └ python.exe
├ Lib/
│ └ site-packages/
└ pyvenv.cfg
```

```{hint}
Der Ordnername `.venv` ist Konvention.\
Du kannst ihn jedoch beliebig wählen (z. B. `env`, `venv-test`), aber `.venv` ist in IDEs wie VS Code automatisch erkennbar.
```

### Aktivieren/Deaktivieren

Das Aktivieren sorgt dafür, dass `python` und `pip` innerhalb des Projekts **auf die lokale Umgebung zeigen**.

#### macOS

```{code-block} console
:caption: Aktivieren der Umgebung (macOS)
:linenos:

source .venv/bin/activate
```

#### Windows

```{code-block} console
:caption: Aktivieren der Umgebung (Windows)
:linenos:

.venv\Scripts\Activate.ps1
```
````{note}
Unter Windows PowerShell kann die Aktivierung einer virtuellen Umgebung blockiert werden. In diesem Fall erscheint eine Meldung wie
*“execution of scripts is disabled on this system”*.

Für die aktuelle Sitzung kann dies umgangen werden durch:

```{code-block} console
:caption: PowerShell-Restriktion temporär aufheben
:linenos:

Set-ExecutionPolicy -Scope Process Bypass
```

Dieser Befehl erlaubt das Ausführen von Aktivierungsskripten nur für die laufende Session und verändert keine globalen Sicherheitseinstellungen.
````

---

```{hint}
Beim Aktivieren wird die Umgebungsvariable **PATH** so angepasst, dass `.venv\Scripts` (Windows) bzw. `.venv/bin` (macOS) an erster Stelle steht.
Dadurch werden `python` und `pip` automatisch aus dieser Umgebung verwendet.
```

Das deaktivieren der virtuellen Umgebung erfolgt auf beiden Systemen mit dem Befehl:

```{code-block} console
:caption: Deaktivieren
:linenos:

deactivate
```

### Pakete installieren & prüfen

Nach der Aktivierung der virtuellen Umgebung können nun Pakete installiert werden.

Da `pip` in der Regel eine ältere Version enthält, empfiehlt es sich, diese zunächst zu aktualisieren:

```{code-block} console
:caption: Aktualisierung von pip
:linenos:

python -m pip install -U pip
```

>Durch das Präfix `python -m` wird sichergestellt, dass das `pip`-Modul des aktuell aktiven Interpreters aufgerufen wird. So werden Pakete immer in die **richtige Umgebung** installiert.

Nach der Aktualisierung können beliebige Python-Pakete installiert werden.

```{code-block} console
:caption: Paket in der Umgebung installieren
:linenos:

python -m pip install <paket>
```

```{hint}
`pip` wird mit `python -m` aufgerufen, da so `pip` über den **aktuell aktiven Interpreter** ausgeführt wird. Dadurch wird garantiert, dass die Pakete in die richtige Umgebung installiert werden.

Bei mehreren Python-Installationen (z.B. System-Python, Anaconda, venvs) kann der reine Aufruf `pip` zu Inkonsistenzen führen, da die Shell eventuell das falsche `pip` im `PATH` findet.

Mit `python -m pip` wird immer das `pip` des angegebenen Interpreters ausgeführt.
```

Die installierten Pakete können anschließend mit dem Befehl `python -m pip list` überprüft werden.

## Reproduzierbarkeit & Deployment

Einer der größten Vorteile einer virtueller Umgebungen ist ihre **Reproduzierbarkeit**. Alle installierten Pakete und Versionen können exakt dokumentiert und auf einem anderen System wiederhergestellt werden. Damit wird der *„works on my machine“*-Effekt außer Kraft gesetzt.


### Freeze: pip freeze > requirements.txt

Mit dem folgenden Befehl werden alle aktuell installierten Pakete, inklusive ihrer Versionsnummern, in eine Textdatei geschrieben.

```{code-block} console
:caption: Abhängigkeiten speichern
:linenos:

python -m pip freeze > requirements.txt
```

Diese Datei dokumentiert den exakten Zustand der Umgebung zum Zeitpunkt der Erstellung und ermöglicht später eine identische Wiederherstellung.

```{tip}
Die Datei `requirements.txt` sollte im Projektverzeichnis gespeichert und versioniert (z.B. über {ref}`Git <git>`) werden, damit sie immer dem aktuellen Stand der Entwicklungsumgebung entspricht.
```
### Installation auf neuem System: pip install -r requirements.txt

Um die Umgebung auf einem anderen System oder in einem neuen Projektordner wiederherzustellen, wird eine frische virtuelle Umgebung erstellt und anschließend mit der gespeicherten `requirements.txt` befüllt.

```{code-block} console
:caption: Umgebung rekonstruieren
:linenos:

python -m venv .venv

# --- macOS ------------------
source .venv/bin/activate

# --- Windows ----------------
.venv\Scripts\activate

python -m pip install -r requirements.txt
```

Alle zuvor gesicherten Pakete werden in der **exakten Version** installiert. Dadurch bleibt das Projekt unabhängig von späteren Updates oder Systemänderungen vollständig reproduzierbar.