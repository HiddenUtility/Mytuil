import hashlib
from time import sleep
from zipfile import ZipFile, ZIP_DEFLATED, BadZipFile
from pathlib import Path
from pyutil.ziputil.error.CompressionFileSizeError import CompressionFileSizeError
from pyutil.ziputil.error.NotSameCompressionDataBinaryError import NotSameCompressionDataBinaryError
from pyutil.ziputil.error.ZipFileExistsError import ZipFileExistsError
from pyutil.ziputil.error.BadZipFileError import BadZipFileError
from pyutil.ziputil.error.ZipRetryCountOverError import ZipRetryCountOverError


class UsingZip:
    RETRY_N = 3
    INTERMEDIATE_SUFFIX = '.zi_'
    ZIP_SUFFIX = '.zip'
    __zi_path: Path
    __zippath: Path
    __filepath: Path
    def __init__(self,
                 target: Path, 
                 dst: Path = None,
                 error_size_rate : float = 0.0,
                
                 ):
        '''
        Paramter
        ____________________________________________________________
        target: Path 圧縮対象のファイルパス
        dst: 出力先を変えたい場合
        error_size_rate : float 圧縮後に比率より小さいデータサイズの場合はエラーにする。

        '''
        if not isinstance(target, Path): raise TypeError
        if not target.is_file(): raise FileNotFoundError
        self.__filepath = target
        self.__size = target.stat().st_size
        self.__error_size = error_size_rate * self.__size
        self.__zi_path = self.__filepath.with_suffix(self.INTERMEDIATE_SUFFIX)
        self.__zippath = self.__filepath.with_suffix(self.ZIP_SUFFIX)
        if dst is not None:
            if not dst.is_dir(): raise NotADirectoryError()
            self.__zi_path = dst / self.__zi_path.name
            self.__zippath = dst / self.__zippath.name
    
    def __get_hash_origin(self):
        with open(self.__filepath, "rb") as f:
            data = f.read()
            return hashlib.sha256(data).hexdigest()
    
    def __get_hash_exists_zipfle(self):
        with ZipFile(self.__zi_path, 'r') as zip_file:
            with zip_file.open(self.__filepath.name) as origin:
                data = origin.read()
                return hashlib.sha256(data).hexdigest()
    
    def __get_hash_zip(self):
        with ZipFile(self.__zippath, 'r') as zip_file:
            with zip_file.open(self.__filepath.name) as origin:
                data = origin.read()
                return hashlib.sha256(data).hexdigest()
            
    def __delete_zp(self):
        for i in range(self.RETRY_N):
            try:
                if self.__zi_path.exists():
                    self.__zi_path.unlink()
                    return
                else:
                    return
            except Exception as e:
                error = e
        raise ZipRetryCountOverError(str(error))
    
    def __is_same_binary(self) -> bool:
        try:
            return self.__get_hash_origin() == self.__get_hash_exists_zipfle()
        except BadZipFile:
            raise BadZipFileError(f'{self.__zi_path}はzipファイルではない可能性があります。')
        except Exception as e:
            raise e

    def __unlink(self, f:Path):
        try:
            if f.exists():
                f.unlink()
        except Exception as e:
           raise Exception(f"{f.name}の削除に失敗しました。")

    def __to_zip(self):
        if self.__zi_path.exists():
            self.__unlink(self.__zi_path)
        
        if self.__zippath.exists():
            if self.__get_hash_origin() == self.__get_hash_zip():
                raise ZipFileExistsError(f"{self.__zippath.name}が既に存在している。")
            else:
                raise ZipFileExistsError(f"{self.__zippath.name}が既に存在していますが、バイナリが一致しません。")

        try:
            with ZipFile(self.__zi_path, "w", compression=ZIP_DEFLATED) as f:
                f.write(self.__filepath, arcname=self.__filepath.name)
        except Exception as e:
            self.__delete_zp()
            raise e
        
        try:
            same = self.__is_same_binary()
        except Exception as e:
            self.__delete_zp()
            raise e
            
        if not same:
            self.__delete_zp()
            raise NotSameCompressionDataBinaryError()
        
        if self.__zi_path.stat().st_size < self.__error_size:
            self.__delete_zp()
            raise CompressionFileSizeError()
        
        try:
            if self.__zi_path.exists():
                self.__zi_path.rename(self.__zippath)
        except Exception as e:
           raise Exception(f"{self.__zippath.name}への変更に失敗しました。")
        
    @property
    def zi_path(self) -> Path:
        return self.__zi_path
    
    @property
    def zippath(self) -> Path:
        return self.__zippath
    
    def is_same_binary(self) -> bool:
        '''
        オリジナルデータとzipが同じファイルかどうかチェックする。
        zipが存在しなければ False
        zipが開けなければ False

        return: bool
        '''
        if not self.__zippath.exists(): return False
        try:
            return self.__get_hash_origin() == self.__get_hash_zip()
        except BadZipFile:
            return False
        except Exception as e:
            raise e

    
    def unlink(self):
        '''中間ファイルや出力先が存在している場合は削除する'''
        self.__delete_zp()
        for _ in range(self.RETRY_N):
            try:
                if self.__zippath.exists():
                    self.__zippath.unlink()
                    return
                else:
                    return
            except Exception as e:
                error = e
        raise ZipRetryCountOverError(str(error))

    def to_zip(self):
        '''圧縮する。'''
        self.__to_zip()
