
from pathlib import Path
import time
from traceback import print_exc
from pyutil.filetransfer.error.DeleteRetryCountOverError import DeleteRetryCountOverError
from pyutil.filetransfer.error.FileDeleteError import FileDeleteError

class FileSourceDataRemover:
    """ファイルを削除する"""
    
    RETRY_COUNT = 3
    DERAY = 1
    
    def __init__(self, src: Path):
        """ファイルを削除する

        Args:
            src (Path): target path

        Raises:
            TypeError: _description_
        """
        if not isinstance(src, Path):
            raise TypeError()
        self.__src: Path = src

        
    def __retry(self,func, *args, **kwargs):
        for i in range(self.RETRY_COUNT):
            try:
                func(*args, **kwargs)
                return
            except FileDeleteError:
                time.sleep(self.DERAY)
            except Exception as e:
                raise e
        raise DeleteRetryCountOverError(f"{func.__name__} {self.__src}をリトライしましたがうまく実行できました。")
        
    def __remove(self):
        try:
            self.__src.unlink()
        except Exception:
            print_exc()
            raise FileDeleteError(f"{self.__src}の削除に失敗しました。")

    def run(self):
        if not self.__src.exists():
            return
        self.__retry(self.__remove)
