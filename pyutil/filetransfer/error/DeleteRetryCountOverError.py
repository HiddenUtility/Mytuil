from pyutil.filetransfer.error.FileTransferError import FileTransferError
from pyutil.myerror.retry_count_over_error import RetryCountOverError

class DeleteRetryCountOverError(RetryCountOverError,FileTransferError):
    pass