
from pyutil.lightautho.LightAuthorizeError import LightAuthorizeError
from pyutil.jwtutil.authorizer.JwtAuthoriizer import MyJwtAuthorizer
from pyutil.lightautho.LightUsersTableColumnName import LightUsersTableColumnName



class LightLakeAutholizer:
    """ユーザー名とパスワードで認証処理を行う簡単なオーソライザー
    - 内部の秘密鍵がインスタンスすると変わってしまうため，利用者はこのオブジェクトを保持する

    """
    __authorizer : MyJwtAuthorizer
    __user_datas : dict[str, str]
    
    def __init__(self,user_datas :dict[str, str]= {}):
        """ユーザー名とパスワードで認証処理を行う簡単なオーソライザー
        """
        self.__user_datas = user_datas
        self.__authorizer = MyJwtAuthorizer().set_random_secret()




    def login(self, client_name: str, client_secret: str) -> str:
        """ログインする。成功すればjwtを発行する 

        Args:
            client_name (str): ログインユーザー名
            client_secret (str): ログインパスワード

        Raises:
            DataLakeAuthorizeError: 失敗

        Returns:
            str: jwt
        """

        if self.__user_datas.get(client_name) != client_secret:
            raise LightAuthorizeError('usernameまたはpasswordが間違っています。')

        return self.__authorizer.get_jwt(
            add_data={
                LightUsersTableColumnName.username.name : client_name,
                }
        )


    def login_from_jwt(self, token: str) -> str:
        """jwtでユーザー認証する

        Args:
            token (str): jwt

        Returns:
            str: 有効期限を更新したjwtを再発行する。
        """
        try:
            payload = self.__authorizer.read_jwt(token)
        except Exception:
            raise LightAuthorizeError('jwdのエンコードに失敗しました。')
            
        client_name = payload[LightUsersTableColumnName.username.name]
        if self.__user_datas.get(client_name) is None:
            raise LightAuthorizeError('usernameまたはpasswordが間違っています。')

        if not self.__authorizer.is_ok(token, add_data={LightUsersTableColumnName.username.name : client_name}):
            raise LightAuthorizeError('jwt認証失敗')
        
        return self.__authorizer.get_jwt(
            add_data={
                LightUsersTableColumnName.username.name : client_name,
                }
        )

    