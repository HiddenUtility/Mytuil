# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 22:11:30 2023

@author: iwill
"""
from pathlib import Path
from datetime import datetime
import shutil
from dummiy_creator import DummiyFileCreator
from filepathstream import FilepathListStream


class TestFilepathListStream:
    def __init__(self):
        self.dst = Path(r"Dummiy")
        if self.dst.is_dir(): shutil.rmtree(self.dst)
        self.dst.mkdir()
        DummiyFileCreator().create(self.dst,100,datetime(2023,5,1))
    
    def init(self):
        self.maker = FilepathListStream(self.dst)
        print(self.maker)
    
    def itertor(self):
        for f in self.maker:
            print(f)
        
        
if __name__ == "__main__":


    test = TestFilepathListStream()
    test.init()
    test.itertor()
    
    