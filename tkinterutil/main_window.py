import tkinter

class MainWindow(tkinter.Tk):
    def __init__(self, screenName: str | None = None, 
                 baseName: str | None = None, 
                 className: str = "Tk", 
                 useTk: bool = True, 
                 sync: bool = False, 
                 use: str | None = None
                 ) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.__create_freame()

    def __create_freame(self):
        ...

