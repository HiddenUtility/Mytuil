
from pathlib import Path
from pyutil.filetransfer.file_data_coping import FileDataCoping
from pyutil.filetransfer.file_data_remover import FileSourceDataRemover

class FileDataTransfer:
    __src : Path
    __dst : Path
    def __init__(self, src: Path, dst:Path):
        if not isinstance(src, Path): raise TypeError()
        if not isinstance(dst, Path): raise TypeError()
        if not src.exists(): raise FileNotFoundError()
        self.__src = src
        self.__dst = dst

    def __mkdir(self, path: Path):
        if path.exists(): return
        if not path.parent.exists():
            self.__mkdir(path.parent)
        path.mkdir()
            
    def run(self):
        self.__mkdir(self.__dst)
        FileDataCoping(self.__src, self.__dst).run()
        FileSourceDataRemover(self.__src).run()
        