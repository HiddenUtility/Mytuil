from pyutil.myerror.retry_count_over_error import RetryCountOverError
from pyutil.ziputil.error.ZiputilError import ZiputilError


class ZipRetryCountOverError(ZiputilError,RetryCountOverError):...