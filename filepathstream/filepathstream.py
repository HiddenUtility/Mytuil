# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 08:53:13 2023

@author: nanik
"""
from __future__ import annotations
import abc
import os
from pathlib import Path

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
    def get_file_size(self):
        raise NotImplementedError()
    @abc.abstractmethod
    def sort(self)->FilepathListMaker:
        raise NotImplementedError()
    @abc.abstractmethod
    def narrow_down_datetime(self,start: datetime, end: datetime)->FilepathListMaker:
        raise NotImplementedError()
    @abc.abstractmethod
    def reduce_number(self)->FilepathListMaker:
        raise NotImplementedError()
    @abc.abstractmethod
    def reduce_rate(self)->FilepathListMaker:
        raise NotImplementedError()
    @abc.abstractmethod
    def drop_filenames(self,names: list[str])->FilepathListMaker:
        raise NotImplementedError()
    @abc.abstractmethod
    def narrow_to_contain_keys(self,*key: str) -> FilepathListMaker:
        raise NotImplementedError()
        
class FilepathListMaker(Interface):
    filepaths: list[Filepath]
    empty: bool
    count: int
    def __init__(self,src:Path, extension=""):
        if not src.is_dir(): ValueError
        names = [name for name in os.listdir(src) if extension in name]
        self.filepaths = [Filepath(src.joinpath(name)) for name in names]
        self.empty = len(self.filepaths) == 0
        self.count=0
    def _return(self,filepaths):
        new = copy(self)
        new.filepaths = filepaths
        new.empty = len(filepaths) == 0
        return new
    def __str__(self):
        if len(self.filepaths) <= 10:
            return "".join(["%s\n" % f for f in self.filepaths])
        return "".join(["%s\n" % f for f in self.filepaths[:10]])+"\n.\n.\n."
    def __repr__(self):
        return self.__str__()
    def __len__(self):
        return len(self.filepaths)
    def __iter__(self):
        return self
    def __next__(self):
        if self.count == len(self.filepaths):
            raise StopIteration
        self.count+=1
        return self.filepaths[self.count - 1].get_filepath()
    def __add__(self, obj: FilepathListMaker):
        if not isinstance(obj, FilepathListMaker):raise TypeError
        filepaths = self.filepaths + obj.filepaths
        self._return(filepaths)

    #//Override
    def get_filepaths(self)->list[Path]:
        return [f.get_filepath() for f in self.filepaths]
    #//Override
    def get_file_size(self,num=10) -> float:
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
    
    #@Override
    def sort(self, reverse=False) -> FilepathListMaker:
        filepaths = sorted(self.filepaths, reverse=reverse)
        return self._return(filepaths)
    #@Override
    def narrow_down_datetime(self,
                             start: datetime=datetime(2000, 1, 1),
                             end: datetime=datetime(2099,12,31)) -> FilepathListMaker:
        if not isinstance(start, datetime): raise TypeError
        if not isinstance(end, datetime): raise TypeError
        if end < start: raise ValueError
        filepaths = [f for f in self.filepaths if start < f < end]
        return self._return(filepaths)
        
    #@Override
    def reduce_number(self, n: int | None)->FilepathListMaker:
        if n is None:return self
        if not isinstance(n, int): raise TypeError
        if len(self.filepaths) <= n: return self
        filepaths = random.sample(self.filepaths, n)
        return self._return(filepaths)
    #@Override
    def reduce_rate(self, r: float | None)->FilepathListMaker:
        if r is None:return self
        if not (0 < r < 1):raise ValueError
        n = int(len(self.filepaths) * r)
        return self.reduce_number(n)
    
    #@Override
    def drop_filenames(self,names: list[str]) -> FilepathListMaker:
        if len(names) == 0:return self
        filepaths = [f for f in self.filepaths if f.name not in names]
        return self._return(filepaths)
    
    #@Override
    def narrow_to_contain_keys(self,*keys: str) -> FilepathListMaker:
        filepaths = []
        for k in keys:
            filepaths += [f for f in self.filepaths if k in f.name]
        return self._return(filepaths)

class Filepath:
    def __init__(self,f: Path):
        if not f.is_file():raise ValueError(f"{f}はfilepathではありません。")
        self.filepath = f
        self.name = f.name
        self._datetime = self._get_datetime(f.stem)
        self.suffix = f.suffix
    def _get_datetime(self, name: str) -> datetime:
        obj = re.search("\d{14}",name)
        if obj is None: 
            return datetime.timestamp(self.filepath.stat().st_ctime)
        return datetime.strptime(obj.group(), '%Y%m%d%H%M%S')  
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
    def __hash__(self):
        return hash(self._datetime)
    def get_datetime(self):
        return self._datetime
    def get_filepath(self):
        return self.filepath
    

        
if __name__ == "__main__":
    src = Path(r"C:\hrks\TEST\src")
    test = FilepathListMaker(src)
    print(test)
    print(test.get_file_size())
    test = test.sort()
    print("sorted:\n",test)
 