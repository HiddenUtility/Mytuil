from enum import Enum, auto


class LogLevel(Enum):
    """ログレベル

    emerg : 実行不可能なエラー
    alert : 即時対応が必要
    crit : #致命的なエラー
    error : 一般エラー
    warn : 警告
    notice : 注意
    info  : 一般
    debug  : デバック
    """
    emerg = auto() 
    alert = auto() 
    crit = auto() 
    error = auto() 
    warn = auto() 
    notice = auto() 
    info = auto() 
    debug = auto() 