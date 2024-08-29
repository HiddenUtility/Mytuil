from pathlib import Path

from pyutil.logger.easy.ana.EasyLogFileFinaLoader import EasyLogFileFinaLoader
from pyutil.logger.log_data import LogLevel
from pyutil.logger.easy.EasyLogRowStatementReader import EasyLogRowStatementReader

class EasyLogFileFinalAnalysis:
    """ログファイルを解析する"""
    __loader : EasyLogFileFinaLoader
    def __init__(self, log_path : Path) -> None:
        self.__src = log_path
        self.__loader = EasyLogFileFinaLoader(self.__src)

    @property
    def write_num(self) -> int:
        return self.__loader.write_num
    