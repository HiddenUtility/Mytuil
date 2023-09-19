# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 05:44:10 2023

@author: iwill
"""
from abc import ABCMeta, abstractclassmethod
from pathlib import Path

class SettingReader(metaclass=ABCMeta):

    @abstractclassmethod
    def load(self):
        pass
    
    
    def to_list(self):
        pass
    
class TextSettingReader(SettingReader):
    def __init__(self):
        self.src = Path("settings/settings.txt")
        self.settings = []
        self.load()
    
    def __str__(self):
        return "\n".join(self.settings)
    def __repr__(self):
        return self.__str__()
    
    
    def load(self):
        if not self.src.is_file(): raise FileNotFoundError(f"{self.src}がありません。")
        with open(self.src, "r", encoding="utf-8") as f:
            self.settings = f.readlines()
            
    def to_list(self) -> list:
        return self.settings
    
    def get_paths(self) -> list[Path]:
        paths = [Path(p) for p in self.settings]
        
        return paths
    
        
if __name__ == "__main__":
    reader = TextSettingReader()
    print(reader)
    paths = reader.get_paths()
    
    