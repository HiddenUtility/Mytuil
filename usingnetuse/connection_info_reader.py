from __future__ import annotations
from pathlib import Path
from usingnetuse.json_setting_reader import JsonSettingReader

from usingnetuse.config import SystemDirectory, SettingSuffix


class ConnectionInfoReader:
    SRC:Path = SystemDirectory.SETTING_CONNECTION_PATH
    PATTERN : str = SettingSuffix.PATTERN

    def __init__(self):
        self.__readers = [JsonSettingReader(f) for f in self.SRC.glob(self.PATTERN) if f.is_file()]

    @property
    def readers(self) -> list[JsonSettingReader]:
        return self.__readers
    

    def to_readers(self) -> list[JsonSettingReader]:
        return self.__readers


