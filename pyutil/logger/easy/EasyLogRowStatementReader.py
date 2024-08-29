import re
from pyutil.logger.easy.EasyLogDataDatetimePattern import EasyLogDataDatetimePattern




class EasyLogRowStatementReader:
    """ログ行からさらに情報を読む"""
    PATTEN = EasyLogDataDatetimePattern.VALUE
    def __init__(self, log: str) -> None:
        pass

        pattern = r'\[(.*?)\]:\[(.*?)\]:\[(.*?)\]'
        match = re.search(pattern, log)

        if not match:
            raise ValueError("指定されたパスには必要な情報が含まれていません")

        # 抜き出した情報をクラス変数に格納
        self.__datetime = match.group(1)
        self.__log_level = match.group(2)
        self.__message = match.group(3)

    @property
    def datetime_label(self) -> str:
        return self.__datetime

    @property
    def loglevel(self) -> str:
        return self.__log_level

    @property
    def message(self) -> str:
        return self.__message
    
    
