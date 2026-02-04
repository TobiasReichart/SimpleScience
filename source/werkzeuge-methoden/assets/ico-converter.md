(ico-converter)=
# ICO-Converter

Für diesen Converter wird das Paket `pillow` benötigt, dass über den Python-Paketmanager `pip` installiert werden kann:

```{code-block} console
:caption: Installation von Pillow

python -m pip install Pillow
```

```{code-block} python
:caption: ICO-Converter
:linenos:

import tkinter as tk    # Standard GUI-Bibliothek in Python

from pathlib import Path    # robuste Pfadbehandlung
from tkinter import (
    filedialog,         # Standard Dialoge (Datei Öffnen, Speichern)
    messagebox,         # Rückmeldungen in eigenem Fenster
)
from PIL import (
    Image,          # Öffnen, Konvertieren und Speichern der Bilder
    ImageOps,       # Bildverarbeitungsfunktionen
)

def main(root: tk.Tk) -> None:

    size = [(256, 256)] # Größe der Ico-Datei

    # --- PNG auswählen ----
    picture_path = filedialog.askopenfilename(  # "Datei öffnen" Dialog
        title="PNG auswählen",                  # Fenstertitel
        filetypes=[                             # Anzeige filtern
            ("Bilder", "*.png *.jpg *.jpeg"),
            ("PNG", "*.png"),
            ("JPEG", "*.jpg *.jpeg"),
        ],
    )

    if not picture_path:
        # Programm abbrechen, wenn nichts ausgewählt
        return

    picture_path = Path(picture_path)   # String -> Path-Objekt

    # --- Zielpfad wählen ---
    ico_path = filedialog.asksaveasfilename(    # "Speichern unter" Dialog
        title="ICO speichern",                  # Titel des Dialogs
        defaultextension=".ico",                # Endung der Datei
        filetypes=[("ICO-Dateien", "*.ico")],   # Anzeige nach .ico filtern
        initialfile=picture_path.stem + ".ico", # Datei mit korrekter Endung speichern
        initialdir=str(picture_path.parent),    # Startverzeichnis des Dialogs (PNG-Datei)
    )

    if not ico_path: return # Programm abbrechen, wenn nichts ausgewählt

    # --- Konvertieren ---
    try:
        image_to_ico(picture_path, ico_path, sizes=size) # Bild-Datei laden und als Ico-Datei speichern
        messagebox.showinfo("Fertig", f"Icon gespeichert:\n{ico_path}") # Erfolgstext als Userrückmeldung

    except FileNotFoundError:
        # Falls die Png-Datei nicht existiert
        messagebox.showerror("Fehler", "Datei nicht gefunden.")
    
    except PermissionError:
        # Falls keine Schreibrechte vorhanden sind
        messagebox.showerror("Fehler", "Keine Berechtigung zum Schreiben der Datei.")
    
    except OSError as e:
        # Pillow wirft OSError z.B. bei ungültigen Bilddaten/Formaten
        messagebox.showerror("Fehler", f"Konvertierung fehlgeschlagen:\n{e}")

    except Exception as e:
        # Restliche Fehler
        messagebox.showerror("Unerwarteter Fehler", str(e))

def image_to_ico(picture_path: Path | str, ico_path: str, *, sizes: list[tuple[int, int]]) -> None:
    """Konvertiert ein Bild (PNG/JPEG) in ICO und schreibt die gewünschten Größen."""
    with Image.open(picture_path) as im:    # with schließt die Datei automatisch, sobald Block beendet ist
        # JPEGs haben oft EXIF-Rotation -> korrigieren (auch PNG kann Metadaten haben)
        im = ImageOps.exif_transpose(im)

        # ICO profitiert von RGBA (Transparenz möglich). JPEG wird dadurch opak.
        if im.mode != "RGBA":
            im = im.convert("RGBA")

        im.save(ico_path, format="ICO", sizes=sizes)    # Datei speichern

if __name__ == "__main__":
    root = tk.Tk()  # Tkinter-Hauptfenster (Root)
    root.withdraw() # kein Hauptfenster anzeigen
    try:
        main(root)
    finally:
        root.destroy()  # Tkinter sauber beenden
```