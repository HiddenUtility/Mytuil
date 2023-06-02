# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 16:50:38 2023

@author: nanik
"""
from __future__ import annotations
import abc
import psutil
from pathlib import Path

#interface
class InterfaceDriveResearcher(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_free_size_GB(self):
        raise NotImplementedError()



class DriveResearcher(InterfaceDriveResearcher):
    
    def __init__(self,path: Path):
        self.path = path
        self._set()
        
    def _set(self):
        disk_usage = psutil.disk_usage(self.path)
        self.total_size = disk_usage.total
        self.used_size = disk_usage.used
        self.free_size = disk_usage.free
        self.percent_used = disk_usage.percent
        
    def get_free_size_GB(self) -> int:
        return self.free_size // 1000 //1000 /1000
        
    def get_free_size_TB(self) -> int:
        return self.free_size // 1000 //1000 //1000 /1000
    
    def is_large_free_size_TB(self,terabyte: int) -> bool:
        return terabyte < self.get_free_size_TB()
    

        
if __name__ == "__main__":
    p = r"C:\Users\nanik\OneDrive\デスクトップ"
    reserch = DriveResearcher(p)
    print(reserch.get_free_size_GB())
    print(reserch.get_free_size_TB())
    print(reserch.is_large_free_size_TB(1))
    