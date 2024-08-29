
import hashlib
from datetime import datetime

from pyutil.logger.easy.EasyLogDataDatetimePattern import EasyLogDataDatetimePattern
from pyutil.logger.log_data import LogLevel


class EasyLogData:
    """ログのストラクチャ"""
    PATTEN = EasyLogDataDatetimePattern.VALUE
    LOG_FORMAT : str = '[{timestamp}]:[{level}]:[{message}];'
    __datas : list[str]
    __level : LogLevel
    __now : datetime

    def __init__(self, *args: str, level=LogLevel.info):
        """ログのストラクチャ
        解析の際に改行認識するためにセミコロンはコロンにする。
        Args:
            level (LogLevel, optional): ログレベル. Defaults to LogLevel.info.
        """
        self.__datas = [str(v).replace(';',':') for v in args]
        self.__now = datetime.now()
        self.__level = level


    def __hash__(self):
        return hash(self.__out_log())

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__out_log()

    def __lt__(self, other):
        if not isinstance(other, EasyLogData):raise TypeError
        return self.__now < other.now

    def __le__(self, other):
        if not isinstance(other, EasyLogData):raise TypeError
        return self.__now <= other.now

    def __timestamp(self):
        return self.__now.strftime(r"%Y/%m/%d %H:%M:%S.%f")

    def __out_log(self) -> str:
        return self.LOG_FORMAT.format(
            timestamp=self.__timestamp(),
            level=self.__level.name,
            message="_".join(self.__datas),
            )
        # return f'{self.__timestamp()}]:[{self.__level.name}]:[{"_".join(self.__datas)};' 

    def get_hash(self):
        return hashlib.md5(self.__out_log().encode()).hexdigest()

    @property
    def now(self) -> datetime:
        return self.__now

    @property
    def value(self) -> str:
        return str(self)
    
    