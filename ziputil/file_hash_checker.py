import hashlib
from pathlib import Path
from zipfile import ZipFile

class FileHashChecker:
    def __init__(self, src:Path):
        if not src.exists():
            raise FileNotFoundError(f"{src}は存在しません。")
        self.__src = src

    def get_hash(self, f: Path):
        if not f.exists():
            raise FileNotFoundError(f"{f}は存在しません。")
        with open(self.__filepath, "rb") as f:
            data = f.read()
            return hashlib.sha256(data).hexdigest()
    
    def get_hash_zip(self, zippath: Path, origin_name: str):
        if not zippath.exists():
            raise FileNotFoundError(f"{zippath}は存在しません。")
        with ZipFile(zippath, 'r') as zip_file:
            with zip_file.open(origin_name) as origin:
                data = origin.read()
                return hashlib.sha256(data).hexdigest()
    
    def is_same(self, target:Path) -> bool:
        return self.get_hash(self.src) == self.get_hash(target)

    def is_same_zip(self, zippath:Path) -> bool:
        return self.get_hash(self.src) == self.get_hash_zip(zippath)
        