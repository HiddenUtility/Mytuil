import unicodedata
import re
import tkinter
from tkinter import filedialog
from tkinter import Frame
from tkinter import Entry
from tkinter import Label
from tkinter import Button
from pathlib import Path
from pyutil.tkinterutil.setting_paramter import SettingParamter
from pyutil.tkinterutil.main_frame import MainFrame

class PathInsertFrame(MainFrame):
    __src_entry : Entry
    __dst_entry : Entry
    __dirname_entry : Entry
    __src : Path
    __dst : Path
    __dirname : str
    __setting_paramter : SettingParamter

    def __init__(self, master_frame: Frame) -> None:
        self.__setting_paramter = SettingParamter().load()
        self.__main_frame = Frame(master_frame, relief="solid", bd=1, bg="#4682b4", padx=1, pady=1)
        self.__label_frame = Frame(self.__main_frame)
        self.__input_frame = Frame(self.__main_frame)

        self.__src = self.__setting_paramter.src
        self.__dst = self.__setting_paramter.dst
        self.__dirname = self.__setting_paramter.dirname

    def __check_dirname(self) -> str:
        query = self.__dirname_entry.get()
        dirname = unicodedata.normalize('NFKC', query)
        new = re.sub(r'[\\|/|:|?|.|"|<|>|\|]', '禁止文字', dirname)
        if '禁止文字' in new:
            raise CanNotUsingStringInDrinameError

    def __get_src(self):
        fld = filedialog.askdirectory(initialdir=str(self.__src))
        if fld != '':
            self.__src_entry.delete(0, tkinter.END)
            self.__src_entry.insert(0, fld)
            self.__src = Path(fld)
         
    def __get_dst(self):
        fld = filedialog.askdirectory(initialdir=str(self.__dst))
        if fld != '':
            self.__dst_entry.delete(0, tkinter.END)
            self.__dst_entry.insert(0, fld)
            self.__dst = Path(fld)

    def __create_widget(self):
        Label(self.__label_frame, text="パス指定").pack(anchor="w")

        Label(self.__input_frame, text="入力のディレクトリパス").grid(
            sticky='nw', row=0, column=0
        )
        self.__src_entry = Entry(self.__input_frame, width=70)
        self.__src_entry.insert(0, str(self.__src))
        self.__src_entry.grid(sticky='nw', row=1, column=0)

        Button(self.__input_frame, 
               text="...",
               width=1,
               command= self.__get_src
        ).grid(
            sticky="nw", row=1, column=1
        )

        Label(self.__input_frame, text="出力のディレクトリパス").grid(
            sticky='nw', row=2, column=0
        )
        self.__dst_entry = Entry(self.__input_frame, width=70)
        self.__dst_entry.insert(0, str(self.__dst))
        self.__dst_entry.grid(sticky='nw', row=3, column=0)

        Button(self.__input_frame, 
               text="...",
               width=1,
               command= self.__get_dst
        ).grid(
            sticky="nw", row=3, column=1
        )

        Label(self.__input_frame, text="出力フォルダ名").grid(
            sticky='nw', row=4, column=0
        )
        self.__dirname_entry = Entry(self.__input_frame, width=40)
        self.__dirname_entry.insert(0, str(self.__dirname))
        self.__dirname_entry.grid(sticky='nw', row=5, column=0)


    def get_src(self) -> Path:
        src = Path(self.__src_entry.get())
        if not src.exists():
            raise NotADirectoryError()
        self.__src = src
        return self.__src
    
    def get_dst(self) -> Path:
        dst = Path(self.__dst_entry.get())
        if not dst.exists():
            raise NotADirectoryError()
        self.__dst = dst
        return self.__dst
    
    def get_dirname(self) -> str:
        self.__check_dirname()
        dirname = self.__dirname_entry.get()
        self.__dirname = dirname
        return dirname

    def show(self):
        self.__create_widget()
        self.__main_frame.pack(anchor="w")
        self.__label_frame.pack(anchor="w")
        self.__input_frame.pack(anchor="w")

class CanNotUsingStringInDrinameError(Exception):...
