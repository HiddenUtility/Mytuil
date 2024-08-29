from pathlib import Path
from pyutil.logger.easy.ana.EasyLogFileFinalAnalysis import EasyLogFileFinalAnalysis
from pyutil.logger.easy.EasyLogFileFinalWriteNumberError import EasyLogFileFinalWriteNumberError

from traceback import print_exc



class EasyLogFileFinalWriteNumber:
    """ログファイルの最終行を調べる"""
    __value : int
    def __init__(self, now_path : Path) -> None:
        self.__value = 0
        try:
            self.__value = EasyLogFileFinalAnalysis(now_path).write_num
        except Exception:
            print_exc()
            raise EasyLogFileFinalWriteNumberError()
    @property
    def value(self) -> Path:
        return self.__value
    
    