from datetime import datetime, timedelta


class XdayDateTimePassingFromReferenceTimePolicy:
    """基準日時より過去かどうか"""

    __is_past : bool
    def __init__(self, compared_time:datetime,
                 past_dyas = 0,
                 reference_hours = 0) -> None:
        """基準時間より前か後かを判断する
        - デフォなら本日の0時が基準時間となる
        - reference_dyas = 1 なら1日前
        - マイナスの値も入れれるが未来になるので必ず過去判定になる

        Args:
            compared_time (datetime): 判断する時間
            past_dyas (int, optional): 基準日数. Defaults to 0.
            reference_houre (int, optional): 基準時間. Defaults to 5.

        """
        border = datetime.now().replace(hour=0,minute=0,second=0,microsecond=0) - timedelta(days=past_dyas)
        border = border.replace(hour=reference_hours)
 

        self.__is_past = compared_time < border



    def is_past(self) -> bool:
        """基準時間よりも過去である"""
        return self.__is_past


if __name__ == '__main__':
    po = XdayDateTimePassingFromReferenceTimePolicy(datetime.now())
    assert not po.is_past()

    po = XdayDateTimePassingFromReferenceTimePolicy(datetime.now(), past_dyas=1)
    assert not po.is_past()

    po = XdayDateTimePassingFromReferenceTimePolicy(datetime.now(), past_dyas=-1)
    assert po.is_past()

    # 時間
    po = XdayDateTimePassingFromReferenceTimePolicy(datetime.now(), past_dyas=0, reference_hours=18)
    assert po.is_past()