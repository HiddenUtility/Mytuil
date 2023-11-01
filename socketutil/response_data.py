# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 21:45:42 2023

@author: nanik
"""
from __future__ import annotations
import json
from socketutil.response import Response
from socketutil.response_must_key import ResponseMustKeys
from socketutil.errors import NotHasMustKeyError

class ResponseData(Response):
    
    ENCODING = "utf-8"
    MUST_KYES:ResponseMustKeys = ResponseMustKeys
    
    __dict : dict
    __bytes : bytes
    def __init__(self, dict_: dict = {}, bytes_: bytes = bytes()):
        self.__dict = dict_
        self.__bytes = bytes_
        
    def __check_must_key(self, dict_: dict):
        for k in dict_.keys():
            try:
                self.MUST_KYES(k)
            except ValueError:
                raise NotHasMustKeyError(f"{dict_}は{k}を持っていません。")

    def load_dict(self, dict_: dict) -> ResponseData:
        bytes_ = json.dumps(dict_).encode(self.ENCODING)
        self.__check_must_key(dict_)
        return ResponseData(dict_=dict_, bytes_=bytes_)
    
    def load_bytes(self, bytes_: bytes) -> ResponseData:
        dict_ = json.loads(bytes_.decode(self.ENCODING))
        self.__check_must_key(dict_)
        return ResponseData(dict_=dict_, bytes_=bytes_)
    
    def to_dict(self) -> dict:
        return self.__dict
    
    def to_bytes(self) -> bytes:
        return self.__bytes