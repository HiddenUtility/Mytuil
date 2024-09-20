import time


class ElapsedTimeMeasurer:
    """指定した時間が経過したか測る"""
    __start_time: float
    __secondes: int
    def __init__(self, secondes: int):
        """指定時間をセットする

        Args:
            secondes (int): 何秒測る？
        """

        self.__start_time = time.time()
        self.__secondes = secondes

    def is_passed(self) -> bool:
        """指定時間が経過したかどうか"""
        elapsed_time  = int(time.time() - self.__start_time)
        return elapsed_time > self.__secondes
    

    def get_passed_time(self) -> float:
        """経過時間を得る"""
        return time.time() - self.__start_time

    def to_integer_label(self) -> str:
        """0詰めで何秒経過したか返す"""
        return f"{self.get_passed_time():03}秒経過しました"

    def to_float_label(self) -> str:
        """小数点3ケタで何秒経過したか返す"""
        return f"{self.get_passed_time():.3f}秒経過しました"

