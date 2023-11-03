# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 21:50:23 2023

@author: nanik
"""
from __future__ import annotations
import json
from socketutil.request import Request
from socketutil.request_must_key import RequestMustKeys
from socketutil.errors import NotHasMustKeyError

class RequestData(Request):
    
    ENCODING = "utf-8"
    MUST_KYES:RequestMustKeys = RequestMustKeys
    
    __dict : dict
    __bytes : bytes
    def __init__(self, dict_: dict = {}, bytes_:bytes = bytes()):
        self.__dict = dict_
        self.__bytes = bytes_
        
    def __check_must_key(self, dict_: dict):
        for k in dict_.keys():
            try:
                self.MUST_KYES(k)
            except ValueError:
                raise NotHasMustKeyError(f"{dict_}は{k}を持っていません。")
                
    def dump(self,**kwargs):
        return self.load_dict(dict**kwargs())
    
    #@override
    def load_dict(self, dict_: dict) -> RequestData:
        bytes_ = json.dumps(dict_).encode(self.ENCODING)
        self.__check_must_key(dict_)
        return RequestData(dict_=dict_, bytes_=bytes_)
    #@override
    def load_bytes(self, bytes_: bytes) -> RequestData:
        dict_ = json.loads(bytes_.decode(self.ENCODING))
        self.__check_must_key(dict_)
        return RequestData(dict_=dict_, bytes_=bytes_)
    #@override
    def to_dict(self) -> dict:
        return self.__dict
    #@override
    def to_bytes(self) -> bytes:
        return self.__bytes
        
    def __str__(self):
        return str(self.__dict)
        
    def __getitem__(self, key):
        return self.__dict[key]
    
