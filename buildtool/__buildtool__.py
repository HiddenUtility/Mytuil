# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 16:20:30 2023

@author: nanik
"""

from pathlib import Path
from glob import glob
from shutil import rmtree, copy2, copytree

class BuildTool:
    def __init__(self):
        self.build_name = "build.v1000"
        self.mkdir_names = ["log","data","setting"]
        self.exclusion_pakcages = []
        self.main_modules = ["__buildtool__.py"]
        
    @staticmethod
    def remove_pycache(src: Path):
        target_path = str(src / "**/__pycache__")
        dirpaths = [Path(d) for d in glob(target_path, recursive=True)]
        for d in dirpaths:
            if d.is_dir(): rmtree(d)
            print("Delete !!",d)

    def copy(self, build_path: Path):
        paths = [p for p in Path.cwd().glob("*")]
        for p in paths:
            if p.is_dir():
                if p.name in self.exclusion_pakcages: continue
                copytree(p, build_path / p.name)
            elif p.is_file():
                if p.name not in self.main_modules: continue
                copy2(p, build_path)
        
        self.remove_pycache(build_path)
        
    def mkdir(self,build_path: Path):
        for dirname in self.mkdir_names:
            dirpath = build_path / dirname
            if dirpath.is_dir(): rmtree(dirpath)
            dirpath.mkdir()
            
        
    def run(self,dst: Path = None):
        dst = dst if dst is not None else Path.cwd().parent
        build_path = dst / self.build_name
        if build_path.is_dir(): rmtree(build_path)
        build_path.mkdir()
        self.copy(build_path)
        self.mkdir(build_path)


    
if __name__ == "__main__":
    
    import os
    desktop_path = Path(os.path.expanduser('~/Desktop'))
    tool = BuildTool()
    tool.run(desktop_path)