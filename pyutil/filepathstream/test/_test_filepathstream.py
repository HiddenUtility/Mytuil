# -*- coding: utf-8 -*-
from pathlib import Path
from datetime import datetime
import shutil
from pyutil.dummiy.dummiy_creator import DummiyFileCreator
from pyutil.filepathstream.filepathstream import FilepathStream

class TestFilepathListStream:
    def __init__(self):
        self.dst = Path(r"./dummiy")
        if self.dst.is_dir(): 
            shutil.rmtree(self.dst)
        self.dst.mkdir()
        DummiyFileCreator().create(self.dst, 100, datetime(2023,5,1))
    
    def run(self):
        self.maker = FilepathStream(self.dst)
        print(self.maker)
    
