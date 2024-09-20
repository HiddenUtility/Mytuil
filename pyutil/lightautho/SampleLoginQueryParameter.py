from pydantic import BaseModel


class SampleLoginQueryParameterModel(BaseModel):
    """クエリパラメータ格納用の構造体
    - BalseModelはパブリックなメンバなため書き換えできてしまう
    - 書く量は少ないため、やるならクラス内のプライベートメンバに使いたい
    """
    user: str
    secret: str


class SampleLoginQueryParameter:
    """クエリパラメータ格納用の構造体
    - 自由に改造してOK
    """
    __user: str
    __secret: str
    def __init__(self, user: str, secret: str) -> None:
        """ログイン用の情報

        Args:
            user (str): _description_
            secret (str): _description_
        """
        self.__user = user
        self.__secret = secret
    
    @property
    def user(self) -> str:
        return self.__user
    
    @property
    def secret(self) -> str:
        return self.__secret