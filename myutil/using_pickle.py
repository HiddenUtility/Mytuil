# -*- coding: utf-8 -*-
import pickle
from pathlib import Path
class UsingPickle:
    
    @staticmethod
    def load(filepath: Path)-> object:
        with open(filepath, "rb") as f:
            obj = pickle.load(f)
        return obj
    
    @staticmethod
    def dump(filepath: Path, obj: object)-> None:
        with open(filepath, "wb") as f:
            pickle.dump(obj, f)
