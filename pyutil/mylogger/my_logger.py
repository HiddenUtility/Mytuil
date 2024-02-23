from __future__ import annotations
from datetime import datetime
from pathlib import Path
from copy import copy
import time
import traceback
from pyutil.mylogger.my_log_data import MyLogData
from pyutil.mylogger.logger import Logger
from pyutil.myerror.retry_count_over_error import RetryCountOverError 


class MyLogger(Logger):
    RETRY_LIMIT = 3
    DELAY_TIME = 0.1
    __name: str
    __dst: Path
    __logs: list[MyLogData]
    __start_time : dict[str, float]
    def __init__(self,
                 dst:Path = Path("./log"), 
                 name="", 
                 split_day=True, 
                 limit=5
                 ):
        """
        ログを作成する。排他とか無いので注意
        
        """
        self.__limit = limit
        self.__dst = dst
        self.__dst.mkdir(exist_ok=True)
        self.__name = f"{self.__class__.__name__}" if name=="" else name
        self.__rmlog(self.__name)
        if split_day:
            self.__name = "{} {}".format(self.__name, datetime.now().strftime("%Y-%m-%d-%a"),)
        self.__logs=[]
        self.__start_time = {}
        
    def __add__(self,obj: MyLogger):
        if not isinstance(obj, MyLogger):raise TypeError
        new = copy(self)
        new.__logs += obj.logs
        return new
    
    def __rmlog(self,name):
        if self.__limit < 1: return
        fs = [f for f in self.__dst.glob(f"*.{name}.log")]
        n = len(fs)
        if n < self.__limit:return
        for i in range(n - self.__limit - 1):
            fs[i].unlink()
    
    @staticmethod
    def __out(filepath, logs):
        with open(filepath, "a") as f:
            [f.write("%s\n" % log) for log in logs]

    def __retry(self, func, *args, **kargs):
        for i in range(self.RETRY_LIMIT):
            try:
                func(*args, **kargs)
            except Exception as e:
                print(e)
                time.sleep(self.DELAY_TIME)
                continue
            else:
                return
        raise RetryCountOverError()
    
    @property  
    def logs(self):
        return self.__logs

    def start(self, id_: str = "main") -> None:
        self.__start_time[id_] = time.time()
        start = f"################# {id_} START######################"
        self.write(start,out=True)

    def end(self, id_: str = "main", sampling=0) -> None:
        end   = f"################## {id_} END #######################"
        self.write(end, out=False)
        processing_time = time.time() - self.__start_time[id_]
        self.write("{} 処理時間は{:5f}sでした。".format(id_, processing_time),out=True)
        if sampling > 0:
            per_time = processing_time / sampling
            self.write("{}個中の1個当たりの処理時間は{:5f}sでした。".format(
                sampling, 
                per_time, 
                out=True
                )
            )

    def write(self, *args: str, debug=True, out=True) -> None:
        data = MyLogData(*args)
        if debug: print(data)
        self.__logs.append(data)
        if out: self.out()
    
    def write_error(self, e: Exception):
        try:
            raise e
        except:
            self.write(traceback.format_exc())

    def out(self):
        logs = self.__logs
        filepath = self.__dst.joinpath(f"{self.__name}.log")
        try:
            self.__retry(self.__out, filepath, logs)
            self.__logs = []
        except RetryCountOverError as e:
            self.__logs.append("リトライ上限を超えました。")
            return
        except Exception as e:
            raise e
        else:
            return
        