import json
from pathlib import Path
from pyutil.pathuil import DirectoryCreator

from pyutil.prefeutil.interface.PreferencesFileSerializer import PreferencesFileSerializer
from pyutil.prefeutil.json.db.DataBaseJsonKeyName import DataBaseJsonKeyName


class DataBasePreferencesJsonFileSerializer(PreferencesFileSerializer):
    """DataBaseの設定をJson設定ファイルに書かれてる"""
    DataBaseJsonKeyName
    __host : str
    __port : int
    __db_name : str
    __user_name : str
    __password : str
    __src : Path
    __data : dict

    def __init__(self, path : str | Path, exixts_error=False) -> None:
        """DataBaseの設定をJson設定ファイルを読む

        Args:
            path (str | Path): 設定ファイルのパス
            exixts_error (bool, optional): 読む先ないときにエラーにするかどうか.Falseだとなければデフォを作る Defaults to False.

        Raises:
            FileNotFoundError: 読む先ない
        """
        self.__src = Path(path)
        if not self.__src.exists():
            if exixts_error:
                raise FileNotFoundError(f'{self.__src}がありません。')
            else:
                self.__dump(self.__src)

        with open(self.__src, "r", encoding="utf-8") as data:
            info = json.loads(data.read())

        self.__host = str(info[DataBaseJsonKeyName.host.name])
        self.__port = int(info[DataBaseJsonKeyName.port.name])  
        self.__db_name = str(info[DataBaseJsonKeyName.dbname.name])  
        self.__user_name = str(info[DataBaseJsonKeyName.username.name])  
        self.__password = str(info[DataBaseJsonKeyName.password.name])
        self.__data = info

    def __dump(self,dest : Path):
        data = {
            DataBaseJsonKeyName.host.name : "localhost",
            DataBaseJsonKeyName.port.name : 5432,
            DataBaseJsonKeyName.dbname.name : "postgres",
            DataBaseJsonKeyName.username.name : "postgres",
            DataBaseJsonKeyName.password.name : "postgres",
        }
        DirectoryCreator(dest.parent)
        with open(dest, 'w') as json_file:
            json.dump(data, json_file, indent=len(data))

    @property
    def host(self) -> str:
        return self.__host

    @property
    def port(self) -> int:
        return self.__port
    
    @property
    def db_name(self) -> str:
        return self.__db_name

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def password(self) -> str:
        return self.__password
    
    def to_dict(self) -> dict:
        return self.__data
    