#!/usr/bin/python
# -*- coding: utf-8 -*-
"""__init__.py

Explain : ファイル移動
          
Create  : 2024-06-06(木): H.U
          
Todo    : 
          
"""
from pyutil.filetransfer.file_data_transfer import FileDataTransfer
from pyutil.filetransfer.file_data_coping import FileDataCoping
from pyutil.filetransfer.failure_file_remover import FailureFileRemover
from pyutil.filetransfer.file_data_remover import FileSourceDataRemover

from pyutil.filetransfer.error.FileTransferError import FileTransferError
from pyutil.filetransfer.error.DestinationUnknownFileError import DestinationUnknownFileError
from pyutil.filetransfer.error.DestinationSameFileExistsError import DestinationSameFileExistsError


__copyright__    = 'Copyright(C) 2024 Hiroki Uchimura'
__version__      = '1000'
__license__      = 'BSD-3-Clause'
__author__       = 'HiddenUtility'
__author_email__ = 'i.will.be.able.to.see.you@gmail.com'
__url__          = 'https://github.com/HiddenUtility/pyutil'

__all__ = [
    # // ファイル転送
    'FileDataTransfer',
    'FailureFileRemover',
    'FileDataCoping',
    'FileSourceDataRemover',
    'FileTransferError',
    'DestinationUnknownFileError',
    'DestinationSameFileExistsError',
    
]