from pathlib import Path
from pyutil.hashutil.hash_label_maker import HashLableMaker

from pyutil.hashutil.hash_cheacker import HashCheacker

class FileHashCheacker(HashCheacker):
    def __init__(self, src:Path):
        if not src.exists():
            raise FileNotFoundError(f"{src}は存在しません。")
        self.__src = src
        self.__hash = self.get_hash(self.__src)


    def get_hash(self, f: Path)-> str:
        return HashLableMaker.get_file_hash(f)

    
    # @override
    def is_same(self, target:Path) -> bool:
        return self.get_hash(self.__src) == self.get_hash(target)
    # @override
    def to_path(self) -> Path:
        return self.__src
    # @override
    def to_hash(self) -> str:
        return self.__hash


    