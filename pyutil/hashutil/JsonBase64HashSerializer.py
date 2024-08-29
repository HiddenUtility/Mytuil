from __future__ import annotations


import base64
import json


class JsonBase64HashSerializer:
    """辞書等をjsonにしてbase64値を得たり、戻したりする"""
    __data : dict[str, str]
    __json : str
    __base64_value : str


    def __init__(self, data: dict = {'Name':'Json'}) -> None:
        """_summary_

        Args:
            data (_type_, optional): _description_. Defaults to {'Name':'Json'}.
        """
        self.__data = data
        self.__json = json.dumps(data)
        self.__base64_value = self.dict_to_base64(data)


    def load(self, base64_data: str):
        """base64を取り込む

        Args:
            base64_data (str): _description_

        Returns:
            _type_: _description_
        """
        return JsonBase64HashSerializer(JsonBase64HashSerializer.base64_to_dict(base64_data))
        
    @staticmethod
    def dict_to_base64(data_dict: dict[str, str]) -> str:
        """辞書をbase64にする

        Args:
            data_dict (dict[str, str]): _description_

        Returns:
            str: _description_
        """
        json_data = json.dumps(data_dict)
        base64_data = base64.b64encode(json_data.encode()).decode()
        return base64_data

    @staticmethod
    def base64_to_dict(base64_data: str) -> dict[str, str]:
        """base64を辞書にする

        Args:
            base64_data (str): _description_

        Returns:
            dict[str, str]: _description_
        """
        json_data = base64.b64decode(base64_data).decode()
        data_dict = json.loads(json_data)
        return data_dict
    

    @property
    def data(self) -> dict[str, str]:
        return self.__data


    @property
    def json(self) -> json:
        return self.__json
    
    @property
    def base64(self) -> str:
        return self.__base64_value
