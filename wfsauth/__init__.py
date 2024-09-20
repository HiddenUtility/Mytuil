#!/usr/bin/python
# -*- coding: utf-8 -*-
"""__init__.py

Explain : コマンドをつかってWindowsFileServerに認証を通す

### エントリーポイント
from wfsauth import WindFileServerAuthenticator
          
Create  : 2024-05-31(金): H.U
          
Todo    : 
          
"""


from wfsauth.win_file_sever_authenticator import WindFileServerAuthenticator
from wfsauth.error.net_command_error import NetUseCommandCError

__copyright__    = 'Copyright (C) 2024 HiddenUtility'
__version__      = '1000'
__license__      = 'BSD-3-Clause'
__author__       = 'HiddenUtility'
__author_email__ = 'i.will.be.able.to.see.you@gmail.com'
__url__          = 'https://github.com/HiddenUtility/pyutil'

__all__ = [
    "WindFileServerAuthenticator",
    "NetUseCommandCError",
]