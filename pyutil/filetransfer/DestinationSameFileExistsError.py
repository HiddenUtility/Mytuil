from pyutil.filetransfer.FileTransferError import FileTransferError


class DestinationSameFileExistsError(FileExistsError,FileTransferError):
    pass