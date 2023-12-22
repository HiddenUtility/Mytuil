# -*- coding: utf-8 -*-
from __future__ import annotations
import abc
from typing import Final
import os
from datetime import datetime
from pathlib import Path
from copy import copy
import hashlib
import pickle
import shutil

####//Interface
class InterfaceErrorLogMaker(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def write(self, other: object) -> None:
        raise NotImplementedError()
    @abc.abstractmethod
    def read_logs(self, other: object) -> None:
        raise NotImplementedError()
    @abc.abstractmethod
    def out(self, other: object) -> None:
        raise NotImplementedError()

####//ParentClass
class ErrorLogMaker(InterfaceErrorLogMaker):
    DRINAME:Final = "ErrorLog"
    RESULT_NAME:Final = "ErrorLog.txt"
    ERROR_LOG:Final = ".errorlog"
    name: str
    dst: Path
    logs: list[LogData]
    def __init__(self,dst:Path = None, name=""):
        dirpathDst = dst if dst is not None else Path()
        self.name = name
        self.dst = dirpathDst.joinpath(self.DRINAME)
        self._mkdir()
        self.logs=[]

    def __add__(self, other):
        if not isinstance(other, ErrorLogMaker): raise TypeError
        new = copy(self)
        new.logs = sorted(new.logs + other.logs)
        return new
    
    def __str__(self):
        return "".join(["%s\n" % log for log in self.logs])
    
    def __repr__(self):
        return self.__str__()
    
    def _mkdir(self):
        if not self.dst.is_dir():self.dst.mkdir()

    @staticmethod
    def _load(path: Path):
        with open(path, "rb") as f:
            data = pickle.load(f)
        return data
    
    #//Orverride
    def write(self,*args, debug=False):
        self._mkdir()
        log = LogData(*args)
        if debug: print(log)
        path = self.dst.joinpath(log.get_hash() + self.name + self.ERROR_LOG)
        with open(path, "wb") as f:
            pickle.dump(log, f)

    #//Orverride
    def read_logs(self):
        logpaths = [f for f in self.dst.glob("*" + self.name + self.ERROR_LOG )]
        self.logs += [self._load(f) for f in logpaths]
        list(map(lambda f: os.remove(f), logpaths))

    #//Orverride
    def out(self):
        logs = sorted(self.logs)
        filepath = self.dst.parent.joinpath(f"{self.name}{self.RESULT_NAME}")
        with open(filepath, "w") as f:
            [f.write("%s\n" % log) for log in logs]
        if self.dst.is_dir(): shutil.rmtree(self.dst)
        

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
    
    test = ErrorLogMaker()
    for i in range(100):
        test.write(f"{i} test")
    
    print(test)
    test.read_logs()
    test.out()
    
    
    