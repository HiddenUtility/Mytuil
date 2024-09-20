from pandas import DataFrame, to_datetime


class DataFrameColumnValueDatetimeTransfer:
    """
    dfの列をdatetimeに変換したdfを得る
    """
    __df : DataFrame
    __column : str
    __format : str | None

    def __init__(self, df:DataFrame, column: str, format :str = None) -> None:
        """dfの列をdatetimeに変換したdfを得る

        Args:
            df (DataFrame): _description_
            column (str): _description_
            format (str, optional): datetimeのフォーマット形式'%d%m'を指定可能. Defaults to None.
        """
        self.__df = df.copy()
        self.__column = column
        self.__format = format

    def transfer(self) -> DataFrame:
        """

        Returns:
            DataFrame: _description_
        """
        df = self.__df.copy()
        df[self.__column] = to_datetime(self.__df[self.__column],format=self.__format)
        return df
    
