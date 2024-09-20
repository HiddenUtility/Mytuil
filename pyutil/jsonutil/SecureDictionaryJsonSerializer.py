from typing import Mapping, Self, overload
from enum import Enum, auto
from datetime import datetime
from pathlib import Path
from pyutil.myerror.DetaTamperingDetectedError import DetaTamperingDetectedError
from pyutil.hashutil.json_hash_creator import JsonHashCreator
from pyutil.jsonutil.JsonSaver import JsonDataSaver
from pyutil.jsonutil.json_serializer import JsonSerializer


class SecureDictionaryJsonSerializer:
    """簡易的なセキュリティ付きで辞書データを読み書きできるjsonSerializer
    - bodyは自分で設計してくれ.

    ## 使い方
    ### 出力
    1. 空でインスタンスする
    1. set_bodyでデータをセットする.
    1. dumpで出力する

    ## 読み取り
    1. 空でインスタンスする
    1. loadで読む
    1. bodyで内容を取り出す

    """
    class ResultKey(Enum):
        name = auto()
        id = auto()
        file_creation_at = auto()
        last_modifed_at = auto()
        body = auto()

    __data : Mapping[ResultKey, str]

    @overload
    def __init__(self):
        """簡易的なセキュリティ付きで辞書データを読み書きできるjsonSerializer
        ## 使い方
        ### 出力
        1. 空でインスタンスする
        1. set_bodyでデータをセットする.
        1. dumpで出力する

        ## 読み取り
        1. 空でインスタンスする
        1. loadで読む
        1. bodyで内容を取り出す
        """

    def __init__(self,
                 data : dict[any, any] = {}
                 ) -> None:

        if data == {}:
            data = {
                self.ResultKey.name.name : 'name',
                self.ResultKey.file_creation_at.name : str(datetime.now()),
                self.ResultKey.last_modifed_at.name : str(datetime.now()),
                self.ResultKey.id.name : 'id',
                self.ResultKey.body.name : {},
            }
            data[self.ResultKey.id.name] = self.__calc_secret(data)
        else:
            data_id = self.__calc_secret(data)
            if data_id != data[self.ResultKey.id.name]:
                raise DetaTamperingDetectedError('内容が改ざんされています')
        
        self.__data = data
    
    def __calc_secret(self, data: dict) -> str:
        """id計算部がばれなければ改ざんされないはず"""
        body = data[self.ResultKey.body.name]
        secrity_code = f'{data[self.ResultKey.name.name]:}:{data[self.ResultKey.file_creation_at.name]:}:{data[self.ResultKey.last_modifed_at.name]:}'
        return JsonHashCreator(body).get_security(secrity_code)

    
    def set_body(self, name : str, body: Mapping[str, str]) -> Self:
        """データをセットする

        Args:
            name (str): 名前
            datas (Mapping[str, str]): 入れたいデータ

        Returns:
            Self: セットした結果を返す
        """
        data = {
            self.ResultKey.name.name : name,
            self.ResultKey.file_creation_at.name : self.__data[self.ResultKey.file_creation_at.name],
            self.ResultKey.last_modifed_at.name : str(datetime.now()),
            self.ResultKey.id.name : 'id',
            self.ResultKey.body.name : body,
        }
        data[self.ResultKey.id.name] = self.__calc_secret(data)

        return SecureDictionaryJsonSerializer(data)
        
    def dump(self, dest: Path):
        """jsonで出力.セキュリティが更新される．

        Args:
            dest (Path): ファイルパス
        """
        data = {
            self.ResultKey.name.name : self.__data[self.ResultKey.name.name],
            self.ResultKey.file_creation_at.name : self.__data[self.ResultKey.file_creation_at.name],
            self.ResultKey.last_modifed_at.name : str(datetime.now()),
            self.ResultKey.id.name : 'id',
            self.ResultKey.body.name : self.__data[self.ResultKey.body.name],
        }
        data[self.ResultKey.id.name] = self.__calc_secret(data)
        JsonDataSaver(dest, data).run()


    def load(self, src : Path) -> Self:
        """jsonを読む

        Args:
            src (Path): _description_

        Returns:
            Self: _description_
        """
        data = JsonSerializer.read_json(src)
        return SecureDictionaryJsonSerializer(data)

    @property
    def name(self) -> str:
        """入れた名前を得る

        Returns:
            str: _description_
        """
        return self.__data[self.ResultKey.name.name]
 

    @property
    def body(self) -> dict:
        """入れたデータの得る"""
        return self.__data[self.ResultKey.body.name]

    def to_dict(self) -> dict:
        """このオブジェクト全体を辞書に変換する"""
        return self.__data
    
