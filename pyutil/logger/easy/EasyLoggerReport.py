from pathlib import Path

from pandas import DataFrame

from pyutil.logger.easy.ana.EasyLogFileFinalAnalysis import EasyLogFileFinalAnalysis


class EasyLoggerReport:
    """ログを解析した結果を返す"""
    __srcs : list[Path]
    def __init__(self, dirpath : Path) -> None:
        """Logを解析する

        Args:
            dirpath (Path): [Logが入っているディレクトリ]
        """
        self.__srcs = [f for f in dirpath.glob('*.log') if f.is_file()]
        EasyLogFileFinalAnalysis



    def to_df(self) -> DataFrame:
        """DataFrameで出力する

        Returns:
            DataFrame: [description]
        """
        return DataFrame()
    
    def to_csv(self, dest: Path, encoding='cp932') -> None:
        """結果をcsvで出力する

        Args:
            dest (Path): ファイルパス
            encoding (str, optional): _description_. Defaults to 'cp932'.


        """
        return self.to_df().to_csv(self, dest, index=False, encoding=encoding)