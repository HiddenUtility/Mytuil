from pyutil.jwtutil.authorizer.PayloadCreator import PayloadCreator
from pyutil.jwtutil.authorizer.policy.IPaylodAuthorizeRule import IPaylodAuthorizeRule
from pyutil.jwtutil.authorizer.policy.PaylodAuthorizeCustomDataSameRule import PaylodAuthorizeCustomDataSameRule
from pyutil.jwtutil.authorizer.policy.PaylodAuthorizeEncodingRule import PaylodAuthorizeEncodingRule
from pyutil.jwtutil.authorizer.policy.PaylodAuthorizeExpityRule import PaylodAuthorizeExpityRule


class PaylodAuthorizePolicy(IPaylodAuthorizeRule):
    """Palyloadが問題ないか

    有効期限とエンコードはチェックする
    """
    ENCODE = PayloadCreator.ENCODE
    __client_payload : dict[str, str]
    __master_payload : dict[str, str]
    __timezone : str

    def __init__(self,
                client_payload : dict[str, str],
                master_payload : dict[str, str],
                timezone: str = 'Asia/Tokyo',
                ) -> None:
        """Payloadが問題ないかチェックする

        Args:
            client_payload (dict[str, str]): _description_
            master_payload (dict[str, str]): _description_
        """
        self.__client_payload = client_payload
        self.__master_payload = master_payload
        self.__timezone = timezone


    def is_ok(self) -> bool:
        if not PaylodAuthorizeExpityRule(self.__client_payload, self.__timezone).is_ok():
            return False
        if not PaylodAuthorizeEncodingRule(self.__client_payload).is_ok():
            return False
        if not PaylodAuthorizeCustomDataSameRule(self.__client_payload, self.__master_payload).is_ok():
            return False
        return True