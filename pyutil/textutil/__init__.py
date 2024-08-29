#!/usr/bin/python
# -*- coding: utf-8 -*-
"""pyutil/textutil/__init__.py

Explain : Text操作
          
Create  : 2024-06-06(木): H.U
          
Todo    : 
          
"""


from pyutil.textutil.parser.extractor.TextExtraction import TextExtractionMethod
from pyutil.textutil.parser.extractor.NcCommentOutRemovedText import NcCommentOutRemovedText
from pyutil.textutil.parser.extractor.TextPatternsMutchPolicy import TextPatternsMutchPolicy
from pyutil.textutil.parser.extractor.TextNaturalNumberExtractor import TextNaturalNumberExtractor
from pyutil.textutil.parser.StringParseTrier import StringParseFloatTrier

from pyutil.textutil.datelabel.DataBaseTimestampLabelCreator import DataBaseTimestampLabelCreator
from pyutil.textutil.datelabel.DatetimeLabelCreator import DatetimeLabelCreator
from pyutil.textutil.datelabel.FileTimestampLabelCreator import FileNameTimestampLabelCreator
from pyutil.textutil.datelabel.DateStampLabelCreator import DateStampLabelCreator
from pyutil.textutil.random.RandomStringGenerator import RandomStringGenerator


from pyutil.textutil.fomatter.OnlyLowerAciiAndDigitsTextFomatter import OnlyLowerAciiAndDigitsTextFormatter

__copyright__    = 'Copyright(C) 2024 Hiroki Uchimura'
__version__      = '1000'
__license__      = 'BSD-3-Clause'
__author__       = 'HiddenUtility'
__author_email__ = 'i.will.be.able.to.see.you@gmail.com'
__url__          = 'https://github.com/HiddenUtility/pyutil'
__all__ = [
    # //Text操作
    ## 抽出系
    'TextExtractionMethod',
    'NcCommentOutRemovedText',
    'TextPatternsMutchPolicy',
    'TextNaturalNumberExtractor',
    ## DatetimeLabel
    'DatetimeLabelCreator',
    'DataBaseTimestampLabelCreator',
    'FileNameTimestampLabelCreator',
    'DateStampLabelCreator',
    ## パース
    'StringParseFloatTrier',
    ## ランダム
    'RandomStringGenerator',

    ## フォーマッター
    'OnlyLowerAciiAndDigitsTextFormatter',
]