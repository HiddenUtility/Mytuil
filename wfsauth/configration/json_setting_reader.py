import json
from pathlib import Path


from wfsauth.configration.SettingJsonFileKeyName import SettingJsonFileKeyName


class JsonSettingReader:
    """jsonを読み取った結果"""
    MUST_KEYS = [v.name for v in SettingJsonFileKeyName]
    __settings: dict[str, str]

    def __init__(self, src: Path):
        self.__settings =self.__load(src)

    def __str__(self):
        settings = [f"{key} : {self.__settings[key]}" for key in self.__settings]
        return "\n".join(settings)
    
    def __repr__(self):
        return self.__str__()
    
    def __getitem__(self, key: str) -> str:
        return self.__settings[key]
    

    def get(self, key:str) -> str | None:
        return self.__settings.get(key)

    def __load(self,src:Path) -> dict[str, str]:
        if not src.is_file(): raise FileNotFoundError(f"{src}がありません。")
        with open(src, "r", encoding="utf-8") as f:
            data: dict = json.load(f)
        for key in self.MUST_KEYS:
            if key not in data: raise KeyError(f"{src}json内に{key}が有りません。")
        return data

    @property
    def address(self) -> str:
        return self.__settings[SettingJsonFileKeyName.address.name]
    
    @property
    def user(self) -> str:
        return self.__settings[SettingJsonFileKeyName.address.name]
    
    @property
    def password(self) -> str:
        return self.__settings[SettingJsonFileKeyName.address.name]
    