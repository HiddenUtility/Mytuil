#!/usr/bin/python
# -*- coding: utf-8 -*-
"""pyutil/ziputil/__init__.py

Explain : _description_
          
Create  : 2024-06-06(木): H.U
          
Todo    : 
          
"""
from pyutil.ziputil.error.ZiputilError import ZiputilError
from pyutil.ziputil.mono_file_zip_compressor import MonoFileZipCompressor
from pyutil.ziputil.zip_file_information_reader import ZipFileInformationReader
from pyutil.ziputil.easy.EasyZipCompressor import EasyZipCompressor
from pyutil.ziputil.easy.EasyDirectoryCompressor import EasyDirectoryCompressor
from pyutil.ziputil.easy.easy_file_zip_conpressor import EasyFileZipConpressor

__copyright__    = 'Copyright(C) 2024 Hiroki Uchimura'
__version__      = '1000'
__license__      = 'BSD-3-Clause'
__author__       = 'HiddenUtility'
__author_email__ = 'i.will.be.able.to.see.you@gmail.com'
__url__          = 'https://github.com/HiddenUtility/pyutil'
__all__ = [
    # //Zipファイルのあれこれ
    'ZipFileInformationReader',
    'MonoFileZipCompressor',
    'ZiputilError',
    # 簡単シリーズ
    'EasyZipCompressor', # おすすめ
    'EasyFileZipConpressor', 
    'EasyDirectoryCompressor',
]