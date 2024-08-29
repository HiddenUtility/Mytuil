from typing import TypedDict, Required


class PayLoadDictionary(TypedDict):
    """予約済みクレーム"""
    iss : str #JWTを発行した者(サーバー)の識別子
    sub : str #JWTの主体となる識別子
    aud : str #JWTを利用する側(クライアント)の識別子
    exp : Required[str] #有効期限の終了日時
    nbf : str #有効期限の開始日時
    iat : str #発行日時
    jti : str #識別子
    typ : Required[str] #コンテンツタイプの宣言


