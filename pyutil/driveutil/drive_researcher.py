
from __future__ import annotations
from typing import overload
import psutil
from pathlib import Path

from pyutil.driveutil.DriveName import DriveName


class DriveResearcher:
    """ドライバの情報を抜く"""
    __path : str
    __drive_name : DriveName

    @overload
    def __init__(self, drive_name: DriveName):
        """調査したいドライバをDriveNameで指定

        Args:
            drive_name (DriveName): _description_

        """
    @overload
    def __init__(self, path: str):
        """調査したいドライバをstringsで指定

        Args:
            path (str): _description_

        """
    @overload
    def __init__(self, path: Path):
        """調査したいドライバをパスで指定

        Args:
            path (Path): _description_
        """

    def __init__(self,obj: Path = Path().cwd()):
        if isinstance(obj, DriveName):
            self.__path = obj.path
            self.__drive_name = obj
            self.__set()
            return
        self.__path = str(obj)
        self.__drive_name = DriveName(obj)
        self.__set()

    def __set(self):
        disk_usage = psutil.disk_usage(self.__path)
        self.__total_size = disk_usage.total
        self.__used_size = disk_usage.used
        self.__free_size = disk_usage.free
        self.__percent_used = disk_usage.percent
    
    def reload(self):
        '''ステータスを最新に更新します。'''
        self.__set()

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
    def free_ratio(self) -> float:
        """空き率"""
        return self.__free_size / self.__total_size
    
    @property
    def using_ratio(self) -> float:
        """使用率"""
        return self.__used_size / self.__total_size
    
    @property
    def using_ratio(self) -> float:
        return self.__percent_used

    def get_free_size_GB(self) -> int:
        return self.__free_size // 1000 //1000 /1000
        
    def get_free_size_TB(self) -> int:
        return self.__free_size // 1000 //1000 //1000 /1000
    
    def is_large_free_size_TB(self,terabyte: int) -> bool:
        return terabyte < self.get_free_size_TB()
    
    @property
    def path(self):
        return self.__path
    
    @property
    def drive_name(self):
        return self.__drive_name.value


