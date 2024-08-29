from abc import ABC, abstractmethod


class IPaylodAuthorizeRule(ABC):
    @abstractmethod
    def is_ok(self)->bool:
        ...