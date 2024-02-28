
from plotly.graph_objects import Figure, Scatter
from array import array
from pathlib import Path

class SingleAxisPlotlyPlotMaker:
    __figure : Figure
    __sxatter : Scatter
    __x_min_array : array
    __x_max_array : array
    __y_min_array : array
    __y_max_array : array

    def __init__(self,) -> None:
        self.__figure = Figure()
        self.__x_max_array = array("f", [])
        self.__x_min_array = array("f", [])
        self.__y_max_array = array("f", [])
        self.__y_min_array = array("f", [])

    def set_title(self, title: str,fontsize=14):
        self.__figure.update_layout(title=title)

    def set_xlabel(self, xlabel: str, fontsize=14):
        '''軸名を設定します。'''
        self.__figure.update_layout(
            xaxis=dict(
                title=xlabel,
                # font=dict(size=fontsize),
                )
        )

        
    def set_ylabel(self, ylabel: str, fontsize=14):
        '''軸名を設定します。'''
        self.__figure.update_layout(
            yaxis=dict(
                title=ylabel,
                # font=dict(size=fontsize),
                )
        )


    def plot(self, x: list, y: list, alpha=1.0):
        scatter = Scatter(
            x=x, 
            y=y, 
            mode = "lines",
        )
        self.__figure = self.__figure.add_trace(scatter)
        self.__x_min_array.insert(0, min(x))
        self.__x_max_array.insert(0, max(x))
        self.__y_min_array.insert(0, min(y))
        self.__y_max_array.insert(0, max(y))



    def invert_xaxis(self):
        self.__figure.update_xaxes(autorange='reversed')



    def save(self, htmlpath: Path):
        self.__figure.write_html(htmlpath)


        