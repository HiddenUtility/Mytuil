# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 13:09:01 2023

@author: Z619480
"""
from __future__ import annotations
import re
from pathlib import Path
from datetime import datetime


class MuscleWaveFilepath:
    PATTERNLABEL_DATETIME= "%Y%m%d%H%M%S"
    def __init__(self,f: Path):
        self.__fielpath = f
        self.__serial = ""
        self.__set_serial()
        self.__datetime = self.__get_datetime(f)
        
    def __set_serial(self):
        obj = re.search("\d{16}", self.stem)
        if obj is not None:
            self.__serial = obj.group()

    def __get_datetime(self,f:Path) -> datetime:
        new = self.stem.replace(self.__serial, "")
        findings = re.findall("\d{14}", new)
        if len(findings) == 0: 
            raise HasNotDatatimeDataError(f"{f}には日付情報がありません。")
        for finding in findings:
            try:
                return datetime.strptime(finding, self.PATTERNLABEL_DATETIME)
            except:
                pass
        raise HasNotDatatimeDataError(f"{f}には日付情報がありません。")
        
    def __eq__(self, o: datetime):
        return self.__datetime == o
    def __ne__(self, o: datetime):
        return self.__datetime != o
    def __lt__(self, o: datetime):
        return self.__datetime < o
    def __le__(self, o: datetime):
        return self.__datetime <= o
    def __gt__(self, o: datetime):
        return self.__datetime > o
    def __ge__(self, o: datetime):
        return self.__datetime >= o
    def __str__(self):
        return f"{self.__datetime}: {self.name}"
    def __repr__(self):
        return self.__str__()
    def __hash__(self):
        return hash(self.__datetime)
    
    def to_filepath(self) -> Path:
        return self.__fielpath
    
    def get_serial(self) -> str:
        return self.__serial
    
    def to_datetime(self) -> datetime:
        return self.__datetime
    
    @property
    def path(self):
        return self.__fielpath
    
    @property
    def name(self):
        return self.__fielpath.name
    
    @property
    def stem(self):
        return self.__fielpath.stem
    
    @property
    def suffix(self):
        return self.__fielpath.suffix

    
class HasNotDatatimeDataError(Exception):
    pass
