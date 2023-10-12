# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 08:53:13 2023

@author: nanik
"""

from __future__ import annotations

from typing import Final
from datetime import datetime
from pathlib import Path
import hashlib
from copy import copy
import time
import traceback


from logger import Logger
        
####//ParentClass
class MyLogger(Logger):
    LOG_NAME:Final = "mylog"
    __name: str
    __dst: Path
    __logs: list[LogData]
    def __init__(self,dst:Path = None, name="", split_day=True, limit=5):
        self.__limit = limit
        self.__dst = dst if dst is not None else Path()
        self.__name = self.LOG_NAME if name=="" else name
        self.__rmlog(self.__name)
        if split_day:
            self.__name = "{} {}".format(datetime.now().strftime("%Y-%m-%d-%a"), self.__name)
        self.__logs=[]
        self.start_time = time.time()
        
    def __add__(self,obj: MyLogger):
        if not isinstance(obj, MyLogger):raise TypeError
        new = copy(self)
        new.__logs += obj.logs
        return new
    
    def __rmlog(self,name):
        if self.__limit < 1: return
        fs = [f for f in self.__dst.glob(f"*.{name}.txt")]
        n = len(fs)
        if n < self.__limit:return
        for i in range(n - self.__limit - 1):
            fs[i].unlink()
    
    @property  
    def logs(self):
        return self.__logs

    def start(self):
        self.start_time = time.time()
        start = f"################# START {self.__name} ######################"
        self.write(start,out=True)
    def end(self):
        end   = f"################## END {self.__name} #######################"
        self.write(end)
        self.write("処理時間は{:5f}sでした。".format(time.time() - self.start_time),out=True)

    def write(self, *args: str, debug=False, out=False) -> None:
        data = LogData(*args)
        if debug: print(data)
        self.__logs.append(data)
        if out: self.out()
    
    def error(self, e: Exception):
        try:
            raise e
        except:
            self.write(traceback.format_exc(), debug=True, out=True)

    def out(self):
        logs = sorted(self.__logs)
        filepath = self.__dst.parent.joinpath(f"{self.__name}.txt")
        with open(filepath, "a") as f:
            [f.write("%s\n" % log) for log in logs]
        self.__logs = []

        
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
    
    logger = MyLogger()
    logger.start()
    
    loggers = {}
    for i in range(3):
        loggers[i] = MyLogger()
        

    for i in range(3):
        
        time.sleep(1)
        loggers[0].write(0,debug=True)
        time.sleep(1)
        loggers[1].write(1,debug=True)
        time.sleep(1)
        loggers[2].write(2,debug=True)
    

    for i in range(3):
        logger += loggers[i]
    logger.end()