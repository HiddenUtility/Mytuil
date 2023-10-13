# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 16:07:58 2023

@author: nanik
"""

from pathlib import Path
from glob import glob
from shutil import rmtree



def main():
    cd = str(Path.cwd() / "**/__pycache__")
    dirpaths = [Path(d) for d in glob(cd, recursive=True)]
    for d in dirpaths:
        if d.is_dir(): rmtree(d)
        print("Delete !!",d)
    
if __name__ == '__main__':
    main()
    
    