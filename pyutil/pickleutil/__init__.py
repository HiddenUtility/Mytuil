#!/usr/bin/python
# -*- coding: utf-8 -*-
"""__init__.py
Explain : pickle関係
          
Create  : 2024-06-11(火): H.U
          
Todo    : 
          
"""

from pyutil.pickleutil.using_pickle import UsingPickle
from pyutil.pickleutil.error.PickleFileOutputFailureError import PickleFileOutputFailureError
from pyutil.pickleutil.error.PickleFileLoadingFailureError import PickleFileLoadingFailureError
from pyutil.pickleutil.PickleCompressor import PickleCompressor

__copyright__    = 'Copyright(C) 2024 Hiroki Uchimura'
__version__      = '1000'
__license__      = 'BSD-3-Clause'
__author__       = 'HiddenUtility'
__author_email__ = 'i.will.be.able.to.see.you@gmail.com'
__url__          = 'https://github.com/HiddenUtility/pyutil'
__all__ = [
    # // pickle関係
    'UsingPickle',
    'PickleFileOutputFailureError',
    'PickleFileLoadingFailureError',
    'PickleCompressor',
]