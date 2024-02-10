from __future__ import annotations
from pathlib import Path
from datetime import date
from myutil import UsingPickle
from pyutil.tkinterutil.setting_paramter_keys import SettingParamterKeys


class SettingParamter:
    __bin_path = Path("./tkinterutil/setting/memory.bin")
    def __init__(self,
                 src = Path(),
                 dst = Path(),
                 dirname = "",
                 datedata = date(2000, 1, 1),
                 ) -> None:
        self.__data = {
            SettingParamterKeys.SRC : src,
            SettingParamterKeys.DST : dst,
            SettingParamterKeys.DATE : datedata,
            SettingParamterKeys.DIRNAME : dirname
        }

    def __str__(self) -> str:
        return f"""
src = {self.src}
dst = {self.dst}
dirname = {self.dirname}
date = {self.datedata}
        """

    def load(self):
        if self.__bin_path.exists():
            return UsingPickle.load(self.__bin_path)
        return SettingParamter()
    
    def dump(self):
        UsingPickle.dump(self.__bin_path, self)
    
    def __getitme__(self, key: SettingParamterKeys):
        return self.__data[key]
    
    @property
    def src(self) -> Path:
        return self.__data[SettingParamterKeys.SRC]
    
    @property
    def dst(self) -> Path:
        return self.__data[SettingParamterKeys.DST]

    @property
    def datedata(self) -> date:
        return self.__data[SettingParamterKeys.DATE]

    @property
    def dirname(self) -> str:
        return self.__data[SettingParamterKeys.DIRNAME]
    
