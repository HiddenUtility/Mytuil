from __future__ import annotations
from pyutil.logger.simple.simple_log_data import SimpleLogData
from pyutil.logger.i_logger import ILogger
import time
import traceback
from copy import copy
from datetime import datetime
from pathlib import Path


class SimpleLogger(ILogger):
    __name: str
    __dst: Path
    __logs: list[SimpleLogData]
    __start_time : dict[str, float]
    def __init__(self,
                 dst:Path = Path("./log"),
                 name="",
                 split_day=True,
                 limit=5
                 ):
        """

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

    def __add__(self,obj: SimpleLogger):
        if not isinstance(obj, SimpleLogger):raise TypeError
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

    @property
    def logs(self):
        return self.__logs

    def start(self, id_: str = "main") -> None:
        self.__start_time[id_] = time.time()
        start = f"################# {id_} START######################"
        self.write(start,out=True)

    def end(self, id_: str = "main") -> None:
        end   = f"################## {id_} END #######################"
        self.write(end)
        self.write("{} 処理時間は{:5f}sでした。".format(id_,time.time() - self.__start_time[id_]),out=True)

    def write(self, *args: str, debug=True, out=True) -> None:
        data = SimpleLogData(*args)
        if debug: print(data)
        self.__logs.append(data)
        if out: self.out()

    def error(self, e: Exception):
        try:
            raise e
        except:
            self.write(traceback.format_exc())

    def out(self):
        logs = sorted(self.__logs)
        filepath = self.__dst.joinpath(f"{self.__name}.log")
        try:
            with open(filepath, "a") as f:
                [f.write("%s\n" % log) for log in logs]
            self.__logs = []
        except:
            pass