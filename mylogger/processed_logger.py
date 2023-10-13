# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 22:42:02 2023

@author: nanik
"""

from __future__ import annotations
from typing import Final
from datetime import datetime
from pathlib import Path

from copy import copy
import time
import pickle

from mylogger.logger import Logger

class ProcessedLogger(Logger):
    LOG_NAME:Final = "mylog"
    __name: str
    __dst: Path
    __logs: list[datetime]
    def __init__(self,dst:Path = None, name="", logs = []):
        self.__dst = dst if dst is not None else Path()
        self.__name = self.LOG_NAME if name=="" else name
        self.__logpath = self.__dst / f"{self.__name}.bin"
        self.__logs = set()
        
    def __add__(self,obj: ProcessedLogger):
        if not isinstance(obj, ProcessedLogger):raise TypeError
        new = copy(self)
        for log in obj.logs:
            new.__logs.add(log)
        return new
    
    @property  
    def logs(self):
        return self.__logs
    
    def load(self)-> object:
        if not self.__logpath.exists():
            return
        with open(self.__logpath, "rb") as f:
            self.__logs = pickle.load(f)

    def write(self, log: any, debug=False, out=False):
        if debug: print(log)
        self.__logs.add(log)
        if out: self.out()
        
    def out(self) -> None:
        with open(self.__logpath, "wb") as f:
            pickle.dump(self.__logs, f)
            
    def exists(self, log: str):
        return log in self.__logs


    
if __name__ == '__main__':
    
    logger = ProcessedLogger()
    logger.load()

    loggers = {}
    for i in range(3):
        loggers[i] = ProcessedLogger()
        
    for i in range(3):
        time.sleep(1)
        loggers[0].write(0,debug=True)
        time.sleep(1)
        loggers[1].write(1,debug=True)
        time.sleep(1)
        loggers[2].write(2,debug=True)
    
    for i in range(3):
        logger += loggers[i]
        
    logger.out()
    print(logger.logs)
