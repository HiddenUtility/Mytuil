# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 16:55:30 2023

@author: nanik
"""

import tkinter
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import Button

from calender_dialog import CalendarDialog

class Test:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("200x200")
        fream = Frame(self.root, bd=4, relief="groove")
        label = Label(fream, text="Date")
        label.grid(padx=2, sticky="w", row=0, column=0)
        self.entry = Entry(fream, width=20)
        self.entry.grid(sticky="w", row=1, column=0)
        button = Button(fream,text="get",width=4,command=self.get_date)
        button.grid(sticky="w", row=1, column=1)
        fream.pack()
        
    def get_date(self) -> None:
        dialog = CalendarDialog(self.root, title="calendar")
        date = dialog.get_date()
        if date != "":
            self.entry.delete(0, tkinter.END)
            self.entry.insert(0,date)
            
    def run(self):
        self.root.mainloop()




if __name__ == "__main__":
    test = Test()
    test.run()