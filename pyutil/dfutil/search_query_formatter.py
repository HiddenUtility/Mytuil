import unicodedata


class SearchQueryTransformer:
    """クエリをワードたちに分解する"""
    def __init__(self, search_query: str):
        self.__query = self.__drop_space(search_query)

    @staticmethod
    def __drop_space(query: str) -> str:
        return unicodedata.normalize('NFKC', query)

    def get_querys(self) -> list[str]:
        return [v for v in self.__query.lower().split(" ") if v != ""]
    
    