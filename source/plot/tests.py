from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from beautyplot import PlotStyle

ps = PlotStyle(figure_transparent=False, background_color="#FFFFFF")

def sin_period(
        T: int = 1,
        n: int = 101
) -> tuple[np.ndarray, np.ndarray]:
    t = np.linspace(0, T*2*np.pi, n)
    x = np.sin(t)
    return (t, x)

    

def normal_plot():
    fig, ax = plt.subplots(1, 1, figsize=(5, 5))

    ps.set_font() # Schriftart setzen

    t, x = sin_period()

    ax.plot(t, x, linewidth=2., color=ps.colors["blue"], label=f"Sinus")

    # --- Achseneinstellungen ---
    ax.set_xlim(left=min(t), right=max(t))
    ax.set_ylim(bottom=min(x)*1.2, top=max(x)*1.2)
    ax.legend()

    ps.style_axes(fig, ax, comma_axis="both", decimals=(1,2))
    fig.tight_layout()
    plt.show()

def origin_plot():
    ps = PlotStyle()
    ps.set_font(family="sans", size=12)

    x = np.linspace(-2, 3, 400)
    y = x**3 - x

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot(x, y, color=ps.colors["blue"], lw=2, label="Funktion")

    ps.origin_axes(
        fig, ax,
        comma_axis="both",       # x und y formatieren
        decimals=(1, 2),         # x: 1 Nachkommastelle, y: 2
        comma=True,
        hide_zero_tick=True,
        prune_ends=True,
    )

    ax.set_title(r"Polynom mit Achsen durch den Ursprung")
    ax.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    #normal_plot()
    origin_plot()