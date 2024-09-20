

import json
from typing import Self
from pyutil.hashutil.hash_label_maker import HashLableMaker


class JsonHashCreator:
    """辞書等をjsonにしてhash値を得る"""
    __json : str
    def __init__(self, data: dict = {}) -> None:
        """辞書等をjsonにしてhash値を得る

        Args:
            data (dict, optional): ハッシュ化したい辞書. Defaults to {}.
        """
        self.__json = json.dumps(data)

    def set_dict(self, data: dict[str,str]) -> Self:
        return JsonHashCreator(data)

    def get_md5(self) -> str:
        return HashLableMaker.get_md5(self.__json.encode())

    def get_sha256(self) -> str:
        return HashLableMaker.get_sha256(self.__json.encode())
    
    def get_security(self, secrety:str) -> str:
        """暗号化hash

        Args:
            secrety (str): 暗号化キー

        Returns:
            str: SHA256で暗号化したハッシュ値
        """
        return HashLableMaker.get_encryption_hash(self.__json.encode(), secrety.encode())
    


