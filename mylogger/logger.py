# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 23:27:57 2023

@author: nanik
"""

from abc import ABCMeta, abstractmethod

####//Interface
class Logger(metaclass=ABCMeta):
    @abstractmethod
    def write(self, other: object, debug=False, out=False) -> None:
        raise NotImplementedError()
    @abstractmethod
    def out(self) -> None:
        raise NotImplementedError()