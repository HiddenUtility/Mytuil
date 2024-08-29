from __future__ import annotations
from typing import override

from pathlib import Path
import pickle
from time import sleep
from pyutil.logger.i_logger import ILogger
from pyutil.myerror.retry_count_over_error import RetryCountOverError
from pyutil.pickleutil import UsingPickle


class EasyCacher(ILogger):
    """簡易的的なキャッシュ"""
    RETRY_LIMIT = 3
    DELAY_TIME = 0.1
    __name: str
    __dst: Path
    __cache_datas: set[str]
    __load_error_clear :bool
    def __init__(self,
                 dst:Path = Path("./cache"), 
                 name="",
                 load_error_clear= True,
                 ):
        """処理履歴をローカルにバイナリ形式で保持することを目的とする。
string集合で管理する。
  
        Args:
            dst (Path, optional): _description_. Defaults to Path("./cache").
            name (str, optional): _description_. Defaults to "".
            load_error_clear (bool, optional): 読み取り失敗時は破損扱いとし削除する. Defaults to True.
        """

        self.__dst = dst
        self.__dst.mkdir(exist_ok=True)
        self.__name = f"{self.__class__.__name__}" if name=="" else name
        self.__cache_path = self.__dst / f"{self.__name}.cache"
        self.__cache_datas = set()
        self.__load_error_clear = load_error_clear
        self.__load()
    
    def __load(self) -> None:
        """ストレージに出力済みの場合それを読み込む。
        """
        if not self.__cache_path.exists():
            return
        try:
            self.__cache_datas = UsingPickle.load(self.__cache_path)
            print(f'{self.__cache_path}読み取りました。')
        except Exception as e:
            if self.__load_error_clear:
                self.__cache_path.unlink(missing_ok=True)
                return
            raise e

    def __out(self) -> None:
        with open(self.__cache_path, "wb") as f:
            pickle.dump(self.__cache_datas, f)

    def __retry(self, func, *args, **kargs):
        for i in range(self.RETRY_LIMIT):
            try:
                func(*args, **kargs)
            except Exception as e:
                print(e)
                sleep(self.DELAY_TIME)
                continue
            else:
                return
        raise RetryCountOverError()
            
    @override
    def write(self, data: str, debug=True, out=True):
        """ログに登録する。

        Args:
            log (str): _description_
            debug (bool, optional): プリントする。__str__を呼ぶのでオリジナルオブジェクトの場合は実装してね。. Defaults to True.
            out (bool, optional): 登録と同時にストレージに出力する。
               ロールバックとか大量に登録するときはFalseにしてあとで out メンバー呼んでください. Defaults to True.
        """
        data = str(data)
        if debug:
            try:
                print(f"{data}を登録します")
            except Exception:
                pass

        self.__cache_datas.add(data)
        if out:
            self.out()

    @override  
    def out(self, debug=False) -> None:
        """ストレージに出力する。
        """
        
        try:
            self.__retry(self.__out)
        except RetryCountOverError as e:
            print("リトライ上限を超えました。")
            return
        except Exception as e:
            raise e
        else:
            if debug: print(f'{self.__cache_path}出力しました。')
            return

    def exists(self, data: str):
        """過去に処理したかどうか

        Args:
            log (str): _description_

        Returns:
            _type_: _description_
        """
        return str(data) in self.__cache_datas
    
    def clear(self) -> None:
        """ログの初期化を行う。
        ストレージに過去ログあった場合も削除する。
        """
        self.__cache_path.unlink(missing_ok=True)
        self.__cache_datas = set()

    def to_strings(self) -> set[str]:
        return self.__cache_datas