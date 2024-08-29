#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

Explain : UIR操作まとめ
          
Create  : 2024-06-06(木): H.U
          
Todo    : 
          
"""

from __future__ import annotations
from urllib.parse import urljoin, urlparse, urlencode, ParseResult, parse_qs


class UrlUtility:
    """UIR操作まとめ"""
    __url : str
    __root : str
    __path : str
    __query : dict[str, str]
    def __init__(self,
                 root : str = 'http://localhost:80',
                 path : str='',
                 query : str | dict[str, str]={},
                 ) -> None:
        self.__root = root
        self.__path = path
        self.__query =  self.__parce_query(query)
        self.__url = self.__anparse()

    def set_url(self, url:str) -> UrlUtility:
        """フルのurlを読み取る

        Args:
            url (str): フルのurl

        Returns:
            UrlUtility: new
        """
        pr : ParseResult = urlparse(url)
        return UrlUtility(
            f'{pr.scheme}://{pr.netloc}',
            pr.path,
            pr.query,
        )
    
    def __parce_query(self, query : str | dict[str, str]) -> dict[str, str]:
        if isinstance(query, str):
            query = parse_qs(query)
        if not isinstance(query, dict):
            raise TypeError(f'queryは{type(query)}です。strかdictオブジェクトではありません。')
        return query
    
    def __str__(self) -> str:
        return f'''
root : {self.__root}
endopoint : {self.__path}
query : {urlencode(self.__query)}
'''

    def __anparse(self):
        if not self.__query:
            # joinは第二が空文字もで問題ない
            return urljoin(self.__root, self.__path)
        if self.__query:
            return urljoin(self.__root, f'{self.__path}?{urlencode(self.__query)}')


    @property
    def url(self) -> str:
        return self.__url

    @property
    def root(self) -> str:
        """http://host:portまで"""
        return self.__root

    @property
    def path(self) -> str:
        return self.__path

    @property
    def query(self) -> dict[str, str]:
        return self.__query.copy()


    def join_endpoint(self, *paths: str) -> UrlUtility:
        """エンドポイントを末尾に追加する
        Args:
            *paths (str): 可変長で渡せる   
        Returns:
            UrlUtility: newを返す
        """
        if not paths:
            raise ValueError('引数必要です。')
        new = self.__path
        for p in paths:
            new = urljoin(new, p)

        return UrlUtility(
            self.__root,
            new,
            self.__query,
        )
    
    def replease_endpoint(self, *paths: str) -> UrlUtility:
        """エンドポイントを置き換える
        Args:
            *paths (str): 可変長で渡せる      
        Returns:
            UrlUtility: newを返す

        """
        if not paths:
            raise ValueError('引数必要です。')
        new = ''
        for p in paths:
            new = urljoin(new, p)

        return UrlUtility(
            self.__root,
            new,
            self.__query,
        )
    

    def join_query(self, query : str | dict[str, str]) -> UrlUtility:
        """クエリパラメータを追加する。

        Args:
            query (str | dict[str, str]): クエリ文か辞書

        Returns:
            UrlUtility: newを返す
        """
        query :dict[str, str] = self.__parce_query(query)
        new = self.__query.copy()
        for k, v in query.items():
            new[k] = v
        return UrlUtility(
            self.__root,
            self.path,
            new,
        )
    
    def replace_query(self, query : str | dict[str, str]) -> UrlUtility:
        """クエリパラメータを置き換える。

        Args:
            query (str | dict[str, str]): クエリ文か辞書

        Returns:
            UrlUtility: newを返す
        """
        query :dict[str, str] = self.__parce_query(query)
        return UrlUtility(
            self.__root,
            self.__path,
            query,
        )
    
    def to_http(self)-> UrlUtility:
        """httpにする

        Returns:
            UrlUtility: new
        """
        pr : ParseResult = urlparse(self.__root)
        new = f'http://{pr.netloc}'
        return UrlUtility(
            new,
            self.__path,
            self.__query,
        )
    
    def to_https(self)-> UrlUtility:
        """httpsにする

        Returns:
            UrlUtility: new
        """
        pr : ParseResult = urlparse(self.__root)
        new = f'https://{pr.netloc}'
        return UrlUtility(
            new,
            self.__path,
            self.__query,
        )
    

    def replace_host(self, host : str)-> UrlUtility:
        """hostを変更する。

        Returns:
            UrlUtility: new
        """
        pr : ParseResult = urlparse(self.__root)
        port = '' if pr.port == '' else f':{pr.port}'
        new = f'{pr.scheme}://{host}{port}'
        return UrlUtility(
            new,
            self.__path,
            self.__query,
        )
    
    def replace_port(self, port : str | int)-> UrlUtility:
        """ポートを変更する。

        Returns:
            UrlUtility: new
        """
        pr : ParseResult = urlparse(self.__root)
        port = '' if port == '' else f':{port}'
        new = f'{pr.scheme}://{pr.hostname}{port}'
        return UrlUtility(
            new,
            self.__path,
            self.__query,
        )
    