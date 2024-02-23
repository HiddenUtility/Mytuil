from pyutil.filetransfer.error.FileTransferError import FileTransferError
from pyutil.myerror.retry_count_over_error import RetryCountOverError

class CopyRetryCountOverError(RetryCountOverError,FileTransferError):
    pass