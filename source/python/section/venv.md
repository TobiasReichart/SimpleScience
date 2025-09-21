(Virtuelle Umgebungen)=
# Virtuelle Umgebungen

## Motivation & Überblick

### Was ist eine „virtuelle Umgebung“?

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

