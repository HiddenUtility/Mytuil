# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 23:39:18 2023

@author: nanik
"""

from abc import ABCMeta, abstractclassmethod

class Request(metaclass=ABCMeta):
    
    @abstractclassmethod
    def load_dict(self, data: dict) -> None:
        raise NotImplementedError()
    
    @abstractclassmethod
    def load_bytes(self, data: dict) -> None:
        raise NotImplementedError()
    
    
    @abstractclassmethod
    def to_dict(self) -> dict:
        raise NotImplementedError()
    
    @abstractclassmethod
    def to_bytes(self) -> bytes:
        raise NotImplementedError()
    
