#!/usr/bin/python
# -*- coding: utf-8 -*-
"""build_tool.py

Explain : Mainモジュール
          
Create  : 2024-06-12(水): H.U
          
Todo    : 
          
"""

from shutil import copy
from pyutil import DirectoryTreeCopier, DirectoryCreator
from pyutil import EasyLogger

from buildtool.configration.setting_loader import SettingLoader
from buildtool.configration.IgunoreDirecotryName import IgunoreDirecotryName
from buildtool.configration.BuildProject import BuildProject


class BuildTool:
    """リリース用にファイルを整理する"""
    __logger : EasyLogger
    __loader : SettingLoader
    def __init__(self) -> None:
        self.__loader = SettingLoader()
        self.__logger = EasyLogger(self.__loader.log_path, name=f'{self.__class__.__name__}')

    def __build(self, pjt : BuildProject):
        self.__logger.write(pjt)
        DirectoryCreator(pjt.dest_path, clear=True)
        for dirpath in pjt.dirpaths:
            DirectoryTreeCopier(
                dirpath,
                pjt.dest_path,
                ignore_dirname_patterns=IgunoreDirecotryName.VALUE + pjt.ignore_dirname,
                ignore_filename_patterns=pjt.ignore_filename,
                clear=True,
                ).run()
        for filepath in pjt.filepaths:
            copy(filepath, pjt.dest_path / filepath.name)

    def run(self, clear = True):
        """ビルド開始

        Args:
            clear (bool, optional): 出力先を初期化する. Defaults to True.
        """
        self.__logger.start()
        if clear:
            self.__loader.clear_dest()
        try:
            for pjt in self.__loader.to_pjts():
                self.__build(pjt)
        except Exception as e:
            self.__logger.error_stack_trace(e)
        self.__logger.end()

