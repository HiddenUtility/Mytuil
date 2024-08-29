from pyutil.jwtutil.authorizer.policy.IPaylodAuthorizeRule import IPaylodAuthorizeRule
from pyutil.jwtutil.authorizer.PayloadCreator import PayloadCreator


class PaylodAuthorizeCustomDataSameRule(IPaylodAuthorizeRule):
    """その他データ一致するかどうか
    """
    ENCODE = PayloadCreator.ENCODE
    __client_payload : dict[str, str]
    __master_payload : dict[str, str]
    def __init__(self,
                client_payload : dict[str, str],
                master_payload : dict[str, str],
                ) -> None:
        self.__client_payload = client_payload
        self.__master_payload = master_payload

    def is_ok(self) -> bool:
        """typeあっている"""
        for k, v in self.__master_payload.items():
            try:
                client_value = self.__client_payload[k]
            except:
                return False
            if v != client_value:
                return False
        return True