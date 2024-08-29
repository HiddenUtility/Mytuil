from typing import override


import hashlib

from zipfile import ZipFile, ZIP_DEFLATED, BadZipFile
from pathlib import Path

from pyutil.ziputil.i_zip_compressor import IZipCompressor
from pyutil.ziputil.error.CompressionFileSizeError import CompressionFileSizeError
from pyutil.ziputil.error.NotSameCompressionDataBinaryError import NotSameCompressionDataBinaryError
from pyutil.ziputil.error.ZipFileExistsError import ZipFileExistsError
from pyutil.ziputil.error.BadZipFileError import BadZipFileError
from pyutil.ziputil.error.ZipRetryCountOverError import ZipRetryCountOverError



class MonoFileZipCompressor(IZipCompressor):
    """ファイルを圧縮する
    
    元ファイルは消さない
    """
    RETRY_N = 3
    INTERMEDIATE_SUFFIX = '.ziptemp'
    ZIP_SUFFIX = '.zip'
    __temp_path: Path
    __zip_path: Path
    __target_filepath: Path

    def __init__(self,
                 target_filepath: Path, 
                 dest_dirpath: Path = None,
                 error_size_rate : float = 0.0,
                
                 ):
        """ファイルを圧縮する

        Args:
            target_filepath (Path): _description_
            dest_dirpath (Path, optional): 出力先のディレクトリパス。指定しないと同一ディレクトリになる. Defaults to None.
            error_size_rate (float, optional): 比率よりも小さすぎたらエラー. Defaults to 0.0.

        """

        if not isinstance(target_filepath, Path): raise TypeError
        if not target_filepath.is_file(): raise FileNotFoundError
        self.__target_filepath = target_filepath
        self.__size = target_filepath.stat().st_size
        self.__error_size = error_size_rate * self.__size
        self.__temp_path = self.__target_filepath.with_suffix(self.INTERMEDIATE_SUFFIX)
        self.__zip_path = self.__target_filepath.with_suffix(self.ZIP_SUFFIX)
        if dest_dirpath is not None:
            if not dest_dirpath.is_dir(): raise NotADirectoryError()
            self.__temp_path = dest_dirpath / self.__temp_path.name
            self.__zip_path = dest_dirpath / self.__zip_path.name


    
    def __get_hash_origin(self):
        with open(self.__target_filepath, "rb") as f:
            data = f.read()
            return hashlib.sha256(data).hexdigest()
    
    def __get_hash_zipfle(self, path):
        with ZipFile(path, 'r') as zip_file:
            with zip_file.open(self.__target_filepath.name) as origin:
                data = origin.read()
                return hashlib.sha256(data).hexdigest()

    def __delete_zp(self):
        for i in range(self.RETRY_N):
            try:
                if self.__temp_path.exists():
                    self.__temp_path.unlink()
                    return
                else:
                    return
            except Exception as e:
                error = e
        raise ZipRetryCountOverError(str(error))
    
    def __is_same_binary_at_temp(self) -> bool:
        """tempファイルのバイナリに問題ないか"""
        try:
            return self.__get_hash_origin() == self.__get_hash_zipfle(self.__temp_path) #self.__get_hash_exists_zipfle()
        except BadZipFile:
            raise BadZipFileError(f'{self.__temp_path}はzipファイルではない可能性があります。')
        except Exception as e:
            raise e

    def __unlink(self, f:Path):
        try:
            if f.exists():
                f.unlink()
        except Exception:
           raise Exception(f"{f.name}の削除に失敗しました。")

    def __to_zip(self):
        if self.__temp_path.exists():
            self.__unlink(self.__temp_path)
        
        if self.__zip_path.exists():
            if self.__get_hash_origin() == self.__get_hash_zipfle(self.__zip_path):
                raise ZipFileExistsError(f"{self.__zip_path.name}が既に存在している。")
            else:
                raise ZipFileExistsError(f"{self.__zip_path.name}が既に存在していますが、バイナリが一致しません。")

        try:
            with ZipFile(self.__temp_path, "w", compression=ZIP_DEFLATED) as zf:
                zf.write(self.__target_filepath, arcname=self.__target_filepath.name)
        except Exception as e:
            self.__delete_zp()
            raise e
        
        try:
            same = self.__is_same_binary_at_temp()
        except Exception as e:
            self.__delete_zp()
            raise e
            
        if not same:
            self.__delete_zp()
            raise NotSameCompressionDataBinaryError()
        
        if self.__temp_path.stat().st_size < self.__error_size:
            self.__delete_zp()
            raise CompressionFileSizeError()
        
        try:
            if self.__temp_path.exists():
                self.__temp_path.rename(self.__zip_path)
        except Exception as e:
           raise Exception(f"{self.__zip_path.name}への変更に失敗しました。")
        
    @property
    def temp_path(self) -> Path:
        return self.__temp_path
    
    @property
    def zip_path(self) -> Path:
        return self.__zip_path
    
    def is_same_binary_at_origin(self) -> bool:
        '''
        オリジナルデータとzipが同じファイルかどうかチェックする。
        zipが存在しなければ False
        zipが開けなければ False

        return: bool
        '''
        if not self.__zip_path.exists():
            return False
        try:
            return self.__get_hash_origin() == self.__get_hash_zipfle(self.__zip_path)
        except BadZipFile:
            return False
        except Exception as e:
            raise e

    
    def unlink(self):
        '''中間ファイルや出力先が存在している場合は削除する'''
        self.__delete_zp()
        for _ in range(self.RETRY_N):
            try:
                if self.__zip_path.exists():
                    self.__zip_path.unlink()
                    return
                else:
                    return
            except Exception as e:
                error = e
        raise ZipRetryCountOverError(str(error))

    @override
    def to_zip(self, unlink_src = False):
        """圧縮する

        Args:
            delete_src (bool, optional): 元ファイルを消す. Defaults to False.
        """
        self.__to_zip()

        if unlink_src:
            self.__target_filepath.unlink(missing_ok=True)

