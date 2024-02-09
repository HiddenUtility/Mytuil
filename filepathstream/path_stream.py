from __future__ import annotations
from abc import ABCMeta, abstractmethod
from datetime import datetime

class PathStream(metaclass=ABCMeta):
    @abstractmethod
    def to_filepaths(self):
        raise NotImplementedError()
    
    @abstractmethod
    def get_file_size(self):
        raise NotImplementedError()
    
    @abstractmethod
    def sort(self)->PathStream:
        raise NotImplementedError()
    
    @abstractmethod
    def narrow_down_datetime(self,start: datetime, end: datetime)->PathStream:
        raise NotImplementedError()
    
    @abstractmethod
    def reduce_number(self)->PathStream:
        raise NotImplementedError()
    
    @abstractmethod
    def reduce_rate(self)->PathStream:
        raise NotImplementedError()
    
    @abstractmethod
    def drop_filenames(self,names: list[str])->PathStream:
        raise NotImplementedError()
    
    @abstractmethod
    def drop_datetimes(self,datetimes: list[datetime])->PathStream:
        raise NotImplementedError()
    
    @abstractmethod
    def narrow_to_contain_keys(self,*key: str) -> PathStream:
        raise NotImplementedError()
        