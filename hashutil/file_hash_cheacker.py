import hashlib
from pathlib import Path
from zipfile import ZipFile

from hashutil.hash_cheacker import HashCheacker

class FileHashCheacker(HashCheacker):
    def __init__(self, src:Path):
        if not src.exists():
            raise FileNotFoundError(f"{src}は存在しません。")
        self.__src = src
        self.__hash = self.get_hash(self.__src)

    def get_hash(self, f: Path):
        if not f.exists():
            raise FileNotFoundError(f"{f}は存在しません。")
        with open(self.__src, "rb") as data:
            return hashlib.sha256(data.read()).hexdigest()
    
    # @override
    def is_same(self, target:Path) -> bool:
        return self.get_hash(self.__src) == self.get_hash(target)
    # @override
    def to_path(self) -> Path:
        return self.__src
    # @override
    def to_hash(self) -> str:
        return self.__hash

