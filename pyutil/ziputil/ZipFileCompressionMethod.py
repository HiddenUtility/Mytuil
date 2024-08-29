import zipfile
from enum import Enum


class ZipFileCompressionMethod(Enum):
    """圧縮率"""
    ZIP_STORED = zipfile.ZIP_STORED #　無圧縮
    ZIP_DEFLATED = zipfile.ZIP_DEFLATED
    ZIP_BZIP2 = zipfile.ZIP_BZIP2
    ZIP_LZMA = zipfile.ZIP_LZMA