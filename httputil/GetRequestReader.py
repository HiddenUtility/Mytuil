from urllib.parse import ParseResult, parse_qs, urlparse


class GetRequestReader:
    __url : ParseResult
    __path : str
    __query : str
    def __init__(self, url : str) -> None:
        self.__url = urlparse(url)
        self.__path = self.__url.path
        self.__query = self.__url.query

    def __str__(self) -> str:
        return f'path = {self.path} \n {self.to_dict()}'

    @property
    def path(self):
        return self.__path

    def to_dict(self):
        if self.__query == '':
            return {}
        data = parse_qs(self.__query)
        return {k : v[0] for k, v in data.items()}