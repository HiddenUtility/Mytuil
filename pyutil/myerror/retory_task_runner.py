from pyutil.myerror.retry_count_over_error import RetryCountOverError
from time import sleep
from traceback import format_exc

class RetryTask:
    RETRY_COUNT = 3
    DERAY = 0.1
    THROW_ERORR = RetryCountOverError("リトライの上限に達しました。")
    __retry_count_limit:int
    __deray_time:float
    __error_logs: list[str]
    __ignore: bool
    def __init__(self,
                 retry_count_limit:int = RETRY_COUNT,
                 deray_time:float = DERAY,
                 throw_error_class: Exception = THROW_ERORR,
                 igunore=False,
                 ) -> None:
        if not isinstance(throw_error_class, Exception): raise TypeError()
        self.__error_logs = []
        self.__retry_count_limit = retry_count_limit
        self.__deray_time = deray_time
        self.__throw_error_class = throw_error_class
        self.__ignore = igunore

    def retry(self,func, *args, **kwargs) -> list[str]:
        for _ in range(self.__retry_count_limit):
            try:
                func(*args, **kwargs)
                return
            except Exception as e:
                self.__error_logs.append(format_exc())
                sleep(self.__deray_time)
        if self.__ignore:
            [print(e) for e in self.__error_logs]
            print(self.__throw_error_class)
        raise self.__throw_error_class
    
    def get_error_logs(self) -> list[str]:
        return self.__error_logs
    
    def is_ok(self) -> bool:
        return not self.__error_logs
    