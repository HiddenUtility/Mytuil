from pathlib import Path
from zipfile import ZipFile


class ZipProperties:
    __src : Path
    def __init__(self, zippath: Path) -> None:
        self.__src = zippath

    def get_original_file_size(self, suffix = '.csv') -> int:
        '''
        Parameters
        ----------
        zip_file_path : Path
            調べたいzipファイル。1つのファイルを圧縮していると仮定
        suffix : TYPE, optional
            元の名前の拡張子 The default is '.csv'.

        Returns
        -------
        int
            ファイルサイズ.

        '''
        target_file_name = self.__src.with_suffix(suffix).name
        try:
            with ZipFile(self.__src, 'r') as zipf:
                file_info = zipf.getinfo(target_file_name)
                file_size = file_info.file_size
                return file_size
        except FileNotFoundError:
            print(f"Error: File '{target_file_name}' not found in the ZIP archive.")
            return -1
        