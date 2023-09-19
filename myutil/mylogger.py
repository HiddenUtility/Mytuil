# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 08:53:13 2023

@author: nanik
"""

from __future__ import annotations
import abc
from typing import Final
from datetime import datetime
from pathlib import Path
import hashlib
from copy import copy


####//Interface
class Logger(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def write(self, other: object) -> None:
        raise NotImplementedError()
    @abc.abstractmethod
    def out(self, other: object) -> None:
        raise NotImplementedError()
        
####//ParentClass
class MyLogger(Logger):
    LOG_NAME:Final = "mylog"
    name: str
    dst: Path
    logs: list[LogData]
    def __init__(self,dst:Path = None, name=""):
        self.dst = dst if dst is not None else Path()
        self.name = self.LOG_NAME if name=="" else name
        self.logs=[]
        
    def __add__(self,obj: Logger):
        if not isinstance(obj, Logger):raise TypeError
        new = copy(self)
        new.logs += obj.logs
        return new
    
    def start(self):
        start = "#################START######################"
        self.write(start,out=True)
    def end(self):
        end = "##################END######################"
        self.write(end,out=True)

    def write(self, *args: str, debug=False, out=False) -> None:
        data = LogData(*args)
        if debug: print(data)
        self.logs.append(data)
        if out: self.out
        
    def out(self):
        logs = sorted(self.logs)
        filepath = self.dst.parent.joinpath(f"{self.name}.txt")
        with open(filepath, "w") as f:
            [f.write("%s\n" % log) for log in logs]

        
class LogData:
    def __init__(self, *args: str):
        self.datas = [str(v) for v in args]
        self.now = datetime.now()
    def __hash__(self):
        return hash(self._out_log())
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return self._out_log()
    def __lt__(self, other):
        if not isinstance(other, LogData):raise TypeError
        return self.now < other.now
    def _timestamp(self):
        return self.now.strftime("%Y/%m/%d %H:%M:%S.%f")
    def _out_log(self):
        return self._timestamp() + ": " + "_".join(self.datas)
    def get_hash(self):
        return hashlib.md5(self._out_log().encode()).hexdigest()
    
    
if __name__ == '__main__':
    loggers = {}
    for i in range(3):
        loggers[i] = MyLogger()
        
    import time
    for i in range(3):
        
        time.sleep(1)
        loggers[0].write(0,debug=True)
        time.sleep(1)
        loggers[1].write(1,debug=True)
        time.sleep(1)
        loggers[2].write(2,debug=True)
    
    logger = MyLogger()
    for i in range(3):
        logger += loggers[i]
    logger.out()