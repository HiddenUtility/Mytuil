
from __future__ import annotations
import psutil
from pathlib import Path

class DriveResearcher:
    
    def __init__(self,path: Path = Path().cwd()):
        disk_usage = psutil.disk_usage(path)
        self.__total_size = disk_usage.total
        self.__used_size = disk_usage.used
        self.__free_size = disk_usage.free
        self.__percent_used = disk_usage.percent
    

    @property
    def total_size(self) -> int:
        return self.__total_size
    
    @property
    def used_size(self) -> int:
        return self.__used_size
    
    @property
    def free_size(self) -> int:
        return self.__free_size
    
    @property
    def percent_used(self) -> float:
        return self.__percent_used

    def get_free_size_GB(self) -> int:
        return self.__free_size // 1000 //1000 /1000
        
    def get_free_size_TB(self) -> int:
        return self.__free_size // 1000 //1000 //1000 /1000
    
    def is_large_free_size_TB(self,terabyte: int) -> bool:
        return terabyte < self.get_free_size_TB()
    

    