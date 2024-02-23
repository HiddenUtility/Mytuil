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
        self.load()
    
    def load(self)-> object:
        if not self.__logpath.exists():
            self.out()
            return
        with open(self.__logpath, "rb") as f:
            self.__logs = pickle.load(f)



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
        if debug:
            print(f"{log}を登録します")
        self.__logs.add(log)
        if out:
            self.out()

    #@override  
    def out(self) -> None:
        
        try:
            self.__retry(self.__out)
        except RetryCountOverError as e:
            print("リトライ上限を超えました。")
            return
        except Exception as e:
            raise e
        else:
            return

    def exists(self, log: str):
        return log in self.__logs
