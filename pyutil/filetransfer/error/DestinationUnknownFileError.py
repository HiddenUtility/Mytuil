from pyutil.filetransfer.error.FileTransferError import FileTransferError


class DestinationUnknownFileError(FileExistsError,FileTransferError):
    pass