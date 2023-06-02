# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 08:53:13 2023

@author: nanik
"""



from __future__ import annotations
import abc
from pathlib import Path
import pickle
import hashlib

#interface
class Interface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def foo(self):
        raise NotImplementedError()
        
if __name__ == "__main__":
    pass
 