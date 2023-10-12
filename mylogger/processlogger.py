# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 22:42:02 2023

@author: nanik
"""

from __future__ import annotations
import re
from typing import Final
from datetime import datetime
from pathlib import Path
import hashlib
from copy import copy
import time
import pickle

class ProcessLogger:
    LOG_NAME:Final = "mylog"
    __name: str
    __dst: Path
    __logs: list[datetime]
    def __init__(self,dst:Path = None, name="", split_day=True, limit=5):
        self.__dst = dst if dst is not None else Path()
        self.__name = self.LOG_NAME if name=="" else name
        self.__logs=[]
        
    @property  
    def logs(self):
        return self.__logs
    
    
    @staticmethod
    def load(filepath: Path)-> object:
        with open(filepath, "rb") as f:
            obj = pickle.load(f)
        return obj
    
    @staticmethod
    def dump(filepath: Path, obj: object)-> None:
        with open(filepath, "wb") as f:
            pickle.dump(obj, f)