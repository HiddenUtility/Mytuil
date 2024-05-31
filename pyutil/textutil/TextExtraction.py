import re

from pyutil.textutil.NcCommentOutRemovedText import NcCommentOutRemovedText


class TextExtractionMethod:
    """stringから情報を抜き取る
    ()はコメントして無視する
    """

    @staticmethod
    def extract_float(text: str, target: str) -> str:
        """前方一致でfloatを得る"""
        text = NcCommentOutRemovedText(text).value
        strs = [num for num in re.findall( target + r"([-+]?\d*\.\d+|\d+)", text)]
        if not strs:
            return ''
        return strs[0]
    

    @staticmethod
    def extract_int(text: str, target: str) -> str:
        """前方一致でintを得る"""
        text = NcCommentOutRemovedText(text).value
        strs = [num for num in re.findall( target + r"(\d+)", text)]
        if not strs:
            return ''
        return strs[0]
    
    @staticmethod
    def extract_texts(text: str, target: str) -> list[str]:
        text = NcCommentOutRemovedText(text).value
        return [num for num in re.findall( target + r"\d+", text)]
