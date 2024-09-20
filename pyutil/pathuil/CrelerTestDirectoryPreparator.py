from pyutil.pathuil.directory_creator import DirectoryCreator


import shutil
from pathlib import Path


class CrearTestDirectoryPreparator:
    """用意しているテスト用データを指定のディレクトリにコピーする"""
    __dest : Path
    __src : Path


    def __init__(self,src: Path, dest:Path):
        if not src.exists():
            raise NotADirectoryError(f'{src}がない')
        self.__src, self.__dest = src, dest

    def run(self):
        print("削除中...")
        shutil.rmtree(self.__dest,ignore_errors=True)
        DirectoryCreator.mkdir(self.__dest.parent)
        print("作成中...")
        shutil.copytree(self.__src, self.__dest)

        