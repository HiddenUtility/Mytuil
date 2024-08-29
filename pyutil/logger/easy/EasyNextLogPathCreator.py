from pyutil.logger.easy.EasyNextLogNameCoreator import EasyNextLogNameCoreator
from pathlib import Path

class EasyNextLogPathCreator:
    """行いっぱいになったあとのログのパスを得る
    <なまえ> [num]をふやすスタイルでいくか
    """
    def __init__(self, now_path : Path) -> None:
        self.__dest = now_path.parent
        self.__next_name = EasyNextLogNameCoreator(now_path.stem).name

    @property
    def path(self) -> Path:
        return self.__dest / self.__next_name
    