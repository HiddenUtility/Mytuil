from traceback import format_exception
from typing import Self
from pyutil.structure.ResutStatus import ResutStatus


class PoolResultTypeDefinition:
    """結果いれる構造体"""
    __status : str
    __count : int
    __error : str
    __cache : object
    __detail : dict
    __message : str
    
    
    @property
    def message(self) -> str:
        return self.__message
    
    @property
    def count(self) -> str:
        return self.__count

    @property
    def detail(self) -> dict:
        return self.__detail

    @property
    def cache(self) -> str:
        return self.__cache

    @property
    def error(self) -> str:
        return self.__error

    @property
    def status(self) -> ResutStatus:
        return self.__status

    def __init__(self,
                 message:str = '',
                 count : int = 0,
                 error:str = '',
                 cache:object = '',
                 detail: dict = {}
                 ) -> None:
        """結果ようの構造体

        errorに書き込まなければ成功扱い

        Args:
            message (str, optional): ちょっとしたコメント. Defaults to ''.
            error (str, optional): エラーかどうか. Defaults to ''.
            cache (object, optional): キャッシュ用. Defaults to ''.
            detail (dict, optional): ほかにも詳細いれたいとき. Defaults to {}.
        """
        self.__message = message
        self.__count = count
        self.__error = error
        self.__status = ResutStatus.OK
        if '' != error:
            self.__status = ResutStatus.NG

        self.__cache = cache
        self.__detail = detail

    def __str__(self) -> str:
        body = [
            f'message = {self.message}',
            f'error = {self.error}',
            f'status = {self.status.name}',
        ]
        return '\n'.join(body)
    
    def __repr__(self) -> str:
        return str(self)

    def is_error(self) -> bool:
        return self.status == ResutStatus.NG
    
    def write_error(self, error:str) -> Self:
        """ほかの情報維持してエラー書き込み

        Args:
            error (str):エラー

        Returns:
            PoolResultTypeDefinition: new
        """
        return PoolResultTypeDefinition(message=self.message, count=self.count, error=error, cache=self.cache, detail=self.detail)
    
    def write_error_stack_trace(self, 
                    e: Exception) -> Self:
        """トラックトレース書き込む"""
        self.write_error('\n'.join(format_exception(e)))

    def write_cache(self, cache:object) -> Self:
        """キャッシュプロパティーを変更した結果を返す。

        Args:
            cache (object): 入れたいオブジェクトなんでも

        Returns:
            PoolResultTypeDefinition: _description_
        """
        return PoolResultTypeDefinition(message=self.message, count=self.count, error=self.error, cache=cache, detail=self.detail)

    def write_message(self, message:str) -> Self:
        """メッセージを変更した結果を返す。

        Args:
            message (str): メッセージ

        Returns:
            PoolResultTypeDefinition: _description_
        """
        return PoolResultTypeDefinition(message=message, count=self.count, error=self.error, cache=self.cache, detail=self.detail)

    def write_count(self, count:int) -> Self:
        """カウントを変更した結果を返す。

        Args:
            count (int): 数字

        Returns:
            PoolResultTypeDefinition: _description_
        """
        return PoolResultTypeDefinition(message=self.message, count=count, error=self.error, cache=self.cache, detail=self.detail)


