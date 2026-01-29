@echo off
setlocal
rem In das Verzeichnis der Batch-Datei wechseln
pushd "%~dp0"
rem (Optional) Virtuelle Umgebung aktivieren, wenn vorhanden
if exist ".venv\Scripts\activate.bat" call ".venv\Scripts\activate.bat"
rem Live-Server starten und Browser öffnen
sphinx-autobuild -b html -t dev source build/html --open-browser
rem Aufräumen und Pfad zurücksetzen (nach Beenden)
popd
endlocal