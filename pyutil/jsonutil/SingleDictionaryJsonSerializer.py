from __future__ import annotations


from pyutil.jsonutil.json_serializer import JsonSerializer



from enum import Enum, auto
from pathlib import Path


class SingleDictionaryJsonSerializer:
    """簡易的な辞書データを読み書きできるjsonSerializer

    """
    class ResultKey(Enum):
        data_id = auto()
        datas = auto()

    __data : dict[ResultKey, str]

    def __init__(self,
                 data_id: str = "",
                 datas: dict = {},
                 ) -> None:
        """簡易的な辞書データを読み書きできるjsonSerializer

        Args:
            data_id (str, optional): データの識別用. Defaults to "".
            datas (dict, optional): 可能したいデータ. Defaults to {}.
        """
        self.__data = {
            self.ResultKey.data_id.name : data_id,
            self.ResultKey.datas.name : datas,
        }

    def dump(self, dest: Path):
        """jsonで出力

        Args:
            dest (Path): ファイルパス
        """
        JsonSerializer.to_json(dest, self.__data)

    def load(self, src : Path) -> SingleDictionaryJsonSerializer:
        data = JsonSerializer.read_json(src)
        return SingleDictionaryJsonSerializer(
            data[self.ResultKey.data_id.name],
            data[self.ResultKey.datas.name],
        )

    @property
    def id(self) -> str:
        """識別id"""
        return self.__data[self.ResultKey.data_id.name]

    @property
    def datas(self) -> dict:
        """入れたデータ"""
        return self.__data[self.ResultKey.datas.name]

    def to_dict(self) -> dict:
        """このオブジェクト全体を辞書に変換する"""
        return self.__data
    
