from pyutil.ziputil.easy.EasyDirectoryCompressor import EasyDirectoryCompressor
from pyutil.ziputil.easy.easy_file_zip_conpressor import EasyFileZipConpressor
from pyutil.ziputil.i_zip_compressor import IZipCompressor


from pathlib import Path
from typing import override


class EasyZipCompressor(IZipCompressor):
    """圧縮する
    ファイルまたはフォルダを圧縮する
    同じディレクトリに出力する
    圧縮中は仮の拡張子にする
    """
    __zipper : IZipCompressor
    def __init__(self,target_path: Path, overwrite = True, unlink_src = True):
        """圧縮する

        ファイルまたはフォルダを圧縮する
        同じディレクトリに出力する
        圧縮中は仮の拡張子にする


        Args:
            target_path (Path): ファイルまはたディレクトリ
            overwite (bool, optional): 同名が存在していたら上書きする. Defaults to True.
            unlink_src (bool, optional): 圧縮ができたらソースを削除する. Defaults to True.

        """

        if not isinstance(target_path, Path):
            raise TypeError(f"{target_path}はパスオブジェクトではありません。")

        if target_path.is_file():
            self.__zipper = EasyFileZipConpressor(target_path, overwrite, unlink_src)
        if target_path.is_dir():
            self.__zipper = EasyDirectoryCompressor(target_path, overwrite, unlink_src)

    @override
    def to_zip(self):
        return self.__zipper.to_zip()