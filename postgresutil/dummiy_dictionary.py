# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 14:06:14 2023

@author: nanik
"""

import string
import random



class DummiyDictionary:
    @staticmethod
    def random_string(length):
        # アルファベットと数字から成る文字列を作る
        chars = string.ascii_letters + string.digits
        # 指定した長さ分だけランダムに文字を選んで連結する
        return ''.join(random.choice(chars) for _ in range(length))
    @staticmethod
    def random_hex_string(n=32):
        hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                     'a', 'b', 'c', 'd', 'e', 'f']
        hex_string = ''
        for _ in range(n):
          hex_string += random.choice(hex_chars)
        return hex_string
    @classmethod
    def random_dict(cls):
        d = {}
        # idは32文字ののhash
        d['id'] = cls.random_hex_string(32)
        # nameも1から10文字のランダムな文字列とする
        d['name'] = cls.random_string(random.randint(5, 10))
        # ageは10から100までのランダムな整数とするが、strに変換して格納する
        d['age'] = str(random.randint(10, 100))
        # rankは['copper', 'silver', 'gold']のいずれかからランダムに選ぶ
        d['rank'] = random.choice(['copper', 'silver', 'gold'])

        # 辞書を返す
        return d
    
    
if __name__ == "__main__":
    print(DummiyDictionary.random_dict())
    
    