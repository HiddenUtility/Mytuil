from pyutil.filetransfer.error.FileTransferError import FileTransferError


class DestinationSmallSizeFileError(FileExistsError,FileTransferError):
    pass


