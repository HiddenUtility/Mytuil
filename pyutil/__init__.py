#!/usr/bin/python
# -*- coding: utf-8 -*-
"""__init__.py

Explain : よく使うやつのまとめ。基本骨格など
          
Create  : 2024-06-11(火): H.U
          
Todo    : 
          
"""

# // 時間系
from pyutil.timeutil import *
# // List操作系
from pyutil.listutil import *


# // ドライバ系
from pyutil.driveutil import *

# // ロガー各種
from pyutil.logger import *

# // pickleutil
from pyutil.pickleutil import *
# // FileD転送系
from pyutil.filetransfer import *
# // JsonWebToken
from pyutil.jwtutil import *


# // Error
from pyutil.myerror import *
# // json操作系
from pyutil.jsonutil import *
#// uisngzip
from pyutil.ziputil import *
# // hash値のあれこれ
from pyutil.hashutil import *
# // uri
from pyutil.urlutil import *
# // Settingファイル読み込み
from pyutil.prefeutil import *
# // xml操作
from pyutil.xmlutil import *
# // パス関係
from pyutil.pathuil import *
# // Text操作系
from pyutil.textutil import *
# // 構造体シリーズ
from pyutil.structure import *

# // Dummiy
from pyutil.dummy import *

# // DataFrame操作
from pyutil.dfutil import *

__copyright__    = 'Copyright (C) 2024 HiddenUtility'
__version__      = '1000'
__license__      = 'BSD-3-Clause'
__author__       = 'HiddenUtility'
__author_email__ = 'i.will.be.able.to.see.you@gmail.com'
__url__          = 'https://github.com/HiddenUtility/pyutil'

__all__ = [

    # 時間系
    ## タイマー系
    'MyTimer',
    'LoopTimer',
    'ElapsedTimeMeasurer',
    ## ファイル
    'FileTimestampUpdater',
    ## 比較
    'XdayDateTimePassingFromReferenceTimePolicy',
    'XTimePassingFromReferenceTimePolicy',

    # // ファイル転送
    'FileDataTransfer',
    'FailureFileRemover',
    'FileDataCoping',
    'FileSourceDataRemover',
    'FileTransferError',
    'DestinationUnknownFileError',
    'DestinationSameFileExistsError',


    # // List操作系
    'AdvanceListSpliter',
    
    # //DataFrame操作
    'DataFrameFormatter',
    'DataFrameSearcher',

    
    # /ドライバ系
    'DriveName',
    'DriveResearcher',
 

    # // pickle関係
    'UsingPickle',
    'PickleCompressor',
    'PickleFileOutputFailureError',
    'PickleFileLoadingFailureError',
    


    # // ロガー各種
    'ILogger',
    'EasyLogger',
    'SimpleLogger',
    'EasyCacher',
    'LogLevel',

    # jwt操作系
    'MyJsonWebToken',
    'MyJwtAuthorizer',
    'PayLoadDictionary',


    # //Error
    ## 基底
    'MyError',
    ## カスタムエラー
    'RetryCountOverError',
    'ConvertError',


    # // json操作
    'JsonSerializer',
    'SingleValueJsonSerializer',
    'SingleDictionaryJsonSerializer',

    # //Zipファイルのあれこれ
    'ZipFileInformationReader',
    'MonoFileZipCompressor',
    'ZiputilError',
    # 簡単シリーズ
    'EasyFileZipConpressor', 
    'EasyDirectoryCompressor',
    'EasyZipCompressor',


    # // hash値のあれこれ
    'ZipFileHashCheacker',
    'FileHashCheacker',
    'HashLableMaker',
    'JsonHashCreator',
    'JsonBase64HashSerializer',
    
    # // URI操作
    'UrlUtility',
    # // よく使うSettingファイル読み込みフォーマット
    'DataBasePreferencesJsonFileSerializer',
    'MultiProcessProgramPreferencesXmlFileSerializer',
    'FileControllerPreferencesXmlFileSerializer',
    # xmlにまつわるあれこれ
    'XmlUtility',

    # //Path関係
    ## パスストリーム
    'FilepathStream',
    ## 作成
    'DirectoryCreator',
    'WindowsAvailablePathName',
    'CrearTestDirectoryPreparator',
    'PycacheRemover',
    ## /再回帰系
    'DirectoryTreeCopier',
    'ToInsideDirectoryTreeCopier',
    'DirectoryTreeRemover',
    'TargetDirectoryOnlyCopier',

    
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
    ## パース
    'StringParseFloatTrier',
    ## ランダム
    'RandomStringGenerator',
    ## フォーマッター
    'OnlyLowerAciiAndDigitsTextFormatter',


    # //構造体シリーズ
    'PoolResultTypeDefinition',

    # // Dummiy
    ## ダミーファイル作り
    'DummyDatetimeLabelFileMaker',
    
    ]