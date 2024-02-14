import hashlib
from datetime import datetime


class MyLogData:
    def __init__(self, *args: str):
        self.__datas = [str(v) for v in args]
        self.__now = datetime.now()

    def __hash__(self):
        return hash(self._out_log())

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self._out_log()

    def __lt__(self, other):
        if not isinstance(other, MyLogData):raise TypeError
        return self.__now < other.now
    
    def __le__(self, other):
        if not isinstance(other, MyLogData):raise TypeError
        return self.__now <= other.now
    
    def _timestamp(self):
        return self.__now.strftime("%Y/%m/%d %H:%M:%S.%f")

    def _out_log(self):
        return self._timestamp() + ": " + "_".join(self.__datas)

    def get_hash(self):
        return hashlib.md5(self._out_log().encode()).hexdigest()
    
    @property
    def now(self) -> datetime:
        return self.__now