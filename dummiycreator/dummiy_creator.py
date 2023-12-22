# -*- coding: utf-8 -*-
from __future__ import annotations
from pathlib import Path
from datetime import datetime
import random

class DummiyFileCreator:
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

    def create(self,dst: Path, 
               create_number: int, 
               start: datetime, 
               end:datetime = datetime.now(), 
               file_size=0,
               ):
        for i in range(create_number):
            date = self._get_random_datetime(start, end)
            filepath = dst.joinpath(date.strftime(self.FORMAT + "_dummy.txt"))
            self._create_dummy(filepath, file_size=file_size)
    
