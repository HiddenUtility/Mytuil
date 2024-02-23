from pathlib import Path
from typing import Final
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.lines import Line2D
from matplotlib.pyplot import Figure

from pyutil.matplotutil.plot_maker import PlotMaker


class MultiPlotMaker(PlotMaker):
    __figure : Figure
    __axexs : dict[int, Axes]
    __lines_2ds : dict[int, dict[int, Line2D]]

    def __init__(self,
                 figsize : tuple[int, int]=(5, 4,),
                 dpi : int =64,
                 ) -> None:
        self.__figure = Figure(
            figsize=figsize,
            dpi=dpi,
        )
        __axexs = {}
        __lines_2ds = {}

    def __set_plt_layout(self):
        #色とかの微調整
        MAIN_FONT  :Final = 'Meiryo'
        FONT_SIZE_GRAPH  :Final = 14
        # フォントの種類とサイズを設定する。
        plt.rcParams['font.size'] = FONT_SIZE_GRAPH
        plt.rcParams['font.family'] = MAIN_FONT
        # 目盛を内側にする。
        plt.rcParams['xtick.direction'] = 'in'
        plt.rcParams['ytick.direction'] = 'in'
        #補助目盛
        plt.rcParams["xtick.minor.visible"] = True

    def plot(self, pngpath: Path):
        self.__set_plt_layout()
        self.__figure.savefig(pngpath)