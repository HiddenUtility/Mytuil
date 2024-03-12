from pyutil.filetransfer.file_data_coping import FileDataCoping
from pyutil.filetransfer.file_data_remover import FileSourceDataRemover


from pathlib import Path


class FailureFileRemover:
    XXX =f'*{FileDataCoping.XXX}'
    __src : Path
    def __init__(self,src : Path) -> None:
        '''転送失敗した途中ファイルを削除する。'''
        if not isinstance(src, Path): raise TypeError()
        self.__src = src

    def run(self):
        for target in [p for p in self.__src.glob(self.XXX) if p.is_file()]:
            FileSourceDataRemover(target).run()