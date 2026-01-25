from pathlib import Path

# -- Hilfsfunktion: source-Verzeichnis finden ----------------------------------
def _find_source_dir(start: Path | None = None) -> Path:
    """Geht vom Skript nach oben und gibt den Ordner 'source' zurück."""
    here = (start or Path(__file__).resolve())
    for p in [here] + list(here.parents):
        if p.name == "source":
            return p
    raise RuntimeError("Kein 'source'-Ordner in den übergeordneten Pfaden gefunden.")

# -- source auf sys.path + Pfade ableiten --------------------------------------
SOURCE_DIR = _find_source_dir()

# Ausgabe-Verzeichnis für Plots relativ zu source/
FIG_DIR = SOURCE_DIR / "_static" / "plots" / "analysis" / "transformationen" / "fourier-reihe"
FIG_DIR.mkdir(parents=True, exist_ok=True)

HERE = Path(__file__).resolve()
HTML_PATH = FIG_DIR / (HERE.stem + ".html")

MATHJAX = SOURCE_DIR / "_static" / "js" / "mathjax" / "tex-chtml-full.js"

# ==============================================================================
# Plot erstellen
# ==============================================================================
import numpy as np                          # Numerische Berechnung
import plotly.graph_objects as go           # Plots (allgemein)
from plotly.subplots import make_subplots   # Subplots

# -- Hilfsfunktionen -----------------------------------------------------------
def sig(x):
    """punktsymmetrische Rampensignal (ungerade)"""
    x = np.asarray(x, dtype=float)          # x als NumPy-Array
    x_mod = ((x + 1) % 2) - 1               # Phase in [-1, 1)
    return 0.5 * x_mod

def cosine_components(x_eval, DC, A, phi, omega0, x0, n_terms=None):
    """
    Berechnet die Kosinus-Terme der Fourier-Reihe:
    comps[0, :] = Gleichanteil
    comps[k, :] = k-te Harmonische (k = 1, ..., n_terms)
    """
    x_eval = np.asarray(x_eval, dtype=float)    # Stützstellen in NumPy-Array
    if n_terms is None or n_terms > len(A):     # n_terms ggf. begrenzen
        print(f"Anzahl der Harmonischen wurde von {n_terms} auf {len(A)} angepasst")
        n_terms = len(A)                        # maximale Anzahl setzen

    N_x = x_eval.size                           # Anzahl der x-Stützstellen
    comps = np.zeros((n_terms + 1, N_x), float) # 2D-Array: (DC + n_terms, N_x)
    comps[0, :] = DC                            # Zeile 0: reiner Gleichanteil

    t = x_eval - x0                             # Zeitachse relativ zu x0

    for idx in range(n_terms):                  # Schleife über Harmonische
        k = idx + 1                             # k = 1, 2, ..., n_terms
        comps[idx + 1, :] = A[idx] * np.cos(    # WICHTIG: + phi[idx]
            k * omega0 * t + phi[idx]
        )

    return comps

# -- Signal für die FFT (eine Periode) -----------------------------------------
x_fft = np.linspace(-1, 1, 500)  # Stützstellen im Intervall [-1, 1]
y_fft = sig(x_fft)               # Rampensignal an diesen Stellen

# -- FFT für Fourier-Koeffizienten ---------------------------------------------
N = len(x_fft)                  # Anzahl der Stützstellen
dt = x_fft[1] - x_fft[0]        # Schrittweite Δt
T = N * dt                      # Länge des FFT-Intervalls ≈ Periodenlänge
x0 = x_fft[0]                   # Startpunkt (für die Phasenlage)

Y = np.fft.fft(y_fft)           # FFT des Signals
DC = Y[0].real / N              # Gleichanteil (Mittelwert)

k_max = N // 2                  # Maximal nutzbare Harmonische (Nyquist)
A = 2 * np.abs(Y[1:k_max]) / N  # Amplituden der Kosinus-Terme (ohne DC)
phi = np.angle(Y[1:k_max])      # Phasen der Kosinus-Terme
omega0 = 2 * np.pi / T          # Grundkreisfrequenz ω0 = 2π / T

# -- Anzahl der Harmonischen für den Slider ------------------------------------
n_terms_slider = 10                     # Slider soll 0..10 anzeigen
n_terms = min(n_terms_slider, len(A))   # Sicherheitsbegrenzung

# -- x-Achse für die Darstellung (-3..3, mehrere Perioden) ---------------------
x_sig = np.linspace(-3, 3, 1000)    # Stützstellen für beide Plots
y_sig = sig(x_sig)                  # Original-Rampensignal auf [-3, 3]

# -- Kosinus-Komponenten auf x_sig berechnen -----------------------------------
comps = cosine_components(x_sig, DC, A, phi, omega0, x0, n_terms=n_terms)

# -- Partielle Summen (DC + 1..n Harmonische) vorbereiten ----------------------
y_approx_list = []                            # Liste der Approximationen
for n in range(n_terms + 1):                  # n = 0..n_terms
    y_approx_n = np.sum(comps[0:n+1, :], axis=0)  # Summe Zeilen 0..n
    y_approx_list.append(y_approx_n)

# -- Plot ----------------------------------------------------------------------
fig = make_subplots(
    rows=1, # Eine Zeile
    cols=2, # mit zwei Spalten
    subplot_titles=("Fourier-Komponenten", "Rampensignal + Approximation"), # Diagrammtitel
    horizontal_spacing=0.15,   # mehr Abstand zwischen den Plots
)

for ann in fig.layout.annotations:
    ann.update(
        y=ann.y + 0.1,     # relative Verschiebung nach oben (0..1 im Plotbereich)
        yanchor="bottom",   # Referenzpunkt unten an den Text legen
    )
# -- Linker Plot -----------------------
colors = [
    "#1f77b4",  # k=1
    "#ff7f0e",  # k=2
    "#2ca02c",  # k=3
    "#d62728",  # k=4
    "#9467bd",  # k=5
    "#8c564b",  # k=6
    "#e377c2",  # k=7
    "#7f7f7f",  # k=8
    "#bcbd22",  # k=9
    "#17becf",  # k=10
]
# Trace 0: DC-Komponente links
fig.add_trace(
    go.Scatter(
        x=x_sig,
        y=comps[0, :],
        mode="lines",
        line=dict(width=2, color="#000000"),
        name="DC",
        visible=True,   # bleibt immer sichtbar
        showlegend=False,
    ),
    row=1, col=1,
)
# Traces 1..n_terms: k-te Harmonische links
for k in range(1, n_terms + 1):
    fig.add_trace(
        go.Scatter(
            x=x_sig,
            y=comps[k, :],          # k-te Komponente
            mode="lines",
            line=dict(width=1, color=colors[k-1]),
            name=f"k = {k}",
            visible=False,
            showlegend=False,
        ),
        row=1, col=1,
    )

# -- Rechter Plot ----------------------
fig.add_trace(
    go.Scatter(
        x=x_sig,
        y=y_sig,
        mode="lines",
        line=dict(width=2, color="#1f77b4"),
        name="Rampensignal",
    ),
    row=1, col=2,
)

# Für jede Sliderposition ein eigener Summen-Trace, der per Slider ein-/ausgeblendet wird.
for n in range(n_terms + 1):
    fig.add_trace(
        go.Scatter(
            x=x_sig,
            y=y_approx_list[n],
            mode="lines",
            line=dict(width=2, color="#d62728"),
            name=f"Approximation",
            visible=(n == 0),
            showlegend=True,
        ),
        row=1, col=2,
    )

# -- Slider definieren ---------------------------------------------------------
# Trace-Indizes:
#   0              : DC links
#   1 .. n_terms   : Harmonische links
#   n_terms+1      : Rampe rechts
#   n_terms+2 .. n_terms+2+n_terms : Summen rechts (n=0..n_terms)

total_traces = 2 * n_terms + 3          # Gesamtanzahl Traces
sum_start = n_terms + 2                 # Startindex Summen rechts
square_idx = n_terms + 1                # Index Rampe rechts

steps = []                              # Slider-Schritte

for n in range(n_terms + 1):            # n = 0..n_terms
    visible = [False] * total_traces    # alles zunächst unsichtbar

    # Links: DC immer sichtbar
    visible[0] = True

    # Links: Harmonische 1..n sichtbar
    for k in range(1, n_terms + 1):
        if k <= n:
            visible[k] = True

    # Rechts: Rampe immer sichtbar
    visible[square_idx] = True

    # Rechts: genau eine Summenkurve sichtbar (entsprechend Sliderposition)
    for j in range(n_terms + 1):
        idx = sum_start + j             # Index des j-ten Summen-Traces
        visible[idx] = (j == n)         # nur j == n sichtbar

    step = dict(
        method="update",                # nur Sichtbarkeiten updaten
        args=[{"visible": visible}],
        label=str(n)
    )
    steps.append(step)

sliders = [dict(
    active=0,
    currentvalue={"prefix": "Anzahl Harmonische n = "},
    pad={"t": 60},       # mehr Abstand nach oben (zu den Achsen)
    x=0.5, xanchor="center",
    y=-0.05, yanchor="top",   # dichter unter die Figur statt -0.1
    steps=steps
)]

# -- Layout Einstellungen --------------
fig.update_layout(
    template="plotly_white",    # Theme
    separators=",.",            # deutsches Dezimalformat
    showlegend=True,
    legend=dict(
        orientation="h",
        x=0.75,          # eher über dem rechten Plot
        xanchor="center",
        y=1.25,          # knapp unterhalb des oberen Randes
        yanchor="bottom",
    ),
    sliders=sliders             # Slider zum Layout hinzufügen
)

# -- Alle Achsen gleichermaßen bearbeiten ---
axis_grid = dict(
    showgrid=True,         # Gitterlinien einblenden
    gridcolor="#dddddd", # Farbe der Gitterlinien
    gridwidth=1,           # Linienstärke
    griddash="dot",        # Linienstil: "solid", "dot", "dash", ...
)
axis_minorgrid = dict(
    showgrid=True,          # Minorgrid einblenden
    gridcolor="#eeeeee",  # Farbe der Gitterlinien
)
fig.update_xaxes(               # x-Achsen-Einstellungen
        title="t [s]",          # Titel
        range=[-3., 3.],        # sichtbarer Bereich
        **axis_grid,            # Grid-Style
        minor=axis_minorgrid,   # Minorgrid
)
fig.update_yaxes(               # y-Achsen-Einstellungen
        title="Amplitude",      # Titel
        range=[-0.55, 0.55],        # sichtbarer Bereich
        **axis_grid,            # Grid-Style
        minor=axis_minorgrid,   # Minorgrid
)

# -- Export --------------------------------------------------------------------
fig.write_html(
    HTML_PATH,
    include_plotlyjs=True,     # Plotly lokal
    include_mathjax="../../../js/mathjax/tex-chtml-full.js",   # MathJax lokal
    full_html=True
)
print(f"Unter {HTML_PATH} abgespeichert")