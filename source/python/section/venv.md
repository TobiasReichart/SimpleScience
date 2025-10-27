(Virtuelle Umgebungen)=
# Virtuelle Umgebungen

## Motivation & Überblick

### Was ist eine „virtuelle Umgebung“?

Eine **virtuelle Umgebung** (engl. *virtual enviroment*) in Python ist eine **isolierte Laufzeitumgebung**, in der du Projekte unabhängig voneinander betreiben kannst.
Sie stellt sicher, dass jedes Projekt eigene Bibliotheken, Versionen und Abhängigkeiten verwendet und damit getrennt von der globalen Python-Installation ist.

Dadurch vermeidest du Versionskonflikte und stellst sicher, dass deine Software auch später unter denselben Bedingungen reproduzierbar ausgeführt werden kann.

```{mermaid}
flowchart LR
  %% Isolierte Python-Umgebungen pro Projekt
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



## Wie funktionieren virtuelle Umgebungen?

### Prinzip: eigener `site-packages`-Ordner + angepasster `PATH`/Shebang

### Aktivierung/Deaktivierung: was passiert technisch?

### Grenzen: keine CPU-/OS-Isolation (Abgrenzung zu Containern)



## Schnelleinstieg mit `venv`

### Voraussetzungen (Python 3.x installiert)

### Umgebung erstellen

#### macOS/Linux

#### Windows

### Aktivieren/Deaktivieren

#### macOS/Linux

#### Windows

### Pakete installieren & prüfen

### Löschen der Umgebung: Ordner entfernen


## Reproduzierbarkeit & Deployment

### Freeze: pip freeze > requirements.txt

### Installation auf neuem System: pip install -r requirements.txt



## Integration in Werkzeuge

### VS Code: Interpreter wählen, automatische Aktivierung

### Jupyter: Kernel aus venv registrieren

