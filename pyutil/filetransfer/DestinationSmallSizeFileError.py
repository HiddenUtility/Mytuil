from pyutil.filetransfer.FileTransferError import FileTransferError


class DestinationSmallSizeFileError(FileExistsError,FileTransferError):
    pass