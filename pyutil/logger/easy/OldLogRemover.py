from pathlib import Path

from pyutil.logger.easy.OldLogPathCollector import OldLogPathCollector


class OldLogRemover:
    """たまりすぎたログファイルを消す"""
    __target: Path
    __name : str
    __max_file_num :int
    def __init__(self,
                    target: Path,
                    base_name: str,
                    max_file_num :int
                    ) -> None:
        """たまりすぎたログファイルを消す

        Args:
            target (Path): ログが出力されているところ
            base_name (_type_): ベース名
            max_file_num (int): 最大数
        """
        self.__target = target
        self.__name = base_name
        self.__max_file_num = max_file_num
        if self.__max_file_num < 1: raise ValueError(f'max_file_num={self.__max_file_num}は0以下に設定できません。')
        self.__run()

    def __run(self):
        collector = OldLogPathCollector(self.__target, self.__name)
        fs = collector.get_log_paths()
        if collector.exists():
            return
        
        if len(fs) < self.__max_file_num:return
        for i in range(len(fs) - self.__max_file_num - 1):
            fs[i].unlink(missing_ok=True)
