from typing import Union, Sequence
import numpy as np
from scipy.io import wavfile
import re

# -- Töne ----------------------------------------------------------------------
_NOTE_RE = re.compile(r"^([A-Ga-g])([#b]?)(-?\d+)$") # Regex Muster
_SEMITONES = {
    "C": -9, "C#": -8, "Db": -8, "D": -7, "D#": -6, "Eb": -6, "E": -5,
    "F": -4, "F#": -3, "Gb": -3, "G": -2, "G#": -1, "Ab": -1, "A": 0,
    "A#": 1, "Bb": 1, "B": 2
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

# -- Obertongewichtung ---------------------------------------------------------
INSTRUMENT_PARTIALS = {
    "floete":   {1: 1.00, 2: 0.20, 3: 0.10, 4: 0.05},                   # weich, fast sinusförmig
    "violine":  {1: 1.00, 2: 0.70, 3: 0.50, 4: 0.30, 5: 0.25, 6: 0.15}, # obertonreich, brillant
    "klavier":  {1: 1.00, 2: 0.60, 3: 0.35, 4: 0.20, 5: 0.12, 6: 0.08}, # harmonisch, leicht gedämpft
    "tuba":     {1: 1.00, 2: 0.10, 3: 0.50, 4: 0.05, 5: 0.25},          # tief, weich, ungerade betont
}

# -- Einzelnoten erzeugen ------------------------------------------------------
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

def to_int16(
    x: np.ndarray,
    headroom_db: float = 0.0
) -> np.ndarray:
    """
    Skaliert Float-Signal x in int16 ohne Clipping.
    headroom_db < 0 lässt Headroom (z.B. -1.0 dB).
    """
    x = np.asarray(x, dtype=np.float64)          # stabile Rechnung
    peak = np.max(np.abs(x))                     # größter Betrag
    if peak < 1e-12:                             # Stille -> direkt Nullen
        return np.zeros_like(x, dtype=np.int16)
    scale = (32767.0 * 10**(headroom_db/20.0)) / peak  # auf 16-bit skalieren
    y = np.clip(x * scale, -32768, 32767)        # Sicherheits-Clip
    return y.astype(np.int16)                    # Quantisierung

def make_tone_wav(
    note_or_freq: Union[str, float, int],
    duration_s: float,
    sr: int,
    amp: float,
    filename: str,
    A4: float = 440.0,
) -> None:
    """Erzeugt einen Sinuston und speichert als 16-bit PCM WAV."""
    f = _to_freq(note_or_freq, A4=A4)
    N = int(sr * duration_s)                   # Samples
    t = np.arange(N) / sr                      # Zeitachse [s]
    x = amp * np.sin(2 * np.pi * f * t)        # Sinus

    # kurze Fades (~10 ms) gegen Klicks
    fadelen = max(int(0.01 * sr), 1)
    x[:fadelen] *= np.linspace(0, 1, fadelen)  # Fade-In
    x[-fadelen:] *= np.linspace(1, 0, fadelen) # Fade-Out

    wavfile.write(filename, sr, to_int16(x))   # schreiben

# -- Töne mit Obertönen erzeugen -----------------------------------------------
def normalize_partials(partials: dict[int, float], mode: str = "sum") -> dict[int, float]:
    """Normiert Teiltongwichte
    
    mode='sum' -> Summe a_k = 1
    mode='max' -> max a_k = 1
    """
    if not partials:
        return {1: 1.0}  # Fallback: Grundton mit Gewicht 1

    vals = list(partials.values()) # Alle Gewichte
    div = (sum(vals) if mode == "sum" else max(vals)) or 1.0 # Normierungsfaktor (gegen 0 absichern)

    return {k: (a / div) for k, a in partials.items()} # Normierte Map zurückgeben

def get_partials(preset_or_dict, *, norm: str = "sum") -> dict[int, float]:
    """Akzeptiert Preset-Namen (str) oder eigenes Dict und gibt normierte Partials zurück."""
    if isinstance(preset_or_dict, str):
        key = preset_or_dict.lower()  # Preset-Key normalisieren
        if key not in INSTRUMENT_PARTIALS:
            known = ", ".join(sorted(INSTRUMENT_PARTIALS))  # verfügbare Presets auflisten
            raise ValueError(f"Unbekanntes Preset: {preset_or_dict!r} (bekannt: {known})")  # Fehlermeldung
        base = INSTRUMENT_PARTIALS[key]  # Preset holen
    else:
        base = dict(preset_or_dict)  # Kopie des benutzerdefinierten Dicts

    return normalize_partials(base, mode=norm)  # Normierung anwenden und zurückgeben

def make_tone_with_partials(
    note_or_freq: Union[str, float, int],
    duration_s: float,
    sr: int,
    amp: float,
    filename: str,
    partials: Union[str, dict[int, float]] = "sinus",
    A4: float = 440.0,
    fade_s: float = 0.01,
    norm_mode: str = "sum",
) -> None:
    """Erzeugt einen Ton mit harmonischen Obertönen und speichert ihn als 16-bit-WAV."""
    f0 = _to_freq(note_or_freq, A4=A4)                 # Grundfrequenz in Hz
    p = get_partials(partials, norm=norm_mode)         # Obertongewichte normiert holen

    N = int(sr * duration_s)                           # Anzahl Samples
    t = np.arange(N) / sr                              # Zeitachse [s]
    x = np.zeros(N, dtype=np.float64)                  # Akkumulator

    for k, a in p.items():
        x += a * np.sin(2 * np.pi * k * f0 * t)        # k-ter Teilton addieren

    fadelen = max(int(fade_s * sr), 1)                 # Fade-Länge in Samples
    x[:fadelen] *= np.linspace(0, 1, fadelen)          # Fade-in gegen Klicks
    x[-fadelen:] *= np.linspace(1, 0, fadelen)         # Fade-out

    wavfile.write(filename, sr, to_int16(amp * x))     # Pegeln, in int16 wandeln, schreiben

def make_instrument_tone_wav(
    instrument: str,
    note_or_freq: Union[str, float, int],
    duration_s: float,
    sr: int,
    amp: float,
    filename: str,
    A4: float = 440.0,
    fade_s: float = 0.01,
    norm_mode: str = "sum",
) -> None:
    """Komfort: direkt per Instrument-Preset speichern (Alias für make_tone_with_partials)."""
    make_tone_with_partials(
        note_or_freq=note_or_freq,
        duration_s=duration_s,
        sr=sr,
        amp=amp,
        filename=filename,
        partials=instrument,
        A4=A4,
        fade_s=fade_s,
        norm_mode=norm_mode,
    )

# -- Akorde erzeugen -----------------------------------------------------------
def parse_chord_name(chord: str) -> tuple[str, str]:
    """Parser, der Grundton und Akkordqualität aus natürlicher Sprache zurück gibt."""
    m = _CHORD_RE.match(chord) # Regex-Match auf Eingabe
    if not m:
        raise ValueError(f"Ungültiges Akkordformat: {chord!r} (erwartet z.B. 'D4-Major' oder 'A3-dur')")

    root = m.group(1)             # Grundton mit Oktave
    qual_raw = m.group(2).lower() # Qualitätsstring in Kleinbuchstaben

    # Umlaute/ß vereinheitlichen
    qual_norm = (qual_raw
                 .replace("ä", "ae")
                 .replace("ö", "oe")
                 .replace("ü", "ue")
                 .replace("ß", "ss"))

    return root, qual_norm # (Grundton, normalisierte Qualität)

def chord_frequencies(root_note: str, quality: str, A4: float = 440.0) -> list[float]:
    """Berechnet die Frequenzen aller Töne eines Akkords."""
    if quality not in QUALITY_INTERVALS:
        raise ValueError(f"Unbekannte Qualität {quality!r}. Erlaubt: {sorted(set(QUALITY_INTERVALS))}")

    f0 = note_to_freq(root_note, A4=A4)    # Grundfrequenz des Root-Notes berechnen
    intervals = QUALITY_INTERVALS[quality] # Halbton-Intervalle für die Akkordqualität

    return [f0 * (2.0 ** (k / 12.0)) for k in intervals] # Frequenzen aus Halbtonabständen berechnen

def make_chord_wav(
    notes_or_freqs: Sequence[Union[str, float, int]],
    duration_s: float,
    sr: int,
    amp: float,
    filename: str,
    A4: float = 440.0,
    headroom_db: float = 0.0,
) -> None:
    """Speichert einen mehrstimmigen Akkord als 16-bit-WAV."""
    # Frequenzen ermitteln (Notennamen → Hz; Zahlen → float) 
    freqs = [(_to_freq(nf, A4=A4) if not isinstance(nf, (int, float)) else float(nf))  # Name zu Hz oder casten
             for nf in notes_or_freqs]

    # Zeitachse & Mixpuffer
    N = int(sr * duration_s)            # Anzahl Samples
    t = np.arange(N) / sr               # Zeitvektor in s
    mix = np.zeros(N, dtype=np.float64) # Akkumulator für Summensignal

    # Pegel pro Stimme (einfaches Anti-Clipping)
    per = amp / max(len(freqs), 1)      # gleichmäßig verteilen

    # Stimmen addieren (Sinusschwingungen)
    for f in freqs:
        mix += per * np.sin(2 * np.pi * f * t)  # Summe der Sinustöne

    # kurze Fades (~10 ms) gegen Klicks am Anfang/Ende
    fadelen = max(int(0.01 * sr), 1)
    mix[:fadelen] *= np.linspace(0, 1, fadelen)    # Fade-in
    mix[-fadelen:] *= np.linspace(1, 0, fadelen)   # Fade-out

    # In int16 wandeln und schreiben
    x16 = to_int16(mix, headroom_db=headroom_db)   # Normalisierung/Headroom + Quantisierung
    wavfile.write(filename, sr, x16)               # WAV speichern

def make_named_chord_wav(
    chord_name: str,
    duration_s: float,
    sr: int,
    amp: float,
    filename: str,
    A4: float = 440.0,
    headroom_db: float = 0.0,
) -> None:
    """Erzeugt direkt aus einem Akkordnamen eine WAV-Datei."""
    root, qual = parse_chord_name(chord_name)    # Name -> (Grundton, Qualität)
    freqs = chord_frequencies(root, qual, A4=A4) # Akkordton-Frequenzen berechnen

    # WAV rendern und speichern
    make_chord_wav(freqs, duration_s, sr, amp, filename, A4=A4, headroom_db=headroom_db)

# --- Akkorde mit Obertönen ----------------------------------------------------
from typing import Union, Sequence

def make_chord_with_partials(
    notes_or_freqs: Sequence[Union[str, float, int]],
    duration_s: float,
    sr: int,
    amp: float,
    filename: str,
    partials: Union[str, dict[int, float]] = "violine",
    A4: float = 440.0,
    fade_s: float = 0.01,
    norm_mode: str = "sum",
    headroom_db: float = 0.0,
) -> None:
    """
    Erzeugt einen mehrstimmigen Akkord, bei dem jede Stimme mit demselben Obertonspektrum
    (Preset oder Dict) synthetisiert wird. Pegel pro Stimme = amp / N (robust gegen Clipping).
    """
    # Frequenzen auflösen (Notennamen → Hz; Zahlen → float)
    freqs = [(_to_freq(nf, A4=A4) if not isinstance(nf, (int, float)) else float(nf))
             for nf in notes_or_freqs]

    N = int(sr * duration_s)
    t = np.arange(N) / sr
    mix = np.zeros(N, dtype=np.float64)

    # Obertongewichte holen & normieren
    p = get_partials(partials, norm=norm_mode)

    # pro Stimme gleicher Pegelanteil
    per_voice = amp / max(len(freqs), 1)

    # konservative Anti-Aliasing-Grenze
    nyq_guard = 0.45 * sr

    for f0 in freqs:
        x = np.zeros(N, dtype=np.float64)
        for k, a in p.items():
            fk = k * f0
            if fk >= nyq_guard:
                continue  # Oberton oberhalb Bandgrenze weglassen
            x += a * np.sin(2 * np.pi * fk * t)
        # kurze Fades pro Stimme (gegen Klicks)
        fadelen = max(int(fade_s * sr), 1)
        x[:fadelen] *= np.linspace(0, 1, fadelen)
        x[-fadelen:] *= np.linspace(1, 0, fadelen)
        # in den Summenmix addieren (mit pro-Stimme-Pegel)
        mix += per_voice * x / (np.sum(list(p.values())) or 1.0)

    # sicher in int16 schreiben (optional Headroom)
    wavfile.write(filename, sr, to_int16(mix, headroom_db=headroom_db))


def make_named_chord_with_partials(
    chord_name: str,
    duration_s: float,
    sr: int,
    amp: float,
    filename: str,
    partials: Union[str, dict[int, float]] = "violine",
    A4: float = 440.0,
    fade_s: float = 0.01,
    norm_mode: str = "sum",
    headroom_db: float = 0.0,
) -> None:
    """
    Komfort: z. B. 'D4-Major' → Oberton-Akkord als WAV.
    Verwendet QUALITY_INTERVALS + gleichstufige Stimmung (A4=440 Hz).
    """
    root, qual = parse_chord_name(chord_name)
    freqs = chord_frequencies(root, qual, A4=A4)
    make_chord_with_partials(
        notes_or_freqs=freqs,
        duration_s=duration_s,
        sr=sr,
        amp=amp,
        filename=filename,
        partials=partials,
        A4=A4,
        fade_s=fade_s,
        norm_mode=norm_mode,
        headroom_db=headroom_db,
    )


# -- Hilfsfunktionen -----------------------------------------------------------
def _to_freq(note_or_freq: Union[str, float, int], A4: float = 440.0) -> float:
    """Hilfsfunktion: nimmt 'A4' oder 440.0 und gibt Hz zurück."""
    if isinstance(note_or_freq, (int, float)):
        return float(note_or_freq)
    return note_to_freq(str(note_or_freq), A4=A4)

if __name__ == "__main__":
    # C-Dur-Dreiklang mit „Violine“-Obertönen
    make_named_chord_with_partials("C4-Major", 1.2, 44100, 0.9, "C4_maj_violine.wav", partials="violine")

    # A-Moll-Dreiklang, flötenartig
    make_named_chord_with_partials("A3-moll", 1.2, 44100, 0.9, "A3_min_floete.wav", partials="floete")

    # Custom-Spektrum (ungerade Obertöne betont)
    odd = {1:1.0, 3:0.7, 5:0.4, 7:0.25}
    make_chord_with_partials(["D4","F#4","A4"], 1.0, 44100, 0.9, "D_maj_odd.wav", partials=odd)