from pathlib import Path
from typing import Final
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
# from matplotlib.lines import Line2D
from matplotlib.pyplot import Figure

from plotutil.matplot.plot_maker import PlotMaker
from array import array
import numpy as np

class SingleAxisMatPlotMaker(PlotMaker):
    __figure : Figure
    __axes : Axes
    # __lines : dict[int, Line2D] #更に細かく制御する場合
    __x_min_array : array
    __x_max_array : array
    __y_min_array : array
    __y_max_array : array

    def __init__(self,
                 figsize : tuple[int, int]=(16, 9,),
                 dpi : int =128,
                 ) -> None:
        

        self.__set_plt_layout()
        self.__figure = Figure(
            figsize=figsize,
            dpi=dpi,
        )
        self.__axes = self.__figure.add_subplot(1,1,1)
        self.__add_drow()
        self.__x_max_array = array("f", [])
        self.__x_min_array = array("f", [])
        self.__y_max_array = array("f", [])
        self.__y_min_array = array("f", [])

        # 色々Axesのインスタンス生成方法あるけど
        # self.__figure, self.__axex = plt.subplot(1, 1, figsize=figsize)
        # self.__figure.set_dpi(dpi)
       
    def __set_plt_layout(self):
        # フォントの種類とサイズを設定する。
        plt.rcParams['font.size'] = 14
        plt.rcParams['font.family'] = 'Meiryo'
        # 目盛を内側にする。
        plt.rcParams['xtick.direction'] = 'in'
        plt.rcParams['ytick.direction'] = 'in'
        #補助目盛
        plt.rcParams["xtick.minor.visible"] = True

    def __add_drow(self,
                 line_style="--",
                 alpha=0.9,
                 ):
        self.__axes.grid(which='major',alpha=alpha)
        self.__axes.grid(which='minor',alpha=alpha, ls=line_style)
        self.__axes.yaxis.set_ticks_position('both')
        self.__axes.xaxis.set_ticks_position('both')

    def set_title(self, title: str, fontsize=14):
        self.__axes.set_title(title, fontsize=fontsize)

    def set_xlabel(self, xlabel: str, fontsize=14):
        self.__axes.set_xlabel(xlabel, fontsize=fontsize)

    def set_ylabel(self, ylabel: str, fontsize=14):
        self.__axes.set_ylabel(ylabel, fontsize=fontsize)

    def set_xlim(self, min_value:float, max_value:float):
        self.__axes.set_xlim(min_value,max_value)

    def set_ylim(self, min_value:float, max_value:float):
        self.__axes.set_ylim(min_value,max_value)

    def plot(self, x: list, y: list, alpha=1.0):
        self.__axes.plot(x, y, alpha=alpha)
        self.__x_min_array.insert(0, min(x))
        self.__x_max_array.insert(0, max(x))
        self.__y_min_array.insert(0, min(y))
        self.__y_max_array.insert(0, max(y))

    def set_midian_axis_lim(self):
        self.__axes.set_xlim(np.median(self.__x_min_array), np.median(self.__x_max_array))
        self.__axes.set_ylim(np.median(self.__y_min_array), np.median(self.__y_max_array))

    def invert_xaxis(self):
        self.__axes.invert_xaxis()

    def draw_x_range(self,min_value:float, max_value:float, alpha:float=0.3, color="rad"):
        x_min, x_max  = self.__axes.get_xlim()
        self.__axes.axvspan(min_value, max_value, alpha=alpha, color=color)
        self.__axes.set_xlim(x_min, x_max)

    def save(self, pngpath: Path):
        if self.__axes is None:
            raise Exception("Axesがありません。")
        self.__set_plt_layout()
        self.__figure.savefig(pngpath)

    def __del__(self):
        plt.close()
        