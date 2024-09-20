from __future__ import annotations
from pathlib import Path
from datetime import datetime
import random

from pyutil.pathuil.pathstream.path_stream import PathStream
from pyutil.pathuil.pathstream.xxx_filepath import DateTime14LabelFilepath

class FilepathStream(PathStream):
    """Pathの複数をメソッドチェーンで操作するためのオブジェクト"""
    __filepaths: list[DateTime14LabelFilepath]
    __empty: bool
    _count: int
    def __init__(self,src:Path = None, glob="*", _filepaths:list[DateTime14LabelFilepath]=[]):
        self.__filepaths = _filepaths
        self._count = 0
        self.__empty = len(self.__filepaths) == 0
        if src is None:return
        if self.__filepaths:return
        if not src.is_dir(): ValueError(f"{src} is Not Directory Path")
        self.__filepaths = [DateTime14LabelFilepath(f) for f in src.glob(glob) if f.is_file()]
        self.__empty = len(self.__filepaths) == 0
        
    def _return(self,filepaths: list[DateTime14LabelFilepath]) -> FilepathStream :
        return FilepathStream(_filepaths=filepaths)
    
    def __str__(self):
        if len(self.__filepaths) <= 10:
            return "".join(["%s\n" % f for f in self.__filepaths])
        return "".join(["%s\n" % f for f in self.__filepaths[:10]])+"\n.\n.\n."
    
    def __repr__(self):
        return self.__str__()
    
    def __len__(self):
        return len(self.__filepaths)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._count == len(self.__filepaths):
            raise StopIteration
        self._count+=1
        return self.__filepaths[self._count - 1].get_filepath()
    
    def __add__(self, obj: FilepathStream):
        if not isinstance(obj, FilepathStream):raise TypeError
        filepaths = self.__filepaths + obj.filepaths
        self._return(list(set(filepaths)))
    
    @property
    def empty(self):
        return self.__empty

    #//Override
    def to_filepaths(self)->list[Path]:
        return [f.get_filepath() for f in self.__filepaths]
    
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
        if len(self.__filepaths):return 0.0
        filepaths = self.__filepaths if len(self.__filepaths) < 10 else random.sample(self.__filepaths, num)
        sizes = [path.stat().st_size for path in filepaths]
        return sum(sizes) / len(sizes) //1000
    
    #@Override
    def sort(self, reverse=False) -> FilepathStream:
        filepaths = sorted(self.__filepaths, reverse=reverse)
        return self._return(filepaths)
    
    #@Override
    def filter_datetime(self,
                             start: datetime=datetime(2000, 1, 1),
                             end: datetime=datetime(2099,12,31)) -> FilepathStream:
        """ファイパスをdatetimeで絞る

        Args:
            start (datetime, optional): 開始. Defaults to datetime(2000, 1, 1).
            end (datetime, optional): 終了. Defaults to datetime(2099,12,31).

        Raises:
            TypeError: _description_
            TypeError: _description_
            ValueError: _description_

        Returns:
            FilepathStream: _description_
        """
        if not isinstance(start, datetime): raise TypeError
        if not isinstance(end, datetime): raise TypeError
        if end < start: raise ValueError
        filepaths = [f for f in self.__filepaths if start < f.to_datetime() < end]
        return self._return(filepaths)
        
    #@Override
    def reduce_number(self, n: int | None)->FilepathStream:
        if n is None:return self
        if not isinstance(n, int): raise TypeError
        if len(self.__filepaths) <= n: return self
        filepaths = random.sample(self.__filepaths, n)
        return self._return(filepaths)
    
    #@Override
    def reduce_rate(self, r: float | None)->FilepathStream:
        if r is None:return self
        if not (0 < r < 1):raise ValueError
        n = int(len(self.__filepaths) * r)
        return self.reduce_number(n)
    
    #@Override
    def drop_filenames(self,names: list[str]) -> FilepathStream:
        if len(names) == 0:return self
        filepaths = [f for f in self.__filepaths if f.name not in names]
        return self._return(filepaths)
    
    #@Override
    def drop_datetimes(self,datetimes: list[datetime]) -> FilepathStream:
        if len(datetimes) == 0:return self
        filepaths = [f for f in self.__filepaths if f.to_datetime() not in datetimes]
        return self._return(filepaths)
    
    #@Override
    def narrow_to_contain_keys(self,*keys: str) -> FilepathStream:
        filepaths = []
        for k in keys:
            filepaths += [f for f in self.__filepaths if k in f.name]
        return self._return(filepaths)
