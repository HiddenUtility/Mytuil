
from pathlib import Path
from pyutil.pathuil.directory_creator import DirecotryCreator

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
        DirecotryCreator.mkdir(path)

    def run(self, remove=True):
        self.__mkdir(self.__dst)
        FileDataCoping(self.__src, self.__dst,remove=remove).run()
        if not remove:
            return
        FileSourceDataRemover(self.__src).run()
        