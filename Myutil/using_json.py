# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 14:06:41 2023

@author: nanik
"""

from pathlib import Path
import json

class UsingJson:
    @staticmethod
    def to_json(filepath: Path, dictionary: dict):
        with open(filepath, "w") as f:
            json.dump(dictionary, f)
    
    def read_json(filepath) -> dict:
        with open(filepath, "r") as f:
            dictionary = json.load(f)
        return dictionary