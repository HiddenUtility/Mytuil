# -*- coding: utf-8 -*-
from pathlib import Path
import json

from pyutil.jsonutil.JsonSaver import JsonDataSaver


class JsonSerializer:
    """json操作"""
    @staticmethod
    def to_json(filepath: Path, dictionary: dict):
        """辞書をjsonで出力する。
        セーバーを使うので，保存中は適当な拡張子になるので安心してね
        """
        JsonDataSaver(filepath,dictionary).run()

    @staticmethod
    def read_json(filepath) -> dict:
        """jsonを読んで辞書にする"""
        with open(filepath, "r") as f:
            dictionary = json.load(f)
        return dictionary
    



