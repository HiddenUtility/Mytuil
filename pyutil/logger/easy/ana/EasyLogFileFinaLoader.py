from pathlib import Path
import re





class EasyLogFileFinaLoader:
    """ログファイルを読む"""
    __lines : list[str]
    __rows : list[str]
    __write_num : int
    def __init__(self, log_path : Path) -> None:
        if not log_path.exists():
            raise FileNotFoundError(f'{log_path}は存在しません。')
        self.__src = log_path
        with open(self.__src, 'r') as fs:
            self.__lines = fs.readlines()
        __write_num = 0
        self.__rows = []
        self.__set_write_num()


    
    def __set_write_num(self) -> int:
        """ログの書き込まれた数を数える
        `;`を数えるだけ.
        
        """
        count = 0
        # デフォの最大は10000なので速度的にforでいいや
        row = ''
        for line in self.__lines:
            row += line
            if re.search(';', line):
                count += 1
                row += ';'
                self.__rows.append(row)
        
        self.__write_num = count
    
    @property
    def write_num(self) -> int:
        """ログの書き込まれた数を数える
        `;`を数えるだけ.
        
        """
        return self.__write_num
    
    @property
    def lines(self) -> list[str]:
        return self.__lines
    
    @property
    def rows(self) -> list[str]:
        """log文章の行"""
        return self.__rows
