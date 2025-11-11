from __future__ import annotations
from dataclasses import dataclass
from typing import Literal

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.ticker import FuncFormatter

# ----------------------------------------------------------------------
# Hilfsfunktionen
# ----------------------------------------------------------------------
def _format_decimal_comma(x: float, decimals: int) -> str:
    """Formatiert eine Zahl mit fester Nachkommastellenzahl und Dezimalkomma."""
    if not np.isfinite(x):
        return ""  # NaN/Inf ausblenden
    s = f"{x:.{decimals}f}"
    return s.replace(".", ",")

def make_comma_formatter(decimals: int) -> FuncFormatter:
    """Erzeugt einen FuncFormatter mit Dezimalkomma und fester Stellenzahl."""
    return FuncFormatter(lambda val, pos: _format_decimal_comma(val, decimals))

# ----------------------------------------------------------------------
# PlotStyle-Klasse
# ----------------------------------------------------------------------
@dataclass
class PlotStyle:
    background_color: str = "#f5f5f5"
    colors: dict = None
    figure_transparent: bool = True  # nur der Rand außerhalb der Axes

    def __post_init__(self):
        if self.colors is None:
            self.colors = {
                "red":    "#D62728",
                "blue":   "#1F77B4",
                "green":  "#2CA02C",
                "orange": "#FF7F0E",
                "purple": "#9467BD",
                "cyan":   "#17BECF",
                "teal":   "#2AA198",
                "gray":   "#6E6E6E",
            }

    # ---------- Global: Schrift/Typografie ----------
    def set_font(
        self,
        family: str = "serif",
        weight: str = "normal",
        style: str = "normal",
        size: int = 12,
        subtitlesize: int = 16,
        labelsize: int = 12,
        legendsize: int = 12,
        titlesize: int = 18,
    ) -> None:
        plt.rcParams.update({
            "text.usetex": False,
            "font.family": family,
            "font.weight": weight,
            "font.style":  style,
            "font.size":   size,
            "axes.titlesize":   subtitlesize,
            "axes.labelsize":   labelsize,
            "xtick.labelsize":  labelsize,
            "ytick.labelsize":  labelsize,
            "legend.fontsize":  legendsize,
            "figure.titlesize": titlesize,
        })

    # ---------- Achsen „aufhübschen“ ----------
    def beauty(self, fig: Figure, ax: Axes) -> None:
        ax.tick_params(axis="both", which="major", direction="inout", length=10, width=1)
        ax.minorticks_on()
        ax.tick_params(axis="both", which="minor", direction="inout", length=5, width=0.8, color="gray")

        # Rahmen
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_linewidth(1)
        ax.spines["bottom"].set_linewidth(1)

        # Grid + Hintergrund
        ax.grid(True, linestyle=":", linewidth=0.5, alpha=1.0)
        ax.set_facecolor(self.background_color)

        # Figure-Hintergrund transparent (nur außerhalb der Axes)
        if self.figure_transparent:
            fig.patch.set_alpha(0.0)

    # ---------- Dezimalkomma-Formatter anwenden ----------
    def set_decimal_comma(
        self,
        ax: Axes,
        axis: Literal["x", "y", "both"] = "both",
        decimals: int = 2,
        *,
        minor: bool = False,
    ) -> None:
        """
        Setzt einen Dezimalkomma-Formatter auf x-, y- oder beide Achsen.

        Parameters
        ----------
        ax : Axes
            Ziel-Achse.
        axis : 'x' | 'y' | 'both'
            Welche Achse formatiert werden soll.
        decimals : int
            Anzahl Nachkommastellen für die Hauptticks.
        minor : bool
            Falls True, wird derselbe Formatter auch für Minorticks gesetzt.
        """
        fmt = make_comma_formatter(decimals)
        if axis in ("x", "both"):
            ax.xaxis.set_major_formatter(fmt)
            if minor:
                ax.xaxis.set_minor_formatter(fmt)
        if axis in ("y", "both"):
            ax.yaxis.set_major_formatter(fmt)
            if minor:
                ax.yaxis.set_minor_formatter(fmt)

    # ---------- Bequem: alles in einem Rutsch ----------
    def style_axes(
        self,
        fig: Figure,
        ax: Axes,
        *,
        comma_axis: Literal["x", "y", "both", "none"] = "none",
        decimals: int = 2,
        minor: bool = False,
    ) -> None:
        """
        Kombiniert 'beauty' und optional Dezimalkomma-Formatter.
        """
        self.beauty(fig, ax)
        if comma_axis != "none":
            self.set_decimal_comma(ax, axis=comma_axis, decimals=decimals, minor=minor)
