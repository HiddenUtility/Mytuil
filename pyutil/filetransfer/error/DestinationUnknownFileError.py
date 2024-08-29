from pyutil.filetransfer.error.FileTransferError import FileTransferError


class DestinationUnknownFileError(FileExistsError,FileTransferError):
    """不明なファイルが既に存在する.
    元ファイルよりもファイルサイズが大きい"""
    