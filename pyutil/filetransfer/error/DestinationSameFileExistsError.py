from pyutil.filetransfer.error.FileTransferError import FileTransferError


class DestinationSameFileExistsError(FileExistsError,FileTransferError):
    """すでに同じファイルが存在する"""