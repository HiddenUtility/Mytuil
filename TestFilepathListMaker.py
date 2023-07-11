# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 22:11:30 2023

@author: iwill
"""
from pathlib import Path
from datetime import datetime
import shutil
from Myutil.DummiyFileCreator import DummiyFileCreator
from Myutil.FilepathListMaker import FilepathListMaker


class TestFilepathListMaker:
    def __init__(self):
        self.dst = Path(r"Dummiy")
        if self.dst.is_dir(): shutil.rmtree(self.dst)
        self.dst.mkdir()
        DummiyFileCreator().create(self.dst,100,datetime(2023,5,1))
    
    def init(self):
        maker = FilepathListMaker(self.dst)
        print(maker)
        
if __name__ == "__main__":


    test = TestFilepathListMaker()
    test.init()
    
    