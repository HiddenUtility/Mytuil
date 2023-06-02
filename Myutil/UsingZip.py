# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 16:28:31 2023

@author: nanik
"""

import os
from zipfile import ZipFile, ZIP_DEFLATED
from pathlib import Path

class UsingZip:
    @staticmethod
    def to_zip(filepath: Path):
        if not isinstance(filepath, Path): raise TypeError
        if not filepath.is_file(): raise FileNotFoundError
        try:
            with ZipFile(filepath.with_suffix(".zip"), "w", compression=ZIP_DEFLATED) as f:
                f.write(filepath, arcname=filepath.name)
                os.remove(filepath)
        except:
            print(f"{filepath}:圧縮失敗")