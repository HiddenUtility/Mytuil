from __future__ import annotations


from pyutil.jsonutil.json_serializer import JsonSerializer


from enum import Enum, auto
from pathlib import Path


class SingleValueJsonSerializer:
    """簡易的なデータを読み書きできるjsonSerializer

    """
    class ResultKey(Enum):
        mid = auto()
        query = auto()

    __data : dict[ResultKey, str]

    def __init__(self,
                 data_id: str = "",
                 value: str = "",
                 ) -> None:
        self.__data = {
            self.ResultKey.mid.name : data_id,
            self.ResultKey.query.name : value,
        }



    def dump(self, dest: Path):
        JsonSerializer.to_json(dest, self.__data)

    def load(self, src : Path) -> SingleValueJsonSerializer:
        data = JsonSerializer.read_json(src)
        return SingleValueJsonSerializer(
            data[self.ResultKey.mid.name],
            data[self.ResultKey.query.name],
        )

    @property
    def id(self) -> str:
        return self.__data[self.ResultKey.mid.name]

    @property
    def value(self) -> str:
        return self.__data[self.ResultKey.query.name]
    
    def to_dict(self) -> dict:
        return self.__data


    