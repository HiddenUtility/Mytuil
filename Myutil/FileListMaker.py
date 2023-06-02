# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 08:53:13 2023

@author: nanik
"""



from __future__ import annotations
import abc
import os
from pathlib import Path
import pickle
import hashlib
import re
from datetime import datetime
import random
from copy import copy

#interface
class Interface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_filepaths(self):
        raise NotImplementedError()
        

    
    @abc.abstractmethod
    def reverce_sort(self)->FilelistMaker:
        raise NotImplementedError()

class FilelistMaker(Interface):
    filepaths: list[Filepath]
    empty: bool
    def __init__(self,src:Path, extension=""):
        if not src.is_dir(): ValueError
        names = [name for name in os.listdir(src) if extension in name]
        self.filepaths = [Filepath(src.joinpath(name)) for name in names]
        self.empty = len(self.filepaths) == 0
    def _return(self,filepaths):
        new = copy(self)
        new.filepaths = filepaths
        new.empty = len(filepaths) == 0
        return new
    def __str__(self):
        if len(self.filepaths) <= 10:
            return "".join(["%s\n" % f for f in self.filepaths])
        return "".join(["%s\n" % f for f in self.filepaths[10]])+"\n.\n.\n."
    def __repr__(self):
        return self.__str__()
        
    #//Override
    def get_filepaths(self)->list[Path]:
        return self.filepaths
    #//Override
    def get_filesize(self,num=10) -> float:
        """
        

        Parameters
        ----------
        num : TYPE, optional
            randumでn個のデータを開いて平均値を求める。
            デフォルトは10個

        Returns
        -------
        float
            平均値を返す。（kbyte）

        """
        if len(self.filepaths):return 0.0
        filepaths = self.filepaths if len(self.filepaths) < 10 else random.sample(self.filepaths, num)
        sizes = [path.stat().st_size for path in filepaths]
        return sum(sizes) / len(sizes) //1000
    
    def reverce_sort(self)->None:
        filepaths = sorted(self.filepaths, reverse=True)
        return self._return(filepaths)
    
    
    
class Filepath:
    def __init__(self,f: Path):
        if not f.is_file():raise ValueError
        self.filepath = f
        self._datetime = self._get_datetime(f.stem)
        self.suffix = f.suffix
        
    @staticmethod
    def _get_datetime(name: str)->datetime:
        date_string = re.search("\d{14}",name).group()
        if date_string is None: raise FileExistsError("ファイル名に情報が含まれません。")
        _datetime = datetime.strptime(date_string, '%Y%m%d%H%M%S')
        return _datetime  
    def __eq__(self, o: datetime):
        return self._datetime == o
    def __ne__(self, o: datetime):
        return self._datetime != o
    def __lt__(self, o: datetime):
        return self._datetime < o
    def __le__(self, o: datetime):
        return self._datetime <= o
    def __gt__(self, o: datetime):
        return self._datetime > o
    def __ge__(self, o: datetime):
        return self._datetime >= o
    def __str__(self):
        return f"{self._datetime}: {self.filepath.parent.name}/{self.filepath.name}"
    def __repr__(self):
        return self.__str__()
    def get_datetime(self):
        return self._datetime
    
    
    
    
    
    
    
    
        
if __name__ == "__main__":
    src = Path(r"C:\hrks\TEST\dst\2023-05-31")
    test = FilelistMaker(src)
    print(test)
    print(test.get_filesize())
    test = test.reverce_sort()
    print("sorted:\n",test)
 