import json
from pathlib import Path


class JsonSettingReader:
    MUST_KEYS = [
        "address",
        "user",
        "password",
        ]

    __settings: dict

    def __init__(self, src: Path):
        self.__settings =self.__load(src)

    def __str__(self):
        settings = [f"{key} : {self.__settings[key]}" for key in self.__settings]
        return "\n".join(settings)
    
    def __repr__(self):
        return self.__str__()
    
    def __getitem__(self,key):
        return self.__settings.get(key)

    def __load(self,src:Path) -> dict:
        if not src.is_file(): raise FileNotFoundError(f"{src}がありません。")
        with open(src, "r", encoding="utf-8") as f:
            data: dict = json.load(f)
        for key in self.MUST_KEYS:
            if key not in data: raise KeyError(f"{src}json内に{key}が有りません。")
        return data

    @property
    def address(self):
        return self.__settings["address"]
    @property
    def user(self):
        return self.__settings["user"]
    @property
    def password(self):
        return self.__settings["password"]