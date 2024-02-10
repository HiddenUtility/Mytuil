import hashlib
from time import sleep
from zipfile import ZipFile, ZIP_DEFLATED
from pathlib import Path
from pyutil.ziputil.CompressionFileSizeError import CompressionFileSizeError
from pyutil.ziputil.NotSameCompressionDataBinaryError import NotSameCompressionDataBinaryError
from pyutil.ziputil.ZipFileExistsError import ZipFileExistsError

class UsingZip:
    RETRY_N = 3
    def __init__(self,target: Path, error_size_rate = 0):
        if not isinstance(target, Path): raise TypeError
        if not target.is_file(): raise FileNotFoundError
        self.__filepath = target
        self.__size = target.stat().st_size
        self.__error_size = error_size_rate * self.__size
        self.__zi_path = self.__filepath.with_suffix(".zi_")
        self.__zippath = self.__filepath.with_suffix(".zip")
    
    def __get_hash_origin(self):
        with open(self.__filepath, "rb") as f:
            data = f.read()
            return hashlib.sha256(data).hexdigest()
    
    def __get_hash_zi_(self):
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
                err = e
                sleep(1)
        raise err
    
    
    def unlink(self):
        self.__delete_zp()
        for i in range(self.RETRY_N):
            try:
                if self.__zippath.exists():
                    self.__zippath.unlink()
                    return
                else:
                    return
            except Exception as e:
                err = e
                sleep(1)
        raise err       
    
    def __is_same_binary(self) -> bool:
        return self.__get_hash_origin() == self.__get_hash_zi_()
    

    def __unlink(self, f:Path):
        try:
            if f.exists():
                f.unlink()
        except Exception as e:
           raise Exception(f"{f.name}の削除に失敗しました。")

    def to_zip(self):
        if self.__zi_path.exists():
            self.__unlink(self.__zi_path)
        
        if self.__zippath.exists():
            if self.__get_hash_origin() == self.__get_hash_zip():
                raise ZipFileExistsError(f"{self.__zippath.name}が既に存在している。")
            else:
                self.__unlink(self.__zippath)
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
        return self.__get_hash_origin() == self.__get_hash_zip()

