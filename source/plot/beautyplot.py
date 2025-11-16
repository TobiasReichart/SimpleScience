from __future__ import annotations
from dataclasses import dataclass, field
from typing import Literal

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.ticker import FuncFormatter, MaxNLocator


@dataclass
class PlotStyle:
    """
    Kleine Hilfsklasse, um Matplotlib-Plots konsistent und hübsch zu formatieren.

    Features:
    ----------
    - Globale Schrift-Einstellungen (set_font)
    - Einheitliches Achsen-Layout (beauty / style_axes)
    - Dezimalkomma-Formatter für Achsen (set_decimal_comma)
    - Achsenkreuz durch den Ursprung (origin_axes)
    """
    background_color: str = "#f5f5f5"  # Standard-Hintergrundfarbe der Axes
    colors: dict[str, str] = field(default_factory=lambda: {
        "red":    "#D62728",
        "blue":   "#1F77B4",
        "green":  "#2CA02C",
        "orange": "#FF7F0E",
        "purple": "#9467BD",
        "cyan":   "#17BECF",
        "teal":   "#2AA198",
        "gray":   "#6E6E6E",
    })
    figure_transparent: bool = True     # nur der Rand außerhalb der Axes

    # ------------------------------------------------------------------
    #  Globale Schrift-/Typografie-Einstellungen
    # ------------------------------------------------------------------
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
        """
        Setzt globale Matplotlib-Schrifteinstellungen.

        Hinweis: wirkt global über rcParams, sollte daher am Anfang
        eines Skripts/Notebooks aufgerufen werden.
        """
        plt.rcParams.update({
            "text.usetex": False,        # hier erstmal ohne LaTeX
            "font.family":  family,
            "font.weight":  weight,
            "font.style":   style,
            "font.size":    size,        # Basisschriftgröße
            "axes.titlesize":   subtitlesize,
            "axes.labelsize":   labelsize,
            "xtick.labelsize":  labelsize,
            "ytick.labelsize":  labelsize,
            "legend.fontsize":  legendsize,
            "figure.titlesize": titlesize,
        })

    # ------------------------------------------------------------------
    #  Achsenlayout „aufhübschen“ (Gitter, Spines, Ticks, Hintergrund)
    # ------------------------------------------------------------------
    def beauty(self, fig: Figure, ax: Axes) -> None:
        """
        Wendet ein einheitliches, „schönes“ Layout auf eine Achse an.
        """
        # Haupt-Ticks
        ax.tick_params(
            axis="both",
            which="major",
            direction="inout",
            length=10,
            width=1,
        )

        # Neben-Ticks
        ax.minorticks_on()
        ax.tick_params(
            axis="both",
            which="minor",
            direction="inout",
            length=5,
            width=0.8,
            color="gray",
        )

        # Rahmen (Spines)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_linewidth(1)
        ax.spines["bottom"].set_linewidth(1)

        # Grid + Hintergrund
        ax.grid(True, linestyle=":", linewidth=0.5, alpha=1.0)
        ax.set_facecolor(self.background_color)

        # Figure-Hintergrund außerhalb der Axes
        if self.figure_transparent:
            fig.patch.set_alpha(0.0)

    # ------------------------------------------------------------------
    #  Dezimalkomma-Formatter für Achsen (x, y oder beide)
    # ------------------------------------------------------------------
    def set_decimal_comma(
        self,
        ax: Axes,
        axis: Literal["x", "y", "both"] = "both",
        decimals: int | tuple[int, int] = 2,
        *,
        minor: bool = False,
    ) -> None:
        """
        Setzt einen Dezimalkomma-Formatter ('.' → ',') auf x-, y- oder beide Achsen.

        Parameters
        ----------
        ax : Axes
            Ziel-Achse.
        axis : {'x', 'y', 'both'}
            Welche Achsen formatiert werden sollen.
        decimals : int oder (int, int)
            int  -> gleiche Nachkommastellen für x und y
            (dx, dy) -> getrennte Nachkommastellen für x- und y-Achse
        minor : bool
            Falls True, werden auch die Minorticks formatiert.
        """
        dec_x, dec_y = self._resolve_decimals(decimals)  # None ist hier nicht erlaubt, aber schadet nicht

        fmt_x = self._make_comma_formatter(dec_x if dec_x is not None else 0)
        fmt_y = self._make_comma_formatter(dec_y if dec_y is not None else 0)

        if axis in ("x", "both"):
            ax.xaxis.set_major_formatter(fmt_x)
            if minor:
                ax.xaxis.set_minor_formatter(fmt_x)

        if axis in ("y", "both"):
            ax.yaxis.set_major_formatter(fmt_y)
            if minor:
                ax.yaxis.set_minor_formatter(fmt_y)

    # ------------------------------------------------------------------
    #  Convenience: beauty + optional Dezimalkomma
    # ------------------------------------------------------------------
    def style_axes(
        self,
        fig: Figure,
        ax: Axes,
        *,
        comma_axis: Literal["x", "y", "both", "none"] = "none",
        decimals: int | tuple[int, int] = 2,
        minor: bool = False,
    ) -> None:
        """
        Kombiniert 'beauty' und optional den Dezimalkomma-Formatter.

        Parameters
        ----------
        fig : Figure
            Figure, zu der die Achse gehört.
        ax : Axes
            Ziel-Achse.
        comma_axis : {'x', 'y', 'both', 'none'}
            Welche Achse(n) im Dezimalkommaformat angezeigt werden sollen.
        decimals : int oder (int, int)
            Nachkommastellen für x/y.
        minor : bool
            Auch Minorticks formatieren.
        """
        self.beauty(fig, ax)
        if comma_axis != "none":
            self.set_decimal_comma(ax, axis=comma_axis, decimals=decimals, minor=minor)

    # ------------------------------------------------------------------
    #  Achsen durch den Ursprung legen („Origin Plot“)
    # ------------------------------------------------------------------
    def origin_axes(
        self,
        fig: Figure,
        ax: Axes,
        *,
        comma_axis: Literal["x", "y", "both", "none"] = "both",
        decimals: int | tuple[int, int] | None = None,
        comma: bool = True,
        hide_zero_tick: bool = True,
        prune_ends: bool = False,
    ) -> None:
        """
        Legt x- und y-Achse durch den Ursprung und formatiert Ticks.

        Parameters
        ----------
        fig, ax : Figure, Axes
            Ziel-Figure und -Achse.
        comma_axis : {'x', 'y', 'both', 'none'}
            Welche Achsen im Dezimalkommaformat angezeigt werden sollen.
        decimals : int | (int, int) | None
            Nachkommastellen:
            - int       -> gleiche Stellen für x und y
            - (dx, dy)  -> getrennt für x und y
            - None      -> Standardformatierung (g-Format)
        comma : bool
            Ob '.' durch ',' ersetzt werden soll.
        hide_zero_tick : bool
            Tick-Beschriftung bei 0 ausblenden (sauberes Achsenkreuz).
        prune_ends : bool
            Äußerste Major-Ticks „abknipsen“ (MaxNLocator(prune="both")).
        """
        # allgemeinen Style anwenden
        self.beauty(fig, ax)

        # Achsen durch den Ursprung
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_position("zero")
        ax.spines["bottom"].set_position("zero")
        ax.spines["left"].set_linewidth(1)
        ax.spines["bottom"].set_linewidth(1)

        # Daten analysieren → ggf. Limits anpassen
        xs, ys = self.get_all_xy(ax)
        if xs.size > 0 and np.all(xs > 0):
            ax.set_xlim(left=0.0)
        if ys.size > 0 and np.all(ys > 0):
            ax.set_ylim(bottom=0.0)

        # äußerste Ticks abschneiden
        if prune_ends:
            ax.xaxis.set_major_locator(MaxNLocator(prune="both"))
            ax.yaxis.set_major_locator(MaxNLocator(prune="both"))

        # Dezimalstellen für x / y getrennt bestimmen
        dec_x, dec_y = self._resolve_decimals(decimals)

        # Formatter nur für die gewünschten Achsen setzen
        if comma_axis in ("x", "both"):
            fmt_x = self._make_origin_formatter(dec_x, comma=comma, hide_zero=hide_zero_tick)
            ax.xaxis.set_major_formatter(fmt_x)

        if comma_axis in ("y", "both"):
            fmt_y = self._make_origin_formatter(dec_y, comma=comma, hide_zero=hide_zero_tick)
            ax.yaxis.set_major_formatter(fmt_y)

    # ------------------------------------------------------------------
    #  Hilfsfunktionen: Daten auslesen & Formatter
    # ------------------------------------------------------------------
    @staticmethod
    def get_all_xy(ax: Axes) -> tuple[np.ndarray, np.ndarray]:
        """
        Sammelt alle x- und y-Daten aus Linien und Scatter-Collections der Achse.

        Rückgabe:
        ---------
        xs, ys : np.ndarray
            Arrays mit allen gefundenen x- und y-Werten.
        """
        xs: list[float] = []
        ys: list[float] = []

        # Linien (ax.plot)
        for line in ax.get_lines():
            xs.extend(line.get_xdata())
            ys.extend(line.get_ydata())

        # Scatter (ax.scatter) -> Collections mit Offsets
        for col in ax.collections:
            offsets = col.get_offsets()
            if len(offsets) > 0:
                xs.extend(offsets[:, 0])
                ys.extend(offsets[:, 1])

        if not xs:
            return np.array([]), np.array([])
        return np.asarray(xs), np.asarray(ys)

    @staticmethod
    def _format_decimal_comma(x: float, decimals: int) -> str:
        """
        Formatiert eine Zahl mit fester Nachkommastellenzahl und Dezimalkomma.
        """
        if not np.isfinite(x):
            return ""
        s = f"{x:.{decimals}f}"
        return s.replace(".", ",")

    @staticmethod
    def _make_comma_formatter(decimals: int) -> FuncFormatter:
        """
        Erzeugt einen FuncFormatter mit Dezimalkomma und fester Stellenzahl.
        """
        return FuncFormatter(
            lambda val, pos: PlotStyle._format_decimal_comma(val, decimals)
        )

    @staticmethod
    def _make_origin_formatter(
        decimals: int | None,
        *,
        comma: bool,
        hide_zero: bool,
    ) -> FuncFormatter:
        """
        Formatter für Origin-Achsen:
        - optional Dezimalkomma
        - optional 0-Tick ohne Label
        - optionale Nachkommastellen (None => Standardformat)
        """
        def _fmt(x: float, pos: int) -> str:
            # NaN / Inf ausblenden
            if not np.isfinite(x):
                return ""

            # 0 optional ohne Label
            if hide_zero and np.isclose(x, 0.0):
                return ""

            # Basisformat
            if decimals is None:
                s = f"{x:g}"
            else:
                s = f"{x:.{decimals}f}"

            # Punkt → Komma
            if comma:
                s = s.replace(".", ",")

            return s

        return FuncFormatter(_fmt)
    
    @staticmethod
    def _resolve_decimals(
        decimals: int | tuple[int, int] | None
    ) -> tuple[int | None, int | None]:
        """
        Konvertiert eine Dezimalstellen-Angabe in (dec_x, dec_y).

        - int       -> (int, int)
        - (dx, dy)  -> (dx, dy)
        - None      -> (None, None)
        """
        if decimals is None:
            return None, None
        if isinstance(decimals, int):
            return decimals, decimals
        if isinstance(decimals, tuple) and len(decimals) == 2:
            return decimals[0], decimals[1]
        raise ValueError(
            f"Erwartet int, tuple[int, int] oder None, erhalten: {decimals!r} "
            f"(Typ: {type(decimals)})"
        )