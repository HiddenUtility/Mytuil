from datetime import datetime, timedelta


class XTimePassingFromReferenceTimePolicy:
    """現在時間より何日何時間何分前より評価対象が過去かどうか"""

    __is_past : bool
    def __init__(self, compared_time:datetime,
                 dyas = 0,
                 hours = 0,
                 minutes = 0,
                 ) -> None:
        """現在時間より何日何時間何分前より評価対象が過去かどうか

        Args:
            compared_time (datetime): 比較対象
            dyas (int, optional): 何日前. Defaults to 0.
            hours (int, optional): 何時間前. Defaults to 0.
            minutes (int, optional): 何分前. Defaults to 0.
        """
        border = datetime.now() - timedelta(days=dyas, hours=hours, minutes=minutes)
        self.__is_past =  compared_time < border

    def is_past(self) -> bool:
        """基準時間よりも過去である"""
        return self.__is_past
    
if __name__ == '__main__':
    po = XTimePassingFromReferenceTimePolicy(datetime.now(), dyas=0, minutes=1)
    assert not po.is_past()

    po = XTimePassingFromReferenceTimePolicy(datetime(2023,1,1), dyas=0, minutes=1)
    assert po.is_past()
