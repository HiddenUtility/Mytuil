import hashlib
from pathlib import Path
from zipfile import ZipFile

from hashutil.hash_checker import HashChecker

class FileHashChecker(HashChecker):
    def __init__(self, src:Path):
        if not src.exists():
            raise FileNotFoundError(f"{src}は存在しません。")
        self.__src = src
        self.__hash = self.get_hash(self.__src)

    def get_hash(self, f: Path):
        if not f.exists():
            raise FileNotFoundError(f"{f}は存在しません。")
        with open(self.__filepath, "rb") as f:
            data = f.read()
            return hashlib.sha256(data).hexdigest()
    
    # @override
    def is_same(self, target:Path) -> bool:
        return self.get_hash(self.__src) == self.get_hash(target)
    

    def to_path(self) -> Path:
        return self.__src
    
    def to_hash(self) -> Path:
        return self.__hash

