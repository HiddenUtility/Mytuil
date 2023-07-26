# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 09:44:54 2023

@author: nanik
"""

import tkinter
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter.simpledialog import Dialog
from tkcalendar import Calendar


class CalenderDialog(Dialog):
    date: str
    def __init__(self, master: tkinter.Tk, title=None) -> None:
        self.date = ""
        super().__init__(parent=master, title=title)
        
    #//Override
    def body(self, master) -> None:
        self.calender = Calendar(master, showweeknumbers=False,date_patternstr="y-mm-dd")
        self.calender.grid(sticky="w", row=0, column=0)
        
    #//Override
    def apply(self) -> None:
        self.date = self.calender.get_date()
        print(self.date)
        
    def get_date(self):
        return self.date


class Test:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("200x200")
        fream = Frame(self.root, bd=4, relief="groove")
        label = Label(fream, text="Date")
        label.grid(padx=2, sticky="w", row=0, column=0)
        self.entry = Entry(fream, width=10)
        self.entry.grid(sticky="w", row=1, column=0)
        button = Button(fream,text="get",width=4,command=self.get_date)
        button.grid(sticky="w", row=1, column=1)
        fream.pack()
        
    def get_date(self) -> None:
        dialog = CalenderDialog(self.root, title="calendar")
        date = dialog.get_date()
        if date != "":
            self.entry.delete(0, tkinter.END)
            self.entry.insert(0,date)
            
    def run(self):
        self.root.mainloop()




if __name__ == "__main__":
    test = Test()
    test.run()
