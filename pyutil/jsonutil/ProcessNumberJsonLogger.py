from datetime import datetime
from enum import Enum, auto
from pathlib import Path

from pyutil.pathuil.directory_creator import DirecotryCreator
from pyutil.hashutil.json_hash_creator import JsonHashCreator
from pyutil.jsonutil import SingleDictionaryJsonSerializer


class ProcessNumberJsonLogger:
    """今までどれだけ処理したかの数をjsonで記録する"""
    DATE_PATTEM = r"%Y-%m-%d %H:%M:%S"
    __outpath : Path
    __datas : dict
    __data_id : str

    class JsonLoggerKeyName(Enum):
        process_name = auto()
        all_processed_num = auto()
        file_creation_at = auto()
        last_modifed_at = auto()

    

    def __init__(self, dest : Path, process_name : str) -> None:
        """今までどれだけ処理したかの数をjsonで記録する

        Args:
            dest (Path): 出力先のディレクトリパス
            process_name (str): 処理名
        """
        DirecotryCreator(dest)
        self.__outpath = dest / f'{process_name}.json'
        self.__datas = {
            self.JsonLoggerKeyName.process_name.name : process_name,
            self.JsonLoggerKeyName.all_processed_num.name : 0,
            self.JsonLoggerKeyName.file_creation_at.name : self.__get_now(),
            self.JsonLoggerKeyName.last_modifed_at.name : self.__get_now(),
            }
        self.__data_id = ""
        self.__calc_id()

        if not self.__outpath.exists():
            self.__out()
        self.__load()

    def __calc_id(self):
        self.__data_id = JsonHashCreator(self.__datas).get_sha256()

    def __load(self):
        serializer = SingleDictionaryJsonSerializer().load(self.__outpath)
        self.__datas = serializer.datas
        self.__calc_id()
        if self.__data_id != serializer.id:
            raise Exception("idが一致しません。何者かに改ざんされています")

    def __out(self):
        serializer = SingleDictionaryJsonSerializer(self.__data_id, self.__datas)
        serializer.dump(self.__outpath)

    def add(self, num : int):
        """処理数を増やす"""
        self.__datas[self.JsonLoggerKeyName.all_processed_num.name] += num
        self.__datas[self.JsonLoggerKeyName.last_modifed_at.name] = self.__get_now()

        self.__calc_id()
        self.__out()

    def __get_now(self):
        return datetime.now().strftime(self.DATE_PATTEM)

    def get_all_process_number(self) -> int:
        """処理した数を得る

        Returns:
            int: 処理数
        """
        return self.__datas[self.JsonLoggerKeyName.all_processed_num.name]
    
    