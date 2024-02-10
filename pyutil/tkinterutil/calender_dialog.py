# -*- coding: utf-8 -*-
import tkinter
from tkinter.simpledialog import Dialog
from tkcalendar import Calendar


class CalendarDialog(Dialog):
    date: str
    def __init__(self, master: tkinter.Tk, title=None) -> None:
        self.date = ""
        super().__init__(parent=master, title=title)
        
    #//Override
    def body(self, master) -> None:
        self.calendar = Calendar(master, showweeknumbers=False,date_pattern="yyyy/mm/dd")
        self.calendar.grid(sticky="w", row=0, column=0)
        
    #//Override
    def apply(self) -> None:
        self.date = self.calendar.get_date()
        print(self.date)
        
    def get_date(self) -> str:
        return self.date

