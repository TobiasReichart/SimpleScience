from __future__ import annotations
from matplotlib.figure import Figure
from matplotlib.axes import Axes

import numpy as np
import matplotlib.pyplot as plt
import re
from pathlib import Path
from beautyplot import beautyplot, COLORS

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
        f: float | str = 440.,
        time: float = 5e-3,
        periods_fft: int = 4,
        spp: int = 1024,
        *,
        fmax_window: float = 600,
        A4: float = 440
) -> tuple[Figure, tuple[Axes, Axes]]:

    fig, (ax_t, ax_f) = plt.subplots(1, 2, figsize=(10, 4.5))

    if type(f) is str:
        text = f
        f = note_to_freq(f, A4)
        ax_t.set_title(rf"reiner Sinuston: {text} ($f$ = {f:.1f} Hz)".replace(".", ","))
    else:
        ax_t.set_title(rf"reiner Sinuston ($f$ = {f:.1f} Hz)".replace(".", ","))

    
    fs = f*spp     # Abtastfrequenz
    Ts = 1 / fs   # Abtastperiode

    # --- Zeitbereich ---
    t_time = np.arange(0.0, time, Ts)
    x_time = np.sin(2*np.pi*f*t_time)

    ax_t.plot(t_time, x_time, lw=1.8, color=COLORS["blue"])
    ax_t.set_xlim(left=0, right=time)
    ax_t.set_ylim(bottom=-1.2, top=1.2)
    ax_t.set_xlabel(r"$t$ [s]")
    ax_t.set_ylabel("Amplitude")
    beautyplot(fig, ax_t)

    # --- Frequenzbereich ---
    T_fft = periods_fft / f              # Dauer der FFT-Zeitreihe [s]
    N_fft = int(round(T_fft * fs))       # Datenpunkte für FFT
    t_fft = np.arange(0.0, N_fft) * Ts   # Zeitachse für FFT
    x_fft = np.sin(2*np.pi*f*t_fft)      # Signal

    # --- FFT (einseitig) mit sauberer Amplitudenskalierung ---
    X = np.fft.rfft(x_fft)
    f_x = np.fft.rfftfreq(N_fft, d=Ts)

    amp = np.abs(X) / N_fft                  # Grundnormierung
    if N_fft > 1:
        amp[1:-1] *= 2.0                     # einseitig: doppeln außer DC/Nyquist

    # Index der Bin-Frequenz am f0 (exakt, weil coherent)
    k0 = int(round(f * N_fft / fs))
    f0_bin = f_x[k0]
    A0 = amp[k0]                             # Amplitude am Bin

    ax_f.vlines(f0_bin, 0.0, A0, linestyles="-", lw=2.0, color=COLORS["orange"])
    ax_f.scatter([f0_bin], [A0], marker="o", s=20, color=COLORS["orange"], label=rf"$f$= {f0_bin:.1f} Hz".replace(".", ","))
    ax_f.set_xlabel(r"$f$ [Hz]")
    ax_f.set_ylabel(r"|$X(f)$|")
    ax_f.set_title(f"Fourier-Analyse")
    ax_f.set_ylim(bottom=0, top=1.2)
    ax_f.set_xlim(left=0, right= (fs/2) if (fs/2 < fmax_window) else fmax_window)
    ax_f.legend(
    loc="upper right",
    frameon=True,      # Rahmen aktivieren
    edgecolor="black", # Rahmenfarbe
    facecolor="white", # Hintergrund (optional)
    framealpha=0.8,    # Transparenz (1 = deckend)
    )
    beautyplot(fig, ax_f)



    return fig, (ax_t, ax_f)

tones = ["C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4"]

for tone in tones:
    PNG_PATH = FIG_DIR / (f"plot_reiner_sinus_{tone}".replace("#", "is") + ".png")
    fig, (ax_t, ax_f) = sine_with_fft(tone)
    fig.savefig(PNG_PATH, dpi=150)
    plt.close(fig)