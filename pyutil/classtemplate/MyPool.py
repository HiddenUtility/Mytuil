#!/usr/bin/python
# -*- coding: utf-8 -*-
"""MyPool.py

Explain : Poolのテンプレ
          
Create  : 2024-09-13(金): H.U
          
Todo    : 
          
"""


from multiprocessing import Pool
from typing import Iterable

from tqdm import tqdm
from pyutil.logger.easy.easy_logger import EasyLogger
from pyutil.structure.PoolResultTypeDefinition import PoolResultTypeDefinition


class MyPool:
    __logger : EasyLogger


    def _process(self, *args) -> PoolResultTypeDefinition:
        """処理

        Returns:
            PoolResultTypeDefinition: _description_
        """

        result = PoolResultTypeDefinition()
        try:
            # ////////////////処理//////////////////////
            ...

        except Exception as e:
            result = result.write_error_stack_trace(e)
        return result

    def __multi_run(self):
        # ////////////////リアルデータ//////////////////////
        iterable : Iterable = []

        with Pool() as pool:
            ite = pool.imap(self._process, iterable)
            tq = tqdm(iterable)
            while True:
                try:
                    tq.update()
                    # タイムアウトいれるならここ
                    result = ite.next()
                    if result.is_error():
                        self.__logger.error(result.error)
                except StopIteration:
                    break
                except Exception as e:
                    raise e
        

    def run(self):
        """実行
        """
        self.__logger.start()
        try:
            self.__multi_run()
        except Exception as e:
            self.__logger.error_stack_trace(e)
        finally:
            self.__logger.end()

