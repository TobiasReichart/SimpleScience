# Töne mit Python erzeugen und speichern

```{hint}
Die folgenden Beispiele sind bewusst **didaktisch aufgebaut**:\ 
Ziel ist das **Verständnis der Prinzipien** hinter digitaler Klangerzeugung, nicht die Entwicklung eines perfekt programmierten Synthesizers.
```

In diesem Abschnitt wollen wir, **synthetisch Töne** mit **Python, NumPy** und **SciPy** generieren und als **WAV-Datei** abspeichern.
Dabei beginnen wir mit dem einfachsten denkbaren Ton, dem **Kammerton A4**, von dem sich alle anderen Töne der Musik ableiten.
Wir wollen diesen als reinen Sinuston generieren.
Wir wollen schrittweise von einfachen Sinustönen zu komplexeren Klängen mit Hüllkurven, Obertönen und Akkorden vordringen.\
Der hier vorgestellte Code wird später um diese Funktionen erweitert.

```{admonition} benötigte Module
:class: note

Um die hier beschriebenen Code-Snippets oder den gesamten code verwenden zu können werden die folgenden Module benötigt:

- `numpy`
- `scipy`
```

```{code-block} console
:caption: benötigte Module mit pip installieren

python -m pip install numpy scipy
```

## Der Sinuston als Grundbaustein

Ein reiner Ton ist eine **periodische Schwingung mit nur einer Frequenz**. Mathematisch wird er beschrieben durch

$$\blue{A(t)} = \red{A_{0}} \sin(2 \pi \purple{f} \green{t})$$

```{figure} ../../../_static/plots/python/rezepte/audio/plot_tone_A4.png
:width: 90%
:align: center
:alt: Kammerton A4 (440 Hz) im Zeitbereich

Verlauf eines reinen Sinustons mit 440 Hz (A4) über 5 ms.
```

mit der Amplitude $\red{A_{0}}$, der Frequenz $\purple{f}$ (in Hz) und der Zeit $\green{t}$ (in s).

Diese Gleichung liefert eine kontinuierliche Schwingung, die ein Computer jedoch **abtasten** muss, da er nur **diskrete Werte** verarbeiten kann.

### Die Abtastrate

Beim Sampling wird das analoge Signal in festen Zeitabständen gemessen. Die **Abtastrate** $f_s$ gibt an, wie viele Messwerte pro Sekunde erfasst werden.

Typische Werte sind hierbei:

- 8 000 Hz – Telefonqualität  
- 44 100 Hz – CD-Qualität (Standard in Audioverarbeitung)  
- 48 000 Hz – Studio- und Videotechnik  
- 96 000 Hz und mehr – High-Resolution-Audio  

```{figure} ../../../_static/plots/python/rezepte/audio/plot_abtasten.png
:width: 100%
:align: center
:alt: Kammerton A4 (440 Hz) im Zeitbereich

Abtasten des Kammertons mit einer Abtastrate von 2 kHz
```

In diesem Beispiel verwenden wir die Standardrate **44 100 Hz**. Damit werden in einer Sekunde 44 100 Messpunkte erzeugt,genug, um auch hohe Frequenzen korrekt darzustellen (siehe **Nyquist-Theorem**).

### Die Umsetzung in Python

Im folgenden minimalen Beispiel wird ein **440 Hz-Sinuston** erzeugt und als
WAV-Datei gespeichert.

```{literalinclude} toene_erzeugen_code/01_tone_A4.py
:caption: 440-Hz-Sinuston (A4) als WAV
:language: python
:linenos:
```

{download}`Vollständiger Code (Ton erzeugen) <toene_erzeugen_code/01_tone_A4.py>`

**Klicks vermeiden: kurze Ein-/Ausblendung (Fades)**

Abrupte Signalstarts/-enden erzeugen hörbare Klicks (Sprungstellen).
Eine 5 bis 10 ms **Fade-In/Out** glättet den Anfang und das Ende und ist für saubere Demos völlig ausreichend.
Für realistischere Hüllkurven (Instrumente) führen wir später ADSR ein.
Für den Moment bleiben die Fades jedoch bewusst minimal.

### Programmstruktur

Im nächsten Schritt bringen wir den bisherigen Code in eine klare Programmstruktur, um darauf später neue Funktionen wie Akkorderzeugung, Obertöne oder spektrale Analysen aufbauen zu können.
Ziel ist eine saubere, wiederverwendbare API.

Dazu trennen wir zwei Aufgaben:

1.	**Konvertierung**: Eine Hilfsfunktion `to_int16()` normiert Float-Signale clippingfrei auf den 16-bit-PCM-Bereich [-32768, 32767] und verhindert damit Übersteuerungen beim Speichern.
2.	**Erzeugung**: Die Funktion `make_tone_wav()` erzeugt einen Sinuston beliebiger Frequenz und Dauer, fügt kurze Fades gegen Klicks hinzu und speichert das Ergebnis als WAV-Datei.

Diese Struktur erlaubt es, Töne oder ganze Tonfolgen künftig systematisch zu generieren, ohne Code zu duplizieren.
So entsteht schrittweise ein modulares Grundgerüst für akustische und spektrale Experimente.

```{literalinclude} toene_erzeugen_code/02_tone_freq.py
:caption: Töne beliebiger Frequenzen mit klarer API
:language: python
:linenos:
```

```{code-block} python
:caption: Beispielcode: Sinuston erzeugen
:linenos:

# Demo 1: A4 440 Hz, 1 s
make_tone_wav(freq_hz=440.0, duration_s=1.0, sr=44100, amp=0.9, filename="tone_A4_440Hz.wav")

# Demo 2: C5 ca. 523.25 Hz, 0.8 s
make_tone_wav(freq_hz=523.251, duration_s=0.8, sr=44100, amp=0.9, filename="tone_C5_523Hz.wav")
```

{download}`Vollständiger Code (Töne nach Frequenz) <toene_erzeugen_code/02_tone_freq.py>`

Die **physikalische Grundlage**, also wie Frequenzen bestimmten Tönen zugeordnet werden und wie Skalen entstehen, wird im Abschnitt {ref}`Töne und Frequenzen` ausführlich behandelt.

## Notennamen unterstützen

Um das Arbeiten mit Tönen intuitiver zu gestalten, wollen wir die bisherige Funktion um eine **Notenerkennung** erweitern.
Anstatt eine Frequenz manuell anzugeben, kann so direkt eine Notation wie A4, C#5 oder Db3 verwendet werden.
Die Funktion `note_to_freq()` berechnet daraus die entsprechende Frequenz nach der **gleichstufigen Stimmung** (Referenzton A4 = 440 Hz).

```{code-block} python
:caption: Notennamen unterstützen (A4=440 Hz, gleichstufig)
:linenos:

# --- Notennamen -> Frequenz (A4 = 440 Hz) ---
import re

_NOTE_RE = re.compile(r"^([A-Ga-g])([#b]?)(-?\d+)$")
_SEMITONES = {
    "C": -9, "C#": -8, "Db": -8, "D": -7, "D#": -6, "Eb": -6, "E": -5,
    "F": -4, "F#": -3, "Gb": -3, "G": -2, "G#": -1, "Ab": -1, "A": 0,
    "A#": 1, "Bb": 1, "B": 2
}

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
```

Nun müssen wir unsere `make_tone_wav()` Funktion noch anpassen, sodass diese Hz und Note akzeptiert.

```{code-block} python
:caption: Anpassen der API für das Unterstützen von Notennamen
:linenos:

from typing import Union

def _to_freq(note_or_freq: Union[str, float, int], A4: float = 440.0) -> float:
    """Hilfsfunktion: nimmt 'A4' oder 440.0 und gibt Hz zurück."""
    if isinstance(note_or_freq, (int, float)):
        return float(note_or_freq)
    return note_to_freq(str(note_or_freq), A4=A4)

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
```

```{code-block} python
:caption: Beispielcode: Sinuston nach Notenname
:linenos:

# Hz-Eingabe
make_tone_wav(440.0, duration_s=1.0, sr=44100, amp=0.9, filename="tone_A4_440Hz.wav")

# Noten-Eingabe
make_tone_wav("C5",   duration_s=0.8, sr=44100, amp=0.9, filename="tone_C5.wav")
make_tone_wav("F#4",  duration_s=0.8, sr=44100, amp=0.9, filename="tone_Fis4.wav")

# Optional: anderer Kammerton (historisch / Orchester)
make_tone_wav("A4", duration_s=1.0, sr=44100, amp=0.9, filename="tone_A4_442Hz.wav", A4=442.0)
```

Die vollständige Version kann hier Heruntergeladen werden.

{download}`Vollständiger Code (Töne) <toene_erzeugen_code/03_tones_hz_name.py>`

## Akkorde

Nachdem wir jetzt **einzelne Töne** synthetisch erzeugen können, stellt sich die Frage, was geschieht, wenn mehrere Töne **gleichzeitig** klingen?

In der Physik bedeutet das die Überlagerung periodischer Signale.\
In der Musik entsteht daraus ein Akkord.\
Während ein einzelner Ton durch eine einzige Frequenz beschrieben werden kann, setzt sich ein Akkord aus mehreren Teiltönen zusammen, die sich im Zeitbereich überlagern.

Diese einfache Addition von Sinusschwingungen ist ein direktes Beispiel für das **Superpositionsprinzip**, eines der zentralen Konzepte der Wellenphysik.
Ein Akkord ist also nichts anderes als die Summe mehrerer Sinusschwingungen mit unterschiedlichen Frequenzen.\
In der westlichen Musik basieren die meisten Akkorde auf **Dreiklängen**, also drei Tönen, die aus einer Tonleiter nach festen **Intervallabständen** (in Halbtönen) aufgebaut sind.

```{list-table} Arten von Akkorden
:name: Arten von Akkorden
:header-rows: 1
:align: center

* - **Akkordtyp**
  - **Halbtonabstände**
  - **Charakter**
* - Dur (Major)
  - 0–4–7
  - hell, klar, stabil
* - Moll (Minor)
  - 0–3–7
  - weich, melancholisch
* - Vermindert (Dim)
  - 0–3–6
  - spannungsvoll
* - Übermäßig (Aug)
  - 0–4–8
  - schwebend
* - Sus2
  - 0-2-7
  - schwebend, offen
* - Sus4
  - 0-5-7
  - gespannt, auflösend
```

Die Zahlen geben die **Halbtonschritte** an, also Intervalle relativ zum Grundton.\
Diese Intervalle bestimmen den Klangcharakter:\
**Dur-Akkorde** klingen konsonant und stabil, **Moll-Akkorde** wirken weich oder traurig, während **vermindert** und **übermäßig** dissonante Spannungen erzeugen.\
Um später in Python nicht immer jeden einzelnen Ton eines Akkords angeben zu müssen legen wir uns ein Dictionary mit den gängigen Bezeichnungen für die verschiedenen Akkordarten an. So ist später auch die Eingabe von Synonymen, wie beispielsweise *Major* statt *Dur* zulässig.

```{code-block} python
:caption: Dictionary für Akkordbezeichnung
:name: Dictionary für Akkordbezeichnung
:linenos:

QUALITY_INTERVALS = {
    "major":      [0, 4, 7], "dur":  [0, 4, 7], "maj":          [0, 4, 7],
    "minor":      [0, 3, 7], "moll": [0, 3, 7], "min":          [0, 3, 7],
    "diminished": [0, 3, 6], "dim":  [0, 3, 6], "vermindert":   [0, 3, 6],
    "augmented":  [0, 4, 8], "aug":  [0, 4, 8], "uebermaessig": [0, 4, 8], "übermäßig": [0, 4, 8],
    "sus2":       [0, 2, 7],
    "sus4":       [0, 5, 7],
}
```

Dieses Dictionary sagt Python, welche Halbtöne (ausgehend vom Akkord-Grundton) aufaddiert werden müssen.
Das Ergebnis ist ein zusammengesetztes Signal, das im Zeitbereich wie ein mehrstimmiger Wellenzug aussieht:

$$x_{\text{mix}}(t) = \sum_{i=1}^{N} \red{A_{i}} \sin(2 \pi \purple{f_{i}} \green{t})$$

### Akkorde aus natürlicher Sprache extrahieren

Nun wollen wir eine Funktion bauen, die die Akkorde so entgegen nimmt, wie wir sie denken, also *"D4-Major"* oder *"A3-dur"*.
Dafür bauen wie einen **Parser**, der uns die natürliche Sprache so übersetzt, dass unser Python-Programm versteht, was es tun soll.

Dabei zerlegt ein **Regex** die Eingabe in Grundton (inkl. #/b und Oktave) und Akkordqualität ("major", "moll", "sus2", etc.).
Umlaute sind hierbei durch unser Dictionary (*siehe {numref}`Dictionary für Akkordbezeichnung`*) erlaubt.

```{code-block} python
:caption: Parsen des natürlichen Akkordaufrufs
:linenos:

# Grundton+Oktave | Trenner | Qualität(+2/4)
_CHORD_RE = re.compile(r"^\s*([A-Ga-g][#b]?-?\d+)\s*[-\s_]+\s*([A-Za-zäöüÄÖÜ]+[24]?)\s*$")

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
```

### Frequenzen der Akkorde berechnen

Wie bereits beschrieben ist ein Akkord ein **Intervallmuster relativ zum Grundton** (*siehe {numref}`Arten von Akkorden`*).
Wir müssen also die Frequenz des **Grundtons** bestimmen und von diesem ausgehen die Frequenzen der anderen Töne berechnen.
Die **gewählte Qualität** wird in Frequenzfaktoren $2^{\frac{k}{12}}$ umgerechnet und durch diese Faktoren können die Frequenzen der anderen Akkordtöne berechnet werden.

```{code-block} python
:caption: Frequenzen der Akkorde berechnen
:linenos:

def chord_frequencies(root_note: str, quality: str, A4: float = 440.0) -> list[float]:
    """Berechnet die Frequenzen aller Töne eines Akkords."""
    if quality not in QUALITY_INTERVALS:
        raise ValueError(f"Unbekannte Qualität {quality!r}. Erlaubt: {sorted(set(QUALITY_INTERVALS))}")

    f0 = note_to_freq(root_note, A4=A4)    # Grundfrequenz des Root-Notes berechnen
    intervals = QUALITY_INTERVALS[quality] # Halbton-Intervalle für die Akkordqualität

    return [f0 * (2.0 ** (k / 12.0)) for k in intervals] # Frequenzen aus Halbtonabständen berechnen
```

### Speichern der Akkorde als WAV

Nachdem die Frequenzen der einzelnen Akkordtöne bekannt sind, müssen diese im Zeitbereich kombiniert und in eine speicherbare Form gebracht werden.
Jede Stimme wird als Sinusschwingung erzeugt und anschließend addiert, genau das ist physikalisch die Überlagerung mehrerer Schwingungen.

Da jede Stimme $i$ ihre eigene Amplitude $\red{A_{i}}$ und Frequenz $\purple{f_{i}}$ besitzt können diese sich bei einer Überlagerung gegenseitig verstärken oder abschwächen.\
In der Physik nennt man das Interferenz:
- positive Überlagerung $\rightarrow$ Lauter,
- negative Überlagerung $\rightarrow$ Leiser.

Durch diese Überlagerung bekommen wir jedoch ein Problem.
Wenn wir alle Stimmen einfach mit voller Amplitude aufsummieren, kann der Maximalwert der Summe $x(t)$ größer als 1 (bzw. 32767 im 16-bit-Format) werden.\
Das führt zu Clipping. Dabei werden die Spitzen "hart" abgeschnitten, was den Klang verzerrt.

>**Beispiel**:\
>$x(t) = \sin(\dots) + \sin(\dots) + \sin(\dots)$\
>$\rightarrow$ mögliche Maximalamplitude $\approx 3$.\
>Bei 16-bit-Audio darf sie aber nur 1 sein (nach der Normierung).

Wir müssen also die Pegel pro Stimme reduzieren.
Deshalb teilen wir die Gesamtlautstärke durch die Anzahl der Stimmen:

$$\red{A_{i}} = \frac{\blue{A_\text{gesamt}}}{N}$$

Damit ist sichergestellt, dass die Summe nicht übersteuert, egal wie viele Stimmen gespielt werden.
Die Summe aller Maxima kann dann im schlimmsten Fall 1 ergeben (bei perfekter Phasenaddition).

Das ist eine einfache, robuste Heuristik.
Nicht perfekt lautheitslinear, aber sicher gegen Clipping und für synthetische Töne völlig ausreichend.

Damit ist das Programm nun in der Lage, aus mehreren Noten, oder direkt aus einem Akkordnamen, eine hörbare Klangdatei zu erzeugen.

```{code-block} python
:caption: Speichern der Akkorde als WAV
:linenos:

from typing import Sequence

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
```

### Komfortmethode für die Akkorderzeugung

Als letztes bauen wir uns noch einen kleinen Wrapper, also eine Komfortfunktion, die das Erzeugen von Akkorden vereinfacht und zugleich eine saubere API bereitstellt.

```{code-block} python
:caption: Komfortmethode für die Akkorderzeugung
:linenos:

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
```

```{code-block} python
:caption: Beispielcode: Akkorde erzeugen
:linenos:

# A-Dur (A4–C#5–E5)
make_named_chord_wav("A4-Major", 1.5, 44100, 0.9, "chord_A_major.wav")
# A-Moll (A4–C5–E5)
make_named_chord_wav("A4-minor", 1.5, 44100, 0.9, "chord_A_minor.wav")
# D-Dur (D4–F#4–A4), deutscher Alias „dur“ funktioniert ebenfalls:
make_named_chord_wav("D4-dur",   1.2, 44100, 0.9, "chord_D_major.wav")
# Sus-Beispiele:
make_named_chord_wav("D4-sus2",  1.2, 44100, 0.9, "chord_D_sus2.wav")
make_named_chord_wav("D4-sus4",  1.2, 44100, 0.9, "chord_D_sus4.wav")
```

Die aktualisierte Version mit Akkorderzeugung kann hier Heruntergeladen werden.

{download}`Vollständiger Code (Akkorde & Töne) <toene_erzeugen_code/04_akkord_name.py>`

## Obertöne und Klangfarbe

Ein reiner Sinuston klingt technisch sauber, aber zugleich künstlich und leblos.
Reale Instrumente erzeugen komplexe Schwingungen, die sich aus einer Vielzahl von **Obertönen** zusammensetzen.
Das sind Schwingungen, deren Frequenzen **ganzzahlige Vielfache der Grundfrequenz** $\purple{f_{0}}$ sind.
Diese Teilschwingungen überlagern sich gemäß dem Superpositionsprinzip und bilden zusammen den charakteristischen Klang eines Instruments, seine Klangfarbe (*Timbre*).

Mathematisch lässt sich ein solcher Klang als harmonische Reihe darstellen:

$$\blue{x(t)} = \sum_{k=1}^{N} \red{a_k} \sin(2\pi k \purple{f_{0}} \green{t})$$

Die Amplituden $\red{a_k}$ bestimmen, wie stark die jeweiligen Obertöne ausgeprägt sind.
Je nach Instrument fallen diese Werte ganz unterschiedlich aus. 

```{hint}
Die hier betrachteten Obertonspektren beschreiben den spektralen Aufbau eines Tons und sind ein wesentliches Merkmal seiner Klangfarbe.\
Jedoch genügt für eine realistische Nachbildung eines Instrumententons diese reine Obertonverteilung nicht.\
Einen Instrumententon prägen weitere Eigenschaften wie

- die **zeitliche Amplitudenhüllkurve**,
- **Inharmonizitäten** infolge von Materialsteifigkeit oder Schwingungsdispersion,
- **Modulationseffekte** wie Vibrato und Tremolo,
- sowie **Resonanzen** und räumliche Ausbreitung innerhalb des Instrumentenkörpers.

Diese Parameter wirken gemeinsam und erzeugen die komplexe Struktur eines realen Klangereignisses.
```

### Gewichtung der Obertöne

Wir definieren die Obertonstruktur über ein Dictionary, das jedem Instrument eine typische Amplitude-Verteilung zuordnet.

```{list-table} Obertöne unterschiedlicher Instrumente
:header-rows: 1
:align: center

* - **Instrument**
  - **1. Partial**
  - **2. Partial**
  - **3. Partial**
  - **4. Partial**
  - **5. Partial**
  - **6. Partial**
* - Flöte
  - 1,00
  - 0,20
  - 0,10
  - 0,05
  - –
  - –
* - Violine
  - 1,00
  - 0,70
  - 0,50
  - 0,30
  - 0,25
  - 0,15
* - Klavier
  - 1,00
  - 0,60
  - 0,35
  - 0,20
  - 0,12
  - 0,08
* - Tuba
  - 1,00
  - 0,10
  - 0,50
  - 0,05
  - 0,25
  - –
```

```{code-block} python
:caption: Obertöne unterschiedlicher Instrumente
:linenos:

INSTRUMENT_PARTIALS = {
    "floete":   {1: 1.00, 2: 0.20, 3: 0.10, 4: 0.05},                   # weich, fast sinusförmig
    "violine":  {1: 1.00, 2: 0.70, 3: 0.50, 4: 0.30, 5: 0.25, 6: 0.15}, # obertonreich, brillant
    "klavier":  {1: 1.00, 2: 0.60, 3: 0.35, 4: 0.20, 5: 0.12, 6: 0.08}, # harmonisch, leicht gedämpft
    "tuba":     {1: 1.00, 2: 0.10, 3: 0.50, 4: 0.05, 5: 0.25},          # tief, weich, ungerade betont
}
```

*Die hier angegebenen Oberton-Amplituden sind modellhafte Annäherungen typischer Verteilungen*\
*genaue Werte variieren je Instrument, Spielweise und Aufnahmebedingungen.*

Jeder Teilton wird mit seinem Gewicht $\red{a_k}$ **multipliziert**, um seine individuelle Amplitude festzulegen.
Anschließend werden alle **gewichteten** Sinusschwingungen **addiert**, um das Gesamtsignal zu bilden.

Aufbauend auf den bisherigen Grundlagen kann die Erzeugung von Obertönen im folgenden Skript nachvollzogen werden.
Die verwendeten Funktionen und Prinzipien entsprechen dabei den zuvor erläuterten Strukturen.

````{dropdown} hinzugefügter Quellcode: Töne mit Obertönen
:icon: code

```{literalinclude} toene_erzeugen_code/05_obertoene.py
:language: python
:linenos:
:lineno-match:
:lines: 85-163
```
````

```{code-block} python
:caption: Beispielcode: Töne mit Obertönen
:linenos:

# Vier Instrumentfarben auf demselben Grundton – A4
make_instrument_tone_wav("floete",  "A4", 1.0, 44100, 0.9, "floete_A4.wav")
make_instrument_tone_wav("violine", "A4", 1.0, 44100, 0.9, "violine_A4.wav")
make_instrument_tone_wav("klavier", "A4", 1.0, 44100, 0.9, "klavier_A4.wav")
make_instrument_tone_wav("tuba",    "A4", 1.0, 44100, 0.9, "tuba_A4.wav")

# Benutzerdefiniertes Spektrum (ungerade Obertöne stärker)
custom = {1: 1.0, 3: 0.8, 5: 0.5, 7: 0.3}
make_tone_with_partials("D4", 1.2, 44100, 0.9, "custom_D4.wav", partials=custom)
```

{download}`Vollständiger Code (Töne mit Obertönen) <toene_erzeugen_code/05_obertoene.py>`

## Akkorde mit Obertönen

Nun wollen wir den Code noch um die Funktion erweitern, Akkorde mit harmonischen Obertönen zu erzeugen.
Jede Stimme des Akkords wird dabei spektral geformt (Partials) und anschließend per Superposition summiert.
Die verwendeten Funktionen und Strukturen entsprechen den zuvor erläuterten Bausteinen und werden hier lediglich an den Akkordfall angepasst.

````{dropdown} hinzugefügter Quellcode: Töne mit Obertönen
:icon: code

```{literalinclude} toene_erzeugen_code/06_obertoene_akkorde.py
:language: python
:linenos:
:lineno-match:
:lines: 245-328
```
````

```{code-block} python
:caption: Beispielcode: Akkorde mit Obertönen
:linenos:

# C-Dur-Dreiklang mit „Violine“-Obertönen
make_named_chord_with_partials("C4-Major", 1.2, 44100, 0.9, "C4_maj_violine.wav", partials="violine")

# A-Moll-Dreiklang, flötenartig
make_named_chord_with_partials("A3-moll", 1.2, 44100, 0.9, "A3_min_floete.wav", partials="floete")

# Custom-Spektrum (ungerade Obertöne betont)
odd = {1:1.0, 3:0.7, 5:0.4, 7:0.25}
make_chord_with_partials(["D4","F#4","A4"], 1.0, 44100, 0.9, "D_maj_odd.wav", partials=odd)
```

{download}`Vollständiger Code (Akkorde & Töne mit Obertönen) <toene_erzeugen_code/06_obertoene_akkorde.py>`

