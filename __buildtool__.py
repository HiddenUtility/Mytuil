# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 16:20:30 2023

@author: nanik
"""
from abc import ABCMeta, abstractstaticmethod
from pathlib import Path
from shutil import rmtree, copy2, copytree, make_archive

class Process(metaclass=ABCMeta):
    @abstractstaticmethod
    def run(self):
        pass


class PycashRemover(Process):
    def __init__(self):
        pass
    
    def run(self):
        targets = [d for d in Path.cwd().glob("**/__pycache__") if d.is_dir()]
        list(map(rmtree, targets))
        
        
class SystemChashRemover(Process):
    def __init__(self, selfinitialize_dirnames: list[str]):
        self.__initialize_dirnames = selfinitialize_dirnames
        
    def run(self):
        for dirname in self.__initialize_dirnames:
            target = Path.cwd() / dirname
            if target.is_dir():
                rmtree(target)
            target.mkdir()
      
        
class NewPackageBuilder(Process):
    def __init__(self,
                 dst : Path,
                 build_name,
                 main_modules,
                 exclusion_pakcages,
                 ):
        self.__dst = dst / build_name
        self.__build_name = build_name
        self.__main_modules = main_modules
        self.__exclusion_pakcages = exclusion_pakcages
        
    def run(self):
        if self.__dst.is_dir():
            rmtree(self.__dst)
        self.__dst.mkdir()
        
        paths = [p for p in Path.cwd().glob("*")]
        for p in paths:
            if p.is_dir():
                if p.name in self.__exclusion_pakcages: continue
                copytree(p, self.__dst / p.name)
            elif p.is_file():
                if p.name not in self.__main_modules: continue
                copy2(p, self.__dst)

        make_archive(self.__dst , "zip" , self.__dst)


class BuildTool(Process):
    def __init__(self,
                 dst : Path,
                 build_name = "buildtool1000",
                 initialize_dirnames: list[str] = ["log","settings"],
                 main_modules: list[str] = [],
                 exclusion_pakcages: list[str] = [],
                 ):
        if not dst.exists(): raise NotADirectoryError()
        self.__dst = dst
        self.__build_name = build_name
        self.__initialize_dirnames = initialize_dirnames
        self.__main_modules = main_modules + ["README.md"]
        self.__exclusion_pakcages = exclusion_pakcages + [".git"]
        
        self.__processes:list[Process] = [
            PycashRemover(),
            SystemChashRemover(self.__initialize_dirnames),
            NewPackageBuilder(
                self.__dst,
                self.__build_name,
                self.__main_modules,
                self.__exclusion_pakcages
                ),
            ]
        
    def run(self):
        for process in self.__processes:
            process.run()
        
    
if __name__ == "__main__":
    
    dst = Path(r"F:\Git\dst")
    builder = BuildTool(
        dst,
        build_name = "buildtool1000",
        main_modules = ["__main__.py"],
        exclusion_pakcages = ["log","settings"], #//
        initialize_dirnames = ["log","settings"],
        ).run()
    
    
