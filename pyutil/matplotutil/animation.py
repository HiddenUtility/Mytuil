from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
# import matplotlib.pyplot as plt
from matplotlib.pyplot import Figure
import numpy as np
import tkinter
from tkinter import Frame
from tkinter import Button

class Application(tkinter.Tk):
    def __init__(self, master = None):
        super().__init__(master)
        self.title('MatplotlibAnime in tkinter')
        # self.geometry("800x800")
        self.__create_frame()
        self.__init()

        
    def __create_frame(self):
        self.__canvas_frame = Frame(master=self)
        self.__canvas_frame.pack(side=tkinter.LEFT) # expand = True
        self.__control_frame = Frame(master=self)
        self.__control_frame.pack(side=tkinter.RIGHT)
        
    def __init(self):
        self.__fig = Figure(figsize=(5, 4),dpi=64)
        self.__ax = self.__fig.add_subplot(1 ,1, 1)
        self.__line, = self.__ax.plot([], [])
        
        self.__canvas = FigureCanvasTkAgg(self.__fig, self.__canvas_frame)
        self.__canvas.draw()
        self.__canvas.get_tk_widget().pack(side=tkinter.TOP,
                                         fill=tkinter.BOTH,
                                         expand=True
                                         )
        self.__button_start = Button(
            self.__control_frame,
            text="Start",
            command=self.start,
            )
        self.__button_start.pack()
        
        
        self.__button_stop = Button(
            self.__control_frame,
            text="Stop",
            command=self.stop,
            )
        self.__button_stop.pack()
        
        self.__button_reset = Button(
            self.__control_frame,
            text="Reset",
            command=self.reset,
            )
        self.__button_reset.pack()
        
    def update(self, frame: int):
       xdata = np.linspace(0, 4 * np.pi, frame)
       ydata = np.sin(xdata)
       self.__line.set_data(xdata, ydata)
       self.__ax.relim()
       self.__ax.autoscale_view()
       self.__canvas.draw()
    
    def reset(self):
        self.__line.set_data([], [])
        self.__canvas.draw()
        
    def start(self):
        self.__ani = FuncAnimation(
          self.__fig,  # Figureオブジェクト
          self.update,  # グラフ更新関数
           init_func=self.reset,  # 初期化関数
          interval = 10,  # 更新間隔(ms)
          frames=1000, 
          # blit = True,
          )
        self.__canvas.draw()
    
    def stop(self):
        if self.__ani is not None:
            self.__ani.event_source.stop()
            


        
if __name__ == "__main__":
    Application().mainloop()