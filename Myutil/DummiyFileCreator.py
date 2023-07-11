# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 13:45:55 2023

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
import random

#interface
class Interface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(self):
        raise NotImplementedError()
        
        
class DummiyFileCreator(Interface):
    
    FORMAT = "%Y%m%d%H%M%S"
    def __init__(self):
        pass
    
    @staticmethod
    def _create_dummy(filepath, file_size=0):
        with open(filepath, "w") as f:
            if file_size > 0: f.write(" " * file_size)
            
    @staticmethod
    def _get_random_datetime(start, end):
        start_timestamp = start.timestamp()
        end_timestamp = end.timestamp()
        random_timestamp = random.uniform(start_timestamp, end_timestamp)
        return datetime.fromtimestamp(random_timestamp)

    def create(self,dst: Path, create_number: int, start: datetime, end:datetime = datetime.now(), file_size=0):
        for i in range(create_number):
            date = self._get_random_datetime(start, end)
            filepath = dst.joinpath(date.strftime(self.FORMAT + "_dummy.txt"))
            self._create_dummy(filepath, file_size=file_size)
    

    