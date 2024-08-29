from pyutil.logger.easy.EasyLogData import EasyLogData
import hashlib
from datetime import datetime


class SimpleLogData:
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
        if not isinstance(other, EasyLogData):raise TypeError
        return self.__now < other.__now

    def _out_log(self):
        return "_".join(self.__datas)

    def get_hash(self):
        return hashlib.md5(self._out_log().encode()).hexdigest()