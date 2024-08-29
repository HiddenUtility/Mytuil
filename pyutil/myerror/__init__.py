#!/usr/bin/python
# -*- coding: utf-8 -*-
"""__init__.py
Explain : _description_
          
Create  : 2024-06-11(火): H.U
          
Todo    : 
          
"""

from pyutil.myerror.ConvertError import ConvertError
from pyutil.myerror.MyError import MyError
from pyutil.myerror.retry_count_over_error import RetryCountOverError

__copyright__    = 'Copyright(C) 2024 Hiroki Uchimura'
__version__      = '1000'
__license__      = 'BSD-3-Clause'
__author__       = 'HiddenUtility'
__author_email__ = 'i.will.be.able.to.see.you@gmail.com'
__url__          = 'https://github.com/HiddenUtility/pyutil'
__all__ = [
    # //Error
    ## 基底
    'MyError',
    ## カスタムエラー
    'RetryCountOverError',
    'ConvertError',
]