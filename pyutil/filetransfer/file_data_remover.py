
from pathlib import Path
import time
from traceback import print_exc
from pyutil.filetransfer.DeleteRetryCountOverError import DeleteRetryCountOverError
from pyutil.filetransfer.FileDeleteError import FileDeleteError

class FileSourceDataRemover:
    
    RETRY_COUNT = 3
    DERAY = 1
    
    def __init__(self, src: Path):
        if not isinstance(src, Path):
            raise TypeError()
        if not src.exists():
            raise FileNotFoundError()
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
        self.__retry(self.__remove)
