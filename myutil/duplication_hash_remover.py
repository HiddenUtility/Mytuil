# -*- coding: utf-8 -*-
import os
import shutil
from tqdm import tqdm
from pathlib import Path
from datetime import datetime
import hashlib
from myutil.using_pickle import UsingPickle


class DuplicationRemover:
    DIRNAME_ALL = "ALL"
    LOG_NAME = "hash.bin"
    
    def __init__(self, src: Path):
        self.src = src
        self.dst = self.src / self.DIRNAME_ALL
        self.logpath = self.dst / self.LOG_NAME
        if not self.dst.is_dir(): self.dst.mkdir()
        self.dirnames = os.listdir(self.src)
        self.past = set()
        if self.logpath.is_file():
            self.past = UsingPickle.load(self.logpath)
        self.count = len(self.past)
        
    def _get_hash(self,filepath):
        with open(filepath,"rb") as f:
            body = f.read()
            has = hashlib.sha256(body).hexdigest()
        return has
    def get_filepath_hashs(self) -> dict[str, Path]:
        filepaths = []
        for dirname in self.dirnames:
            if self.DIRNAME_ALL == dirname: continue
            src = self.src / dirname
            fs = [f for f in src.glob("*.jpg") if f.is_file()]
            filepaths+=fs
        hashs = {}
        for f in filepaths:
            hashs[self._get_hash(f)] = f
        return hashs
    def set_past_hashs(self) -> set[str]:
        for f in self.dst.glob("*.jpg"):
            if not f.is_file():continue
            self.past.add(self._get_hash(f))
            
    def run(self):
        self.set_past_hashs()
        hashs = self.get_filepath_hashs()
        
        for hs in tqdm(hashs, desc="moving..."):
            if hs in self.past: continue
            dst = self.dst / "{0:06}.jpg".format(self.count)
            shutil.move(hashs[hs], dst)
            self.past.add(hs)
            self.count = len(self.past)

        
        UsingPickle.dump(self.logpath, self.past)
        
        