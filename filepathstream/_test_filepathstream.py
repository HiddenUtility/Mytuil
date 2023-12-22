# -*- coding: utf-8 -*-
from pathlib import Path
from datetime import datetime
import shutil
from dummiycreator.dummiy_creator import DummiyFileCreator
from filepathstream.filepathstream import FilepathListStream

class TestFilepathListStream:
    def __init__(self):
        self.dst = Path(r"./dummiy")
        if self.dst.is_dir(): 
            shutil.rmtree(self.dst)
        self.dst.mkdir()
        DummiyFileCreator().create(self.dst, 100, datetime(2023,5,1))
    
    def run(self):
        self.maker = FilepathListStream(self.dst)
        print(self.maker)
    
