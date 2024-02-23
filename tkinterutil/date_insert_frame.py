from datetime import date, datetime
import tkinter
from tkinter import Frame
from tkinter import Entry
from tkinter import Label
from tkinter import Button
from pathlib import Path
from tkinterutil.setting_paramter import SettingParamter
from tkinterutil.main_frame import MainFrame
from tkinterutil.calender_dialog import CalendarDialog

class DateInsertFrame(MainFrame):
    __date_entry : Entry
    __date : date
    __setting_paramter : SettingParamter

    def __init__(self, master_frame: Frame) -> None:
        self.__setting_paramter = SettingParamter().load()
        self.__main_frame = Frame(master_frame, relief="solid", bd=1, bg="#4682b4", padx=1, pady=1)
        self.__label_frame = Frame(self.__main_frame)
        self.__input_frame = Frame(self.__main_frame)

        self.__date = self.__setting_paramter.datedata

    def __get_date(self):
        dialog = CalendarDialog(self.__input_frame, title="日付を選択")
        datedata = dialog.get_date()
        if datedata != "":
            self.__date_entry.delete(0, tkinter.END)
            self.__date_entry.insert(0, datedata)
            self.__date = datetime.strptime(datedata, "%Y/%m/%d").date()

    def __create_frame(self):
        Label(self.__label_frame, text="パス指定").pack(anchor="w")

        Label(self.__input_frame, text="入力のディレクトリパス").grid(
            sticky='nw', row=0, column=0
        )
        self.__date_entry = Entry(self.__input_frame, width=66)
        self.__date_entry.insert(0, str(self.__date))
        self.__date_entry.grid(sticky='nw', row=1, column=0)

        Button(self.__input_frame, 
               text="日付",
               width=4,
               command=self.__get_date
        ).grid(sticky='nw',
                row=1,
                column=1,                   
        )

    def show(self):
        self.__create_frame()
        self.__main_frame.pack(anchor="w")
        self.__label_frame.pack(anchor="w")
        self.__input_frame.pack(anchor="w")

    def get_data(self) -> date:
        return self.__date