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

# -- Töne ----------------------------------------------------------------------
_NOTE_RE = re.compile(r"^([A-Ga-g])([#b]?)(-?\d+)$") # Regex Muster
_SEMITONES = {
    "C": -9, "C#": -8, "Db": -8, "D": -7, "D#": -6, "Eb": -6, "E": -5,
    "F": -4, "F#": -3, "Gb": -3, "G": -2, "G#": -1, "Ab": -1, "A": 0,
    "A#": 1, "Bb": 1, "B": 2
}

# Einheitliche #-Namensliste (0=C, 11=B)
SHARP_NAMES = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

NAME_TO_INDEX = {
    "C":0,  "C#":1,  "Db":1,
    "D":2,  "D#":3,  "Eb":3,
    "E":4,  "Fb":4,  "E#":5,  # E#=F
    "F":5,  "F#":6,  "Gb":6,
    "G":7,  "G#":8,  "Ab":8,
    "A":9,  "A#":10, "Bb":10,
    "B":11, "Cb":11, "B#":0,  # B#=C (nächste Oktave!)
}

# -- Akkordqualität ------------------------------------------------------------
_CHORD_RE = re.compile(r"^\s*([A-Ga-g][#b]?-?\d+)\s*[-\s_]+\s*([A-Za-zäöüÄÖÜ]+[24]?)\s*$") # Regex Muster
QUALITY_INTERVALS = {
    "major":      [0, 4, 7], "dur":  [0, 4, 7], "maj":          [0, 4, 7],
    "minor":      [0, 3, 7], "moll": [0, 3, 7], "min":          [0, 3, 7],
    "diminished": [0, 3, 6], "dim":  [0, 3, 6], "vermindert":   [0, 3, 6],
    "augmented":  [0, 4, 8], "aug":  [0, 4, 8], "uebermaessig": [0, 4, 8], "übermäßig": [0, 4, 8],
    "sus2":       [0, 2, 7],
    "sus4":       [0, 5, 7],
}

# -- Notenname in Frequenz umwandeln -------------------------------------------
def note_to_freq(note: str, A4: float = 440.0) -> float:
    """Berechnet die Frequenz einer Note in der gleichstufigen Stimmung relativ zu A4.

    Die Funktion unterstützt Notationen wie `A4`, `C#5`, `Db3` usw.
    Sie basiert auf der Formel der gleichstufigen Stimmung:

        f = A4 * 2^(n / 12)

    wobei `n` die Anzahl der Halbtöne Abstand von A4 ist.

    Parameters
    ----------
    note
        Notenbezeichnung als String, z. B. "A4", "C#5" oder "Db3".
    A4
        Referenzfrequenz für den Kammerton A4 (Standard: 440 Hz).

    Returns
    -------
    float
        Frequenz der Note in Hertz.

    Raises
    ------
    ValueError
        Wenn die Notation ungültig ist oder der Notenname nicht erkannt wird.

    Beispiele
    ---------
    >>> note_to_freq("A4")
    440.0
    >>> round(note_to_freq("C4"), 2)
    261.63
    >>> round(note_to_freq("F#5"), 2)
    739.99

    Hinweise
    --------
    - Unterstützt enharmonische Äquivalente (z. B. C# = Db).
    - Oktavangabe muss eine ganze Zahl sein.
    - Referenz A4 kann geändert werden, z. B. `A4=442.0` für Orchesterstimmung.
    """
    m = _NOTE_RE.match(note)                # Regex-Match auf den ganzen String
    if not m:
        raise ValueError(f"Ungültige Notenbezeichnung: {note!r}")
    name = m.group(1).upper()               # Grundton (A..G), auf Großbuchstabe normiert
    accidental = m.group(2)                 # '' oder '#' oder 'b'
    octave = int(m.group(3))                # Oktavzahl als int
    key = name + accidental                 # z. B. "C#", "Bb", "A"
    if key not in _SEMITONES:
        raise ValueError(f"Unbekannter Notenname/Vorzeichen: {key!r}")
    n = _SEMITONES[key] + 12 * (octave - 4) # Halbtöne relativ zu A4
    return A4 * (2.0 ** (n / 12.0))         # Gleichstufige Stimmung

# -- Frequenzen von Akkord finden ----------------------------------------------
def chord_frequencies(root_note: str, quality: str, A4: float = 440.0) -> list[float]:
    """Berechnet die Frequenz einer Note in gleichstufiger Stimmung relativ zu A4.

    Diese Funktion wandelt eine Notenbezeichnung (z. B. „A4“, „C#5“, „Db3“) in ihre
    Frequenz in Hertz um, basierend auf der gleichstufigen Temperatur.

    Formel
    ------
    f = A4 * 2^(n / 12)

    Dabei ist `n` die Anzahl der Halbtöne Abstand zur Referenznote A4.

    Parameters
    ----------
    note
        Notenbezeichnung (z. B. "A4", "C#5", "Db3").
    A4
        Frequenz der Referenznote A4 in Hertz (Standard: 440 Hz).

    Returns
    -------
    float
        Frequenz der angegebenen Note in Hertz.

    Raises
    ------
    ValueError
        Wenn die Notenbezeichnung ungültig ist oder nicht erkannt wird.

    Beispiele
    ---------
    >>> note_to_freq("A4")
    440.0
    >>> round(note_to_freq("C4"), 2)
    261.63
    >>> round(note_to_freq("F#5"), 2)
    739.99
    """
    if quality not in QUALITY_INTERVALS:
        raise ValueError(f"Unbekannte Qualität {quality!r}. Erlaubt: {sorted(set(QUALITY_INTERVALS))}")

    f0 = note_to_freq(root_note, A4=A4)    # Grundfrequenz des Root-Notes berechnen
    intervals = QUALITY_INTERVALS[quality] # Halbton-Intervalle für die Akkordqualität

    return [f0 * (2.0 ** (k / 12.0)) for k in intervals] # Frequenzen aus Halbtonabständen berechnen

def _parse_note(note: str) -> tuple[int, int]:
    """
    Wandelt z.B. 'Db3', 'C#4', 'B#3', 'Cb4' in (index, octave).
    index: 0..11 (C..B), immer als #-Index gedacht.
    """
    m = _NOTE_RE.match(note)
    if not m:
        raise ValueError(f"Ungültige Notation: {note!r}")
    name = m.group(1).upper()
    acc  = m.group(2) or ""
    octv = int(m.group(3))
    key = name + acc
    if key not in NAME_TO_INDEX:
        raise ValueError(f"Unbekannter Notenname/Vorzeichen: {key!r}")

    idx = NAME_TO_INDEX[key]

    # Oktavkorrekturen für enharmonische Sonderfälle
    # B# == C der NÄCHSTEN Oktave
    if key == "B#":
        octv += 1
    # Cb == B der VORHERIGEN Oktave
    if key == "Cb":
        octv -= 1

    return idx, octv

def chord_notes(root_note: str, quality: str) -> list[str]:
    """
    Gibt die Noten eines Akkords als #-Namen mit Oktave zurück (z.B. ['C4','E4','G4']).

    Parameters
    ----------
    root_note : z.B. 'C4', 'Db3', 'B#3'
    quality   : z.B. 'major', 'minor', 'dim', 'aug', 'sus2', 'sus4' (Aliasnamen werden unterstützt)

    Returns
    -------
    list[str]
    """
    if quality not in QUALITY_INTERVALS:
        raise ValueError(f"Unbekannte Qualität {quality!r}. Erlaubt: {sorted(set(QUALITY_INTERVALS))}")

    root_idx, root_oct = _parse_note(root_note)
    intervals = QUALITY_INTERVALS[quality]

    notes = []
    for k in intervals:
        total = root_idx + k
        idx   = total % 12
        oct_add = total // 12
        name = SHARP_NAMES[idx] + str(root_oct + oct_add)
        notes.append(name)
    return notes

# # -- Plot ----------------------------------------------------------------------
def sine_with_fft(
        f: tuple[str, str],
        time: float = 5e-3,
        spp: int = 1024,
        fmax_window: float = 1e3,
        chord_name: str = None
) -> tuple[Figure, tuple[Axes, Axes]]:
    

    ps = PlotStyle()
    ps.set_font(family="sans", size=12)
    fig, (ax_t, ax_f) = plt.subplots(1, 2, figsize=(10, 4.5))

    # --- Frequenzen & Notennamen des Akkords ---
    freqs = np.array(chord_frequencies(*f), dtype=float)
    names = chord_notes(*f)

    # --- Zeitachse ---
    t_time = np.linspace(0.0, time, spp, endpoint=False)
    X = np.sin(2*np.pi * freqs[:, None] * t_time[None, :])

    # Farben (ps.colors oder Matplotlib-Farbnamen)
    color_keys = ["green", "purple", "red", "teal"]
    colors = [ps.colors.get(k, k) for k in color_keys[:len(freqs)]]

    # Jede Teilkomponente plotten
    for x_row, c in zip(X, colors):
        ax_t.plot(t_time*1e3, x_row, lw=1.5, color=c, alpha=0.5)

    # Summensignal (optional)
    x_sum = X.mean(axis=0)  # Normalisiert, damit nichts clippt
    ax_t.plot(t_time*1e3, x_sum, lw=2.0, color=ps.colors["blue"], label=chord_name + " (Summe)")

  
    ax_t.set_xlim(left=0, right=time*1e3)
    ax_t.set_ylim(bottom=-1.2, top=1.2)
    ax_t.set_xlabel(r"$t$ [ms]")
    ax_t.set_ylabel("Amplitude")
    ax_t.set_title(chord_name)
    ax_t.legend(
        loc="lower right",
        frameon=True,      # Rahmen aktivieren
        edgecolor="black", # Rahmenfarbe
        facecolor="white", # Hintergrund (optional)
        framealpha=0.8,    # Transparenz (1 = deckend)
    )
    ps.style_axes(fig, ax_t, comma_axis="y", decimals=1)

    # --- Frequenzbereich ---

    # Sticks an den Akkordfrequenzen
    for fi, c, name in zip(freqs, colors, names):
        ax_f.vlines(fi, 0, 1, color=c, lw=2.0)
        ax_f.plot(fi, 1, "o", color=c, label=f"{name} - {fi:.1f} Hz".replace(".", ","))

    ax_f.set_xlabel(r"$f$ [Hz]")
    ax_f.set_ylabel(r"|$X(f)$|")
    ax_f.set_title(f"Fourier-Analyse")
    ax_f.set_ylim(bottom=0, top=1.6)
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

chords = [("C4", "major"), ("C4", "minor"), ("C4", "diminished"), ("C4", "augmented"), ("C4", "sus2"), ("C4", "sus4")]

for chord, name in zip(chords, ["C4-Dur", "C4-Moll", "C4-Vermindert", "C4-Übermaßig", "C4-Sus2", "C4-Sus4"]):
    PNG_PATH = FIG_DIR / (f"plot_Akkord_{chord[0]}-{chord[1]}".replace("#", "is") + ".png")
    fig, (ax_t, ax_f) = sine_with_fft(chord, time=0.025, spp=1024, fmax_window=600, chord_name=name)
    fig.savefig(PNG_PATH, dpi=150)
    plt.close(fig)
