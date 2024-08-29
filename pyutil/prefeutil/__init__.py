#!/usr/bin/python
# -*- coding: utf-8 -*-
"""__init__.py
Explain : よく使う設定ファイルフォーマットひな形
          
Create  : 2024-06-11(火): H.U
          
Todo    : 
          
"""

from pyutil.prefeutil.json.db.DataBasePreferencesJsonFileSerializer import DataBasePreferencesJsonFileSerializer
from pyutil.prefeutil.xml.MultiProcessProgramPreferencesXmlFileSerializer import MultiProcessProgramPreferencesXmlFileSerializer
from pyutil.prefeutil.xml.FileControllePreferencesXmlFileSerializer import FileControllerPreferencesXmlFileSerializer


__copyright__    = 'Copyright(C) 2024 Hiroki Uchimura'
__version__      = '1000'
__license__      = 'BSD-3-Clause'
__author__       = 'HiddenUtility'
__author_email__ = 'i.will.be.able.to.see.you@gmail.com'
__url__          = 'https://github.com/HiddenUtility/pyutil'
__all__ = [
    # // Settingファイル読み込み
    'DataBasePreferencesJsonFileSerializer',
    'MultiProcessProgramPreferencesXmlFileSerializer',
    'FileControllerPreferencesXmlFileSerializer',

]