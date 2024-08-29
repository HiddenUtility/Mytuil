#!/usr/bin/python
# -*- coding: utf-8 -*-
"""easy_logger.py

Explain : 簡易ログ
          
Create  : 2024-06-21(金): H.U
          
Todo    : 
          
"""

from __future__ import annotations
from typing import Literal, overload
from pathlib import Path
import time
from traceback import format_exception
from pyutil.pathuil.directory_creator import DirecotryCreator


from pyutil.logger.log_data import LogLevel
from pyutil.logger.i_logger import ILogger
from pyutil.logger.easy.EasyLogPathCreator import EasyLogPathCreator
from pyutil.logger.easy.EasyLoggerReport import EasyLoggerReport
from pyutil.logger.easy.EasyNextLogPathCreator import EasyNextLogPathCreator
from pyutil.logger.easy.OldLogRemover import OldLogRemover
from pyutil.logger.easy.EasyLogData import EasyLogData

from pyutil.myerror.retry_count_over_error import RetryCountOverError 


class EasyLogger(ILogger):
    """簡易ログ"""
    LogLevel = LogLevel
    RETRY_LIMIT = 3
    DELAY_TIME = 0.1
    __base_name : str
    __dest: Path
    __log_datas: list[EasyLogData]
    __start_time_map : dict[str, float]
    __max_write_num : int
    __now_write_num : int
    __max_file_num : int
    def __init__(self,
                 dest:Path = Path("../log"), 
                 name="", 
                 mkdir: bool = True,
                 max_file_num=10,
                 max_write_num = 10000,
                 ):
        """簡易的にログを取る
        基本的には追記していく

        Args:
            dest (Path, optional): 出力先を指定. Defaults to Path("../log").
            name (str, optional): ログに任意の名前を付けることができる.排他処理入れるとmultiproressでバグるので入れてない。衝突しそうなときは名前分けて使ってね。 Defaults to "".
            max_file_num (int, optional): ログのファイル数.日付を分けるて出力先した場合の最大値数を設定する。超えたらインスタンス時に消す。 Defaults to 10.
            max_row_num (int, optional): ログのファイルの最大write数。 Defaults to 10000.
            mkdir (bool, optional): 出力先が無ければディレクトを生成する. Defaults to True.
        """
        self.__max_file_num = max_file_num
        self.__max_write_num = max_write_num
        self.__dest = dest
        if mkdir: 
            DirecotryCreator(dest)
        self.__log_datas=[]
        self.__start_time_map = {}
        self.__base_name = f"{self.__class__.__name__}" if name=="" else name
        OldLogRemover(self.__dest, self.__base_name, self.__max_file_num)
        
        creator = EasyLogPathCreator(self.__dest, self.__base_name)
        self.__logpath = creator.path
        self.__now_write_num = creator.write_num

        

    @staticmethod
    def __out_file(filepath, logs):
        with open(filepath, "a") as f:
            [f.write("%s\n" % log) for log in logs]

    def __retry(self, func, *args, **kargs):
        for i in range(self.RETRY_LIMIT):
            try:
                func(*args, **kargs)
            except Exception as e:
                print(e)
                time.sleep(self.DELAY_TIME)
                continue
            else:
                return
        raise RetryCountOverError()
    

    def __out(self):
        logs = self.__log_datas.copy()
        
        try:
            self.__retry(self.__out_file, self.__logpath, logs)
        except RetryCountOverError as e:
            self.__log_datas.append("リトライ上限を超えました。")
            return
        except Exception as e:
            raise e
        else:
            self.__log_datas = []

        
            

    def start(self, id_: str = "main") -> None:
        """簡易的なストップウォッチのスタート

        Args:
            id_ (str, optional): _description_. Defaults to "main".
        """
        self.__start_time_map[id_] = time.time()
        start = f"################# {id_} START######################"
        self.write(start,out=True)


    def end(self, id_: str = "main", sampling : int = 0) -> None:
        """簡易的なストップウォッチのエンド
        処理時間は現在時刻で初期化されるため、もう一度呼ぶとラップタイムになる
        Args:
            id_ (str, optional): _description_. Defaults to "main".
            sampling (int, optional): _description_. Defaults to 0.
        """
        if not isinstance(sampling, int):
            raise TypeError(f'samplingは{type(sampling)}です。intオブジェクトではありません。')
        
        if id_ not in self.__start_time_map:
            raise NotImplementedError(f'id:{id_}はスタートが切られていません。')
        end   = f"################## {id_} END #######################"
        self.write(end, out=False)
        processing_time = time.time() - self.__start_time_map[id_]
        self.__start_time_map[id_] = time.time()
        self.write("{} 処理時間は{:5f}sでした。".format(id_, processing_time),out=True)
        if sampling > 0:
            per_time = processing_time / sampling
            self.write("{}個中の1個当たりの処理時間は{:5f}sでした。".format(
                sampling, 
                per_time, 
                out=True
                )
            )

    @overload
    def write(self, *args: str,
               debug=True, 
               out=True, 
               level : LogLevel=LogLevel.info,
               ) -> None:
       """ログに追加
        Args:
            *args (str)
            debug (bool, optional): printするかどうか. Defaults to True.
            out (bool, optional): ファイルとして出力する。. Defaults to True.
            level (loglevel): ログレベル. Defaults to 'info'.

        """
    
    @overload
    def write(self, *args: str,
               debug=True, 
               out=True, 
               level :Literal['info',
                              'error',
                              'crit',
                              'alert',
                              'warn',
                              'notice',
                              'debug',
                              ] = 'info',
               ) -> None:
       """ログに追加
        Args:
            *args (str)
            debug (bool, optional): printするかどうか. Defaults to True.
            out (bool, optional): ファイルとして出力する。. Defaults to True.
            level (loglevel): ログレベル. Defaults to 'info'.
                {
                    emerg : 実行不可能なエラー
                    alert : 即時対応が必要
                    crit : #致命的なエラー
                    error : 一般エラー
                    warn : 警告
                    notice : 注意
                    info  : 一般
                    debug  : デバック
                }
        """


    def write(self, *args: str,
               debug=True, 
               out=True, 
               level='info',
               ) -> None:
        """ログに追加
        Args:
            *args (str)
            debug (bool, optional): printするかどうか. Defaults to True.
            out (bool, optional): ファイルとして出力する。. Defaults to True.
            level (loglevel): ログレベル. Defaults to 'info'.
                {
                    emerg : 実行不可能なエラー
                    alert : 即時対応が必要
                    crit : #致命的なエラー
                    error : 一般エラー
                    warn : 警告
                    notice : 注意
                    info  : 一般
                    debug  : デバック
                }
        """
        if not isinstance(level, LogLevel):
            level = LogLevel[level]

        if self.__now_write_num > self.__max_write_num:
            self.__logpath = EasyNextLogPathCreator(self.__logpath).path
            self.__now_write_num = 0
        
        data = EasyLogData(*args, level=level)
        self.__log_datas.append(data)
        self.__now_write_num += 1

        if out: self.out()
        if debug: print(data)
    
    def error_stack_trace(self, 
                    e: Exception,
                    debug=True,
                    out=True,
                    level :Literal[
                        'error',
                        'crit',
                        'alert',
                        'emerg',
                        ] | LogLevel= 'error',
                    ) -> None:
        """エラートラックを書き込み

        Args:
            e (Exception): キャッチしたエラー
            debug (bool, optional): printするかどうか. Defaults to True.
            out (bool, optional): ファイルとして出力する。. Defaults to True.
            level (
                Literal[
                    emerg : 実行不可能なエラー
                    alert : 即時対応が必要
                    crit : 致命的なエラー
                    error : 一般エラー
                ], optional): _description_. Defaults to 'error'.
        """
        self.write(*format_exception(e), debug=debug, out=out,level=level)

    def info(self, *args: str,
               debug=True, 
               out=True, 
               ) -> None:
        """一般レベルで書き込み

        Args:
            debug (bool, optional): printするかどうか. Defaults to True.
            out (bool, optional): ファイルとして出力する。. Defaults to True.
        """
        self.write(*args, debug=debug, out=out,level=LogLevel.info)

    def warn(self, *args: str,
               debug=True, 
               out=True, 
               ) -> None:
        """警告を書き込み

        Args:
            debug (bool, optional): printするかどうか. Defaults to True.
            out (bool, optional): ファイルとして出力する。. Defaults to True.
        """
        self.write(*args, debug=debug, out=out,level=LogLevel.warn)
        
    def error(self, *args: str,
               debug=True, 
               out=True, 
               ) -> None:
        """一般エラーを書き込み

        Args:
            debug (bool, optional): printするかどうか. Defaults to True.
            out (bool, optional): ファイルとして出力する。. Defaults to True.
        """
        self.write(*args, debug=debug, out=out,level=LogLevel.error)


        
    def out(self):
        """メモリキャッシュをファイル出力する

        排他入れるとバグったのでいれてない。
        """
        
        try:
            self.__out()
        finally:
            pass

    def to_report(self) -> EasyLoggerReport:
        """ログの解析結果を返す

        Returns:
            EasyLoggerReport: [ログの解析結果]
        """
        return EasyLoggerReport(self.__dest)


