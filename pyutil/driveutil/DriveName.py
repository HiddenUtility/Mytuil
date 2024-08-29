from __future__ import annotations


import re
from pathlib import Path


class DriveName:
    """何ドライブか"""
    __path : str
    __value : str


    def __init__(self,path: Path = Path().cwd()):
        """調査したいドライバのパスを与える

        Args:
            path (Path, optional): 調査したいパス. Defaults to Path().cwd().
        """
        self.__path = str(path)
        if not re.match(r'[A-Z]{1}',self.__path[0]):
            raise ValueError(f'{self.__path}ローカルパスのみです。')
        self.__value = self.__path[0]

    def __str__(self):
        return f"{self.__class__.__name__}={self.__value}"

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.__str__())

    def __lt__(self, obj):
        if not isinstance(obj, DriveName): return False
        return self.value < obj.value

    def __eq__(self, obj):
        if not isinstance(obj, DriveName): return False
        return self.value == obj.value

    def __ne__(self, obj):
        return not self.__eq__(obj)

    @property
    def value(self) -> str:
        return self.__value
    
    @property
    def path(self) -> str:
        return self.__path
    