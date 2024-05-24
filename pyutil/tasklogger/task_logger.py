from __future__ import annotations
from pathlib import Path
import pickle
from time import sleep
from pyutil.mylogger.logger import Logger
from pyutil.myerror.retry_count_over_error import RetryCountOverError

class TaskLogger(Logger):
    RETRY_LIMIT = 3
    DELAY_TIME = 0.1
    __name: str
    __dst: Path
    __logs: set[str]
    def __init__(self,
                 dst:Path = Path("./log"), 
                 name="", 
                 ):
        """
過去の処理履歴をローカルにバイナリ形式で保持することを目的とする。
string集合で管理する。
        """
        self.__dst = dst
        self.__dst.mkdir(exist_ok=True)
        self.__name = f"{self.__class__.__name__}" if name=="" else name
        self.__logpath = self.__dst / f"{self.__name}.bin"
        self.__logs = set()
        self.__load()
    
    def __load(self) -> None:
        """ストレージに出力済みの場合それを読み込む。
        """
        if not self.__logpath.exists():
            return
        with open(self.__logpath, "rb") as f:
            self.__logs = pickle.load(f)
            print(f'{self.__logpath}読み取りました。')

    def __out(self) -> None:
        with open(self.__logpath, "wb") as f:
            pickle.dump(self.__logs, f)

    def __retry(self, func, *args, **kargs):
        for i in range(self.RETRY_LIMIT):
            try:
                func(*args, **kargs)
            except Exception as e:
                print(e)
                sleep(self.DELAY_TIME)
                continue
            else:
                return
        raise RetryCountOverError()
            
    #@override
    def write(self, log: any, debug=True, out=True):
        """ログに登録する。

        Args:
            log (any): _description_
            debug (bool, optional): プリントする。__str__を呼ぶのでオリジナルオブジェクトの場合は実装してね。. Defaults to True.
            out (bool, optional): 登録と同時にストレージに出力する。大量に登録するときはFalseにしてあとで out メンバー読んでください. Defaults to True.
        """
        if debug:
            try:
                print(f"{log}を登録します")
            except Exception:
                pass

        self.__logs.add(log)
        if out:
            self.out()

    #@override  
    def out(self, debug=False) -> None:
        """ストレージに出力する。
        """
        
        try:
            self.__retry(self.__out)
        except RetryCountOverError as e:
            print("リトライ上限を超えました。")
            return
        except Exception as e:
            raise e
        else:
            if debug: print(f'{self.__logpath}出力しました。')
            return

    def exists(self, log: any):
        """過去に処理したかどうか

        Args:
            log (any): _description_

        Returns:
            _type_: _description_
        """
        return log in self.__logs
    
    def clear(self) -> None:
        """ログの初期化を行う。
        ストレージに過去ログあった場合も削除する。
        """
        self.__logpath.unlink(missing_ok=True)
        self.__logs = set()
