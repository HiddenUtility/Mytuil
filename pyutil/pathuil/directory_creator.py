#!/usr/bin/python
# -*- coding: utf-8 -*-
"""directory_creator.py

Explain : 親がいなければ再回帰的に作成する。
          
Create  : 2024-06-11(火): H.U
          
Todo    : 
          
"""
import shutil

from pathlib import Path


class DirectoryCreator:
    """再回帰的にディレクトリを作る
    mkdir
    """
    def __init__(self, path: str | Path, clear=False) -> None:
        """ディレクトリを作る

        Args:
            path (str | Path): 対象。親がいなければ再回帰的に作成する。
            clear (bool, optional): ディレクトリを作る前に存在していたら削除する. Defaults to False.
        """
        if clear:
            return self.clear_dir(path)
        self.mkdir(path)


    @classmethod
    def mkdir(cls, path: str | Path):

        """ディレクトリを作る
        親がいなければ再回帰的に作成する。

        Args:
            path (str | Path): 対象

        Raises:
            Exception: 作ることができなかった場合
        """
        path = Path(path)
        try:
            if not path.parent.exists():
                cls.mkdir(path.parent)
        except Exception as e:
            raise Exception(f"{e}\n{path}は作ることはできません。")
        path.mkdir(exist_ok=True)

    @classmethod
    def clear_dir(cls, path: str | Path):
        """ディレクトリを作る前に存在していたら削除する
        Args:
            path (str | Path): 対象
        """
        path = Path(path)
        if path.exists():
            shutil.rmtree(path, ignore_errors=True)
        cls.mkdir(path)


