from __future__ import annotations
from matplotlib.figure import Figure
from matplotlib.axes import Axes

import numpy as np
import matplotlib.pyplot as plt
import re
from pathlib import Path
from beautyplot import PlotStyle

# -- Projekt-Root finden (Marker) ----------------------------------------------
def find_project_root(start: Path | None = None) -> Path:
    """Wandelt eine Notenbezeichnung in die Frequenz (gleichstufige Stimmung, Referenz A4).

    Unterstützte Notation
    ---------------------
    - Stammtöne: A, B, C, D, E, F, G (Groß-/Kleinschreibung egal)
    - Vorzeichen: # (Kreuz) oder b (Be)
    - Oktave: ganzzahlig (z. B. 4 für A4)
    Beispiele: `A4`, `C#5`, `Db3`, `g#3`, `bb2`

    Die Berechnung erfolgt relativ zu `A4` mittels
        f = A4 * 2^(n/12)
    wobei `n` die Anzahl der Halbtöne Abstand von A4 ist.

    Parameters
    ----------
    note
        Notenstring (z. B. "C#5", "Db3", "A4").
    A4
        Referenzfrequenz für A4.

    Returns
    -------
    float
        Frequenz der Note in Hertz.

    Raises
    ------
    ValueError
        Wenn das Format der Note ungültig ist oder der Notenname/Vorzeichen nicht erkannt wird.
    """
    here = (start or Path(__file__).resolve()).parent
    markers = {".git", "requirements.txt"}
    for p in [here, *here.parents]:
        if any((p / m).exists() for m in markers):
            return p
    return here  # Fallback: Skriptordner

# -- Ausgabe-Pfad --------------------------------------------------------------
ROOT = find_project_root()
FIG_DIR = ROOT / "source" / "_static" / "plots" / "python" / "rezepte" / "audio"
FIG_DIR.mkdir(parents=True, exist_ok=True)  # legt 'assets' und 'figures' an, falls nötig

# -- Noten nach Bezeichnungen --------------------------------------------------
_NOTE_RE = re.compile(r"^([A-Ga-g])([#b]?)(-?\d+)$")
_SEMITONES = {
    "C": -9, "C#": -8, "Db": -8, "D": -7, "D#": -6, "Eb": -6, "E": -5,
    "F": -4, "F#": -3, "Gb": -3, "G": -2, "G#": -1, "Ab": -1, "A": 0,
    "A#": 1, "Bb": 1, "B": 2
}

# -- Obertongewichtung ---------------------------------------------------------
INSTRUMENT_PARTIALS = {
    "floete":   {1: 1.00, 2: 0.20, 3: 0.10, 4: 0.05},                   # weich, fast sinusförmig
    "violine":  {1: 1.00, 2: 0.70, 3: 0.50, 4: 0.30, 5: 0.25, 6: 0.15}, # obertonreich, brillant
    "klavier":  {1: 1.00, 2: 0.60, 3: 0.35, 4: 0.20, 5: 0.12, 6: 0.08}, # harmonisch, leicht gedämpft
    "tuba":     {1: 1.00, 2: 0.10, 3: 0.50, 4: 0.05, 5: 0.25},          # tief, weich, ungerade betont
}

# -- Notenname in Frequenz umwandeln -------------------------------------------
def note_to_freq(note: str, A4: float = 440.0) -> float:
    """Gleichstufige Stimmung. Notation: A4, C#5, Db3, …"""
    m = _NOTE_RE.match(note)                # Regex-Match auf den ganzen String
    if not m:
        raise ValueError(...)
    name = m.group(1).upper()               # Grundton (A..G), auf Großbuchstabe normiert
    accidental = m.group(2)                 # '' oder '#' oder 'b'
    octave = int(m.group(3))                # Oktavzahl als int
    key = name + accidental                 # z. B. "C#", "Bb", "A"
    if key not in _SEMITONES:
        raise ValueError(...)
    n = _SEMITONES[key] + 12 * (octave - 4) # Halbtöne relativ zu A4
    return A4 * (2.0 ** (n / 12.0))         # Gleichstufige Stimmung

# -- Plot ----------------------------------------------------------------------
def sine_with_fft(
        note: str,
        instrument: str,
        time: float = 5e-3,
        spp: int = 1024,
        fmax_window: float = 1e3,
) -> tuple[Figure, tuple[Axes, Axes]]:

    ps = PlotStyle()
    ps.set_font(family="sans", size=12)
    fig, (ax_t, ax_f) = plt.subplots(1, 2, figsize=(10, 4.5))

    freq = note_to_freq(note)
    amp = list(INSTRUMENT_PARTIALS[instrument].values())

    # Farben (ps.colors oder Matplotlib-Farbnamen)
    color_keys = ["green", "orange", "purple", "cyan", "teal", "grey"]

    # --- Zeit ---
    t_time = np.linspace(0.0, time, spp, endpoint=False)

    sum = np.zeros_like(t_time)

    for i, a in enumerate(amp, 1):
        x = a*np.sin(2*np.pi*i*freq*t_time)
        sum += x
        ax_t.plot(t_time*1e3, x, lw=1.5, color=color_keys[i-1], alpha=0.5)
    
    ax_t.plot(t_time*1e3, sum, lw=2.0, color=ps.colors["blue"], label="Summe")

    ax_t.set_xlim(left=0, right=time*1e3)
    ax_t.set_ylim(bottom=-2.2, top=2.2)
    ax_t.set_xlabel(r"$t$ [ms]")
    ax_t.set_ylabel("Amplitude")
    ax_t.set_title(f"{note} mit Obertönen ({instrument})")
    ax_t.legend(
        loc="lower right",
        frameon=True,      # Rahmen aktivieren
        edgecolor="black", # Rahmenfarbe
        facecolor="white", # Hintergrund (optional)
        framealpha=0.8,    # Transparenz (1 = deckend)
    )
    ps.style_axes(fig, ax_t, comma_axis="y", decimals=1)


    # --- Fourier ---
    for i, a, c in zip(range(1, len(amp)+1), amp, color_keys):
        ax_f.vlines(freq*i, 0, a, color=c, lw=2.0)
        ax_f.plot(freq*i, a, "o", color=c, label=f"{i}. Partial - " + f"{freq*i:.1f} Hz".replace(".", ","))

    ax_f.set_xlabel(r"$f$ [Hz]")
    ax_f.set_ylabel(r"|$X(f)$|")
    ax_f.set_title(f"Fourier-Analyse")
    ax_f.set_ylim(bottom=0, top=1.2)
    ax_f.set_xlim(left=0, right=fmax_window)
    ax_f.legend(
        loc="upper right",
        frameon=True,      # Rahmen aktivieren
        edgecolor="black", # Rahmenfarbe
        facecolor="white", # Hintergrund (optional)
        framealpha=0.8,    # Transparenz (1 = deckend)
    )
    ps.style_axes(fig, ax_f, comma_axis="y", decimals=1)



    return fig, (ax_t, ax_f)


for instrument in list(INSTRUMENT_PARTIALS.keys()):
    PNG_PATH = FIG_DIR / (f"plot_obertoene_C4-{instrument}".replace("#", "is") + ".png")
    fig, (ax_t, ax_f) = sine_with_fft("C4", instrument=instrument, time=0.005, spp=1024, fmax_window=1600)
    fig.tight_layout()
    fig.savefig(PNG_PATH, dpi=150)
    plt.close(fig)
