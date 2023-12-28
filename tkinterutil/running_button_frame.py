from tkinter import Frame
from tkinter import Button
from tkinterutil.setting_paramter import SettingParamter
from tkinterutil.main_frame import MainFrame
from tkinterutil.path_insert_frame import PathInsertFrame
from tkinterutil.date_insert_frame import DateInsertFrame

class RunningButtonFrame(MainFrame):
    __path_frame:PathInsertFrame
    __date_frame:DateInsertFrame
    def __init__(self, master_frame: Frame,
                 path_frame: PathInsertFrame,
                 date_frame: DateInsertFrame,
                 ) -> None:
        self.__main_frame = Frame(master_frame, relief="solid", bd=1, bg="#4682b4", padx=1, pady=1)
        # self.__label_frame = Frame(self.__main_frame)
        self.__input_frame = Frame(self.__main_frame)
        self.__path_frame = path_frame
        self.__date_frame = date_frame

    def __run(self):
        setting_paramter = SettingParamter(
            src=self.__path_frame.get_src(),
            dst=self.__path_frame.get_dst(),
            dirname=self.__path_frame.get_dirname(),
            datedata=self.__date_frame.get_data(),
        )
        print(setting_paramter)
        setting_paramter.dump()

    def __create_frame(self):
        Button(text="開始",
               width=20,
               command=self.__run
               ).pack(
                   padx=20,
                   pady=20,
                   side='bottom',
               )

    def show(self):
        self.__create_frame()
        self.__main_frame.pack(anchor="w")
        # self.__label_frame.pack(anchor="w")
        self.__input_frame.pack(anchor="center")
