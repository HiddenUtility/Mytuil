from pyutil.filetransfer.error.FileTransferError import FileTransferError


class DestinationSameFileExistsError(FileExistsError,FileTransferError):
    pass