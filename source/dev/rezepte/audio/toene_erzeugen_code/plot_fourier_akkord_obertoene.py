from __future__ import annotations
from matplotlib.figure import Figure
from matplotlib.axes import Axes

import re
from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt

# --- Hilfsfunktion: source-Verzeichnis finden -----------------
def _find_source_dir(start: Path | None = None) -> Path:
    """Geht vom Skript nach oben und gibt den Ordner 'source' zurück."""
    here = (start or Path(__file__).resolve())
    for p in [here] + list(here.parents):
        if p.name == "source":
            return p
    raise RuntimeError("Kein 'source'-Ordner in den übergeordneten Pfaden gefunden.")

# --- source auf sys.path + Pfade ableiten ---------------------
SOURCE_DIR = _find_source_dir()
sys.path.insert(0, str(SOURCE_DIR))

from plot.beautyplot import PlotStyle

# Ausgabe-Verzeichnis für Plots relativ zu source/
FIG_DIR = SOURCE_DIR / "_static" / "plots" / "python" / "rezepte" / "audio"
FIG_DIR.mkdir(parents=True, exist_ok=True)

HERE = Path(__file__).resolve()
PNG_PATH = FIG_DIR / (HERE.stem + ".png")

# -- Noten nach Bezeichnungen --------------------------------------------------
_NOTE_RE = re.compile(r"^([A-Ga-g])([#b]?)(-?\d+)$")
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

# -- Obertongewichtung ---------------------------------------------------------
INSTRUMENT_PARTIALS = {
    "floete":   {1: 1.00, 2: 0.20, 3: 0.10, 4: 0.05},                   # weich, fast sinusförmig
    "violine":  {1: 1.00, 2: 0.70, 3: 0.50, 4: 0.30, 5: 0.25, 6: 0.15}, # obertonreich, brillant
    "klavier":  {1: 1.00, 2: 0.60, 3: 0.35, 4: 0.20, 5: 0.12, 6: 0.08}, # harmonisch, leicht gedämpft
    "tuba":     {1: 1.00, 2: 0.10, 3: 0.50, 4: 0.05, 5: 0.25},          # tief, weich, ungerade betont
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
    """Gibt die Noten eines Akkords als #-Namen mit Oktave zurück (z.B. ['C4','E4','G4']).

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

# -- Plot ----------------------------------------------------------------------
def chord_with_fft(
        note: str,
        quality: str,
        instrument: str,
        time: float = 5e-3,
        spp: int = 1024,
        fmax_window: float = 1e3,
) -> tuple[Figure, tuple[Axes, Axes]]:

    ps = PlotStyle()
    ps.set_font(family="sans", size=12)
    fig, (ax_t, ax_f) = plt.subplots(2, 1, figsize=(10, 8))

    freq = chord_frequencies(note, quality)
    amp = list(INSTRUMENT_PARTIALS[instrument].values())
    names = chord_notes(note, quality)

    # Farben (ps.colors oder Matplotlib-Farbnamen)
    color_keys = ["green", "purple", "red"]

    # --- Zeit ---
    t_time = np.linspace(0.0, time, spp, endpoint=False)

    sum = np.zeros_like(t_time)
    tone = np.zeros_like(t_time)

    for f, color, name in zip(freq, color_keys, names):
        for i, a in enumerate(amp, 1):
            x = a*np.sin(2*np.pi*i*f*t_time)
            tone += x
        sum += tone
        ax_t.plot(t_time*1e3, tone, lw=1.5, color=color, alpha=0.5, label={name})
        tone = np.zeros_like(t_time)

    ax_t.plot(t_time*1e3, sum, lw=2.0, color=ps.colors["blue"], label=f"{note} {quality.capitalize()} (Summe)")

    ax_t.set_xlim(left=0, right=time*1e3)
    ax_t.set_ylim(bottom=-6.5, top=6.5)
    ax_t.set_xlabel(r"$t$ [ms]")
    ax_t.set_ylabel("Amplitude")
    ax_t.set_title(f"{note} Dur mit Obertönen ({instrument.capitalize()})")
    ax_t.legend(
        loc="lower right",
        frameon=True,      # Rahmen aktivieren
        edgecolor="black", # Rahmenfarbe
        facecolor="white", # Hintergrund (optional)
        framealpha=0.8,    # Transparenz (1 = deckend)
    )
    ps.style_axes(fig, ax_t, comma_axis="y", decimals=1)


    # --- Fourier ---
    for f, color in zip(freq, color_keys):
        for i, a in zip(range(1, len(amp)+1), amp):
            ax_f.vlines(f*i, 0, a, color=color, lw=2.0)
            ax_f.plot(f*i, a, "o", color=color, label=f"{i}. Partial - " + f"{f*i:.1f} Hz".replace(".", ","))

    ax_f.set_xlabel(r"$f$ [Hz]")
    ax_f.set_ylabel(r"|$X(f)$|")
    ax_f.set_title(f"Fourier-Analyse")
    ax_f.set_ylim(bottom=0, top=1.2)
    ax_f.set_xlim(left=0, right=fmax_window)
    ps.style_axes(fig, ax_f, comma_axis="y", decimals=1)



    return fig, (ax_t, ax_f)


for instrument in list(INSTRUMENT_PARTIALS.keys()):
    PNG_PATH = FIG_DIR / (f"plot_akkord_C4-Major-{instrument}".replace("#", "is") + ".png")
    fig, (ax_t, ax_f) = chord_with_fft("C4", "dur", instrument=instrument, time=0.025, spp=1024, fmax_window=2500)
    fig.tight_layout()
    fig.savefig(PNG_PATH, dpi=150)
    plt.close(fig)
