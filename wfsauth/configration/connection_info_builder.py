from __future__ import annotations
from pathlib import Path

from wfsauth.configration.SystemDirectoryPath import SystemSettingFileSavedDirectoryPath
from wfsauth.configration.json_setting_reader import JsonSettingReader
from wfsauth.configration.SettingJsonFileSuffix import SettingJsonFileSuffixPattern


class ConnectionInformationBuilder:
    SRC:Path = SystemSettingFileSavedDirectoryPath.VALUE
    PATTERN : str = SettingJsonFileSuffixPattern.VALUE

    def __init__(self):
        self.__readers = [JsonSettingReader(f) for f in self.SRC.glob(self.PATTERN) if f.is_file()]

    @property
    def readers(self) -> list[JsonSettingReader]:
        return self.__readers
    

    def to_readers(self) -> list[JsonSettingReader]:
        return self.__readers


