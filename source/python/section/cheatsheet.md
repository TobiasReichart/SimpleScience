# Cheatsheet

## Virtuelle Umgebungen

Eine **virtuelle Umgebung** (engl. *virtual enviroment*) in Python ist eine **isolierte Laufzeitumgebung**, in der du Projekte unabhängig voneinander betreiben kannst.

`````{tab-set}
:sync-group: os
````{tab-item} Windows
**Erstellen einer virtuellen Umgebung im Ordner** `.venv`
```{code-block} console
python -m venv .venv
```
**Aktivieren der Umgebung**
```{code-block} console
.venv\Scripts\Activate.ps1
```
(Falls blockiert: `Set-ExecutionPolicy -Scope Process Bypass` nur für die aktuelle Session.)

**Aktualisieren von pip innerhalb der venv** (saubere Basis)
```{code-block} console
python -m pip install -U pip
```
**Installieren der Pakete in der venv**
```{code-block} console
python -m pip install <paket1> <paket2>
```
**Schreiben der Paketversionen in** `requirements.txt`
```{code-block} console
python -m pip freeze > requirements.txt
```
**Reproduzieren der venv anhand von** `requirements.txt`
```{code-block} console
python -m pip install -r requirements.txt
```
**Deaktivieren der virtuellen Umgebung**
```{code-block} console
deactivate
```
````

````{tab-item} macOS
**Erstellen einer virtuellen Umgebung im Ordner** `.venv`
```{code-block} console
python3 -m venv .venv
```
**Aktivieren der Umgebung**
```{code-block} console
source .venv/bin/activate
```
**Aktualisieren von pip innerhalb der venv** (saubere Basis)
```{code-block} console
python -m pip install -U pip
```
**Installieren der Pakete in der venv**
```{code-block} console
python -m pip install <paket1> <paket2>
```
**Schreiben der Paketversionen in** `requirements.txt`
```{code-block} console
python -m pip freeze > requirements.txt
```
**Reproduzieren der venv anhand von** `requirements.txt`
```{code-block} console
python -m pip install -r requirements.txt
```
**Deaktivieren der virtuellen Umgebung**
```{code-block} console
deactivate
```
````
`````