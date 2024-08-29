from pyutil.logger.easy.OldLogPathCollector import OldLogPathCollector
from pyutil.logger.easy.EasyLogFileFinalWriteNumber import EasyLogFileFinalWriteNumber, EasyLogFileFinalWriteNumberError
from pyutil.logger.easy.EasyNextLogNameCoreator import EasyNextLogNameCoreator

from datetime import datetime
from pathlib import Path


class EasyLogPathCreator:
    """ログのパスを得る"""
    __dest : Path
    __collector : OldLogPathCollector
    __write_num : int
    __log_name:str
    
    def __init__(self, dest: Path, base_name : str) -> None:
        """_summary_

        Args:
            dest (Path): ログの出力先
            base_name (str): 純粋なベースの名前
        """
        
        self.__dest = dest
        self.__write_num = 0
        self.__collector = OldLogPathCollector(dest, base_name)

        date_name = '{} {}'.format(base_name, datetime.now().strftime(r"%Y-%m-%d-%a"))
        self.__log_name = EasyNextLogNameCoreator(date_name).name

        if not self.__collector.exists():
            return
        
        last_path = self.__collector.get_final_log_path()
        if  self.__log_name == last_path.name:
            self.__set_old_write_num(last_path)


    def __set_old_write_num(self, last_path :Path):
        """最終行を調べる
        オープンに失敗したら消す?
        """
        try:
            self.__write_num = EasyLogFileFinalWriteNumber(last_path).value
        except EasyLogFileFinalWriteNumberError:
            self.path.unlink(missing_ok=True)
            print(f'{last_path}のオープンに失敗したため削除します。')
        except Exception as e:
            raise e

    @property
    def write_num(self) -> int:
        return self.__write_num

    @property
    def path(self) -> Path:
        return self.__dest / self.__log_name