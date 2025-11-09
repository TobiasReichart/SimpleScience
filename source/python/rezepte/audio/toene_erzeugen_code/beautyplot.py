"""
kleine Funktion um die Optik von Matplotlib-Graphen aufzuhübschen
wird später durch das Modul Beautyplot ersetzt.
Ein Modul, welches auf Basis von Matplotlib schönere Layouteinstellungen setzt.
"""

def beautyplot(fig, ax):
    ax.tick_params(        # Hauptticks anpassen
        axis="both",       # Sowohl x- als auch y-Achse
        which="major",     # Gilt nur für Hauptticks
        direction="inout", # Ticks zeigen sowohl nach innen als auch nach außen
        length=10,         # Länge der Ticks in Punkten
        width=1            # Strichdicke der Ticks
    )
    ax.minorticks_on()     # Nebenticks anzeigen
    ax.tick_params(        # Nebenticks anpassen
        axis="both",       # Sowohl x- als auch y-Achse
        which='minor'  ,   # Gilt nur für Nebenticks
        direction='inout', # Zeigen nach innen
        length=5,          # Kürzer als Hauptticks
        width=0.8,         # Dünner als Hauptticks
        color='gray'       # In dezenter grauer Farbe
    )
    ax.spines["top"].set_visible(False)   # obere Rahmenlinie ausblenden
    ax.spines["right"].set_visible(False) # rechte Rahmenlinie ausblenden

    ax.spines["left"].set_linewidth(1)   # y-Achse Linienstärke anpassen
    ax.spines["bottom"].set_linewidth(1) # x-Achse Linienstärke anpassen

    ax.grid(           # Gitterlinien anzeigen
        True,          # Gitterlinien einschalten
        linestyle=":", # Gepunktete Linie
        linewidth=0.5, # Dünne Linie
        alpha=1        # Volle Deckkraft (1.0 = undurchsichtig)
    )
    ax.set_facecolor("#f5f5f5") # Hintergrundfarbe setzen (Graph)
    fig.patch.set_alpha(0.0)      # Figure transparent
    