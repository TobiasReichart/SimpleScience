import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Domain
L = np.pi
x = np.linspace(-L, L, 2000)

# Original functions
def rect(x):
    return np.where(x >= 0, 1, -1)

def saw(x):
    return x / L

# Fourier coefficients
def b_rect(n):
    if n % 2 == 1:  # ungerade n
        return 4 / (n * np.pi)
    return 0

def b_saw(n):
    return 2 * ((-1)**(n+1)) / (n * np.pi)

# partial sums
def fourier_rect(N):
    s = np.zeros_like(x)
    for n in range(1, N+1):
        s += b_rect(n) * np.sin(n * x)
    return s

def fourier_saw(N):
    s = np.zeros_like(x)
    for n in range(1, N+1):
        s += b_saw(n) * np.sin(n * x)
    return s

# figure setup
fig = make_subplots(rows=1, cols=2, subplot_titles=("Rechteck", "Sägezahn"))

# initial plots N=1
fig.add_trace(go.Scatter(x=x, y=rect(x), name="Original", line=dict(color="black")), 1, 1)
fig.add_trace(go.Scatter(x=x, y=fourier_rect(1), name="Fourier Näherung", line=dict(color="red")), 1, 1)

fig.add_trace(go.Scatter(x=x, y=saw(x), name="Original", line=dict(color="black")), 1, 2)
fig.add_trace(go.Scatter(x=x, y=fourier_saw(1), name="Fourier Näherung", line=dict(color="red")), 1, 2)

# animation frames
frames = []
for N in range(1, 40):
    frames.append(go.Frame(
        data=[
            go.Scatter(y=fourier_rect(N)),
            go.Scatter(y=fourier_saw(N))
        ],
        name=str(N)
    ))

# slider
sliders = [{
    "steps": [{
        "method": "animate",
        "args": [[str(N)], {"mode": "immediate", "frame": {"duration": 0}}],
        "label": str(N)
    } for N in range(1, 40)],
    "currentvalue": {"prefix": "N = "}
}]

fig.update_layout(
    title="Fourier-Reihe von Rechteck- und Sägezahnspannung",
    sliders=sliders,
    updatemenus=[{
        "type": "buttons",
        "buttons": [{
            "label": "Play",
            "method": "animate",
            "args": [None, {"frame": {"duration": 80}}]
        }]
    }]
)

fig.show()