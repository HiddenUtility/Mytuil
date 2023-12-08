# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 16:28:31 2023

@author: nanik
"""

import hashlib
from zipfile import ZipFile, ZIP_DEFLATED
from pathlib import Path

class UsingZip:
    def __init__(self,target: Path):
        if not isinstance(target, Path): raise TypeError
        if not target.is_file(): raise FileNotFoundError
        self.__filepath = target
        self.__zi_path = self.__filepath.with_suffix(".zi_")
        self.__zippath = self.__filepath.with_suffix(".zip")
    
    def __get_hash_origin(self):
        with open(self.__filepath, "rb") as f:
            data = f.read()
            return hashlib.sha256(data).hexdigest()
    
    def __get_hash_zip(self):
        with ZipFile(self.__zi_path, 'r') as zip_file:
            with zip_file.open(self.__filepath.name) as origin:
                data = origin.read()
                return hashlib.sha256(data).hexdigest()
    
    def __is_same_binary(self) -> bool:
        return self.__get_hash_origin() != self.__get_hash_zip()
    
    def to_zip(self):
        try:
            with ZipFile(self.__zi_path, "w", compression=ZIP_DEFLATED) as f:
                f.write(self.__filepath, arcname=self.__filepath.name)
        except Exception as e:
            if self.__zi_path.exists():
                self.__zi_path.unlink()
            raise Exception(f"{self.__filepath}の圧縮失敗\n{e}")
            
        try:
            same = self.__is_same_binary()
        except Exception as e:
            if self.__zi_path.exists():
                self.__zi_path.unlink()
            raise Exception(f"{self.__filepath}の圧縮比較が出来ませんでした。\n{e}")
            
        if not same:
            raise NotSameCompressionDataBinaryError()
            
        self.__zi_path.rename(self.__zippath)
        
            
            
class NotSameCompressionDataBinaryError(Exception):
    pass