# -*- coding: utf-8 -*-
from __future__ import annotations
import abc
from pathlib import Path
import pickle
import shutil
import re

from datetime import datetime, timedelta

#interface
class Interface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def move(self):
        raise NotImplementedError()
        
class FileMover(Interface):
    srcFilepath: Path #
    dstDripath: Path #
    def __init__(self,srcFilepath: Path, dstDripath: Path):
        if not srcFilepath.is_file(): ValueError
        if not dstDripath.is_dir(): ValueError
        self.srcFilepath = srcFilepath
        self.dstDripath = dstDripath
        datetime_day = self._get_datetime(self.srcFilepath.stem)
        self.day_label = self._get_date_label(datetime_day)

    @staticmethod
    def _get_datetime(name: str)->datetime:
        date_string = re.search("\d{14}",name).group()
        if date_string is None: raise FileExistsError("ファイル名に情報が含まれません。")
        _datetime = datetime.strptime(date_string, '%Y%m%d%H%M%S')
        return _datetime
    
    @staticmethod
    def _get_date_label(datetime_: datetime)-> str:
        """
        Parameters
        ----------
        datetime_ : datetime
            ファイルの日時

        Returns
        -------
        str
            ５時であれば一日巻き戻る。

        """
        if datetime_.hour < 5: ##5時までは昨日の２直とする。
            previous_day = datetime_ - timedelta(days=1)
            return previous_day.strftime("%Y-%m-%d")
        else:
            return datetime_.strftime("%Y-%m-%d")
            
    #//Override
    def move(self):

        dst = self.dstDripath.joinpath(self.day_label)
        if not dst.is_dir(): dst.mkdir()
        
        shutil.copy2(self.srcFilepath, dst)
        try:
            shutil.copy2(self.srcFilepath, dst)
            self.srcFilepath.unlink()
        except:
            print(f"移動失敗: {self.srcFilepath}")
        
        
