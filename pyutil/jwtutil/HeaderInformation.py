from typing import TypedDict


class HeaderInformation(TypedDict):
    #一般的なヘッダー
    alg: str #署名の際に使用されるアルゴリズム　HS256とか
    typ: str #トークンのタイプ
    cty: str #ペイロードのメディアタイプ
    kid: str #Key ID ユーザープール署名キー、公開鍵とか
