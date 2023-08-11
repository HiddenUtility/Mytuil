# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 16:33:14 2023

@author: nanik
"""

import random

def get_random_string() -> str:
    #[a-z] ASCII in [97, 122] but i can't remember
    string = "".join(chr(ord("a") + random.randint(0, 25)) for _ in range(4))
    return string


if __name__ == "__main__":
    print(get_random_string())
    