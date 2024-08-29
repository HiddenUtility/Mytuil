

from pyutil.myerror.MyError import MyError


class RetryCountOverError(MyError):
    """リトライ上限に達した"""
    ...