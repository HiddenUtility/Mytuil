#!/usr/bin/python
# -*- coding: utf-8 -*-
"""test_login.py

Explain : FastApiのテストサンプル
          
Create  : 2024-09-12(木): H.U
          
Todo    : 
          
"""


from time import sleep
from fastapi.testclient import TestClient

from fastapi import Response

# 本番はアプリのappを渡してあげてね
from fapiutil import app
from pyutil.hashutil.hash_label_maker import HashLableMaker
client = TestClient(app)


def test_fastapiutil_login():
    """fastaipの認証機能の参考例のテスト例
    - userとパスワードおよび認証機能はサンプル品なので、本番は自分で書き換えてね
    """

    user = 'user'
    faild_secret = 'hoge'
    secret = secret = HashLableMaker.get_security(user, 'password')

    _test_login_faild(user, faild_secret)
    jwt = _test_login(user, secret)
    _test_jwt_login(jwt)

    

def _test_login_faild(user, faild_secret):
    """失敗するかどうか"""
    response : Response = client.get(
        'login',
        params={'user' : user, 'secret' : faild_secret}
        )
    assert response.status_code == 401, f'status_code = {response.status_code}, {response.json()}'

def _test_login(user, secret):
    """userとパスワードでログイン"""
    response : Response = client.get(
        'login',
        params={'user' : user, 'secret' : secret}
        )
    
    assert response.status_code == 200, f'status_code = {response.status_code}, {response.json()}'
    # サンプルはメディアタイプはjson
    data : dict = response.json()
    print(data)

    # jwtが入っているはず
    jwt = data['jwt']
    return jwt

def _test_jwt_login(jwt: str):
    """jwtでlogin"""
    sleep(1) # 早すぎるとjwt更新日時が同じになってしまう

    # 本番のエンドポイントでpostならbodyとか渡してテストしてね
    # ヘッダーにはログイン用のjwtを含める
    response : Response = client.get(
        'login/jwt',
        headers={'Authorization' : jwt}
        )
    
    assert response.status_code == 200, f'status_code = {response.status_code}, {response.json()}'
    # サンプルはメディアタイプはjson
    data : dict = response.json()
    print(data)

    # jwtが更新されているはず
    new_jwt = data['jwt']
    assert jwt != new_jwt

