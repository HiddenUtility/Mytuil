# -*- coding: utf-8 -*-
from pathlib import Path
import json

from pyutil.jsonutil.JsonSaver import JsonSaver


class JsonSerializer:
    """json操作"""
    @staticmethod
    def to_json(filepath: Path, dictionary: dict):
        """辞書をjsonで出力する。"""
        JsonSaver(filepath,dictionary).run()


    def read_json(filepath) -> dict:
        """jsonを読んで辞書にする"""
        with open(filepath, "r") as f:
            dictionary = json.load(f)
        return dictionary
    



