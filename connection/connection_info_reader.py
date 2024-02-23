from __future__ import annotations
from pathlib import Path
from connection.JsonSettingReader import JsonSettingReader
from connection.config import SystemDirectoryName


class ConnectionInfoReader:
    SETTINGS:Path = Path(SystemDirectoryName.SETTING_CONNECTION)

    def __init__(self):
        self.__readers = [JsonSettingReader(f) for f in self.SETTINGS.glob("*_connection_info.json") if f.is_file()]

    @property
    def readers(self) -> list[JsonSettingReader]:
        return self.__readers
    

    def to_readers(self) -> list[JsonSettingReader]:
        return self.__readers


