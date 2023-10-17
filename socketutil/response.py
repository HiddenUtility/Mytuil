# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 23:39:07 2023

@author: nanik
"""

import json

class Responce:
    
    ENCODING = "utf-8"
    MUST_KYES = []
    
    __data : dict
    
    def __init__(self, **kwargs):
        self.__data = dict(**kwargs)
        self.__check_must_keys()
    
    def __check_must_keys(self):
        for key in self.MUST_KYES:
            if self.__data.get(key) is None: raise KeyError(f"{key} Not has in Data")
            
    @property
    def data(self) -> bytes:
        return json.dumps(self.__data).encode(self.ENCODING)