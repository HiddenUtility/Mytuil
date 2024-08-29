from __future__ import annotations
from datetime import datetime
from pathlib import Path
import re

from pyutil.myerror.HasNotDatetimeError import NameHasNotDatetimeError

class DateTime14LabelFilepath:
    """%Y%m%d%H%M%S形式のdatetime情報を持つファイルパス"""
    def __init__(self,f: Path):
        if not f.is_file():raise ValueError(f"{f}はfilepathではありません。")
        self.filepath = f
        self.name = f.name
        self.__datetime = self._get_datetime(f.stem)
        self.suffix = f.suffix

    def _get_datetime(self, name: str) -> datetime:
        findings = re.findall(r"\d{14}",name)
        for str14 in findings:
            try:
                return datetime.strptime(str14, r'%Y%m%d%H%M%S') 
            except:
                pass
        raise NameHasNotDatetimeError(f"{name}はdatetime情報を持ちません。")
    
    def __eq__(self, obj : DateTime14LabelFilepath):
        return self.__datetime == obj.to_datetime()
    
    def __ne__(self, obj : DateTime14LabelFilepath):
        return self.__datetime != obj.to_datetime()
    
    def __lt__(self, obj : DateTime14LabelFilepath):
        return self.__datetime < obj.to_datetime()
    
    def __le__(self, obj : DateTime14LabelFilepath):
        return self.__datetime <= obj.to_datetime()
    
    def __gt__(self, obj : DateTime14LabelFilepath):
        return self.__datetime > obj.to_datetime()
    
    def __ge__(self, obj : DateTime14LabelFilepath):
        return self.__datetime >= obj.to_datetime()
    
    def __str__(self):
        return f"{self.__datetime}: {self.filepath.parent.name}/{self.filepath.name}"
    
    def __repr__(self):
        return self.__str__()
    
    def __hash__(self):
        return hash(self.__datetime)
    
    def to_datetime(self) -> datetime:
        return self.__datetime
    
    def to_filepath(self) -> Path:
        return self.filepath
    

