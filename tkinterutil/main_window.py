import tkinter
from tkinter import Frame
from tkinterutil.path_insert_frame import PathInsertFrame
from tkinterutil.date_insert_frame import DateInsertFrame
from tkinterutil.running_button_frame import RunningButtonFrame


class MainWindow(tkinter.Tk):
    __path_frame : PathInsertFrame
    __date_frame : DateInsertFrame
    def __init__(self, screenName: str | None = None, 
                 baseName: str | None = None, 
                 className: str = "Tk", 
                 useTk: bool = True, 
                 sync: bool = False, 
                 use: str | None = None
                 ) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title("MainFrame")
        self.__main_frame = Frame(self)
        self.__create_freame()

    def __create_freame(self):
        self.__path_frame = PathInsertFrame(self.__main_frame)
        self.__date_frame = DateInsertFrame(self.__main_frame)
        self.__button_frame = RunningButtonFrame(self.__main_frame,
                                                 self.__path_frame,
                                                 self.__date_frame,
                                                 )
        self.__path_frame.show()
        self.__date_frame.show()
        self.__button_frame.show()
        self.__main_frame.pack(anchor="w")
