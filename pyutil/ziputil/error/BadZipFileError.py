from pyutil.ziputil.error.ZiputilError import ZiputilError


from zipfile import BadZipFile


class BadZipFileError(ZiputilError,BadZipFile):...