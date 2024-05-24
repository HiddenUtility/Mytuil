import re

from pyutil.textutil.NcCommentOutRemovedText import NcCommentOutRemovedText


class TextExtraction:

    @staticmethod
    def extract_float(text: str, target: str) -> str:
        text = NcCommentOutRemovedText(text).value
        strs = [num for num in re.findall( target + r"([-+]?\d*\.\d+|\d+)", text)]
        if not strs:
            return ''
        return strs[0]
    

    @staticmethod
    def extract_int(text: str, target: str) -> str:
        text = NcCommentOutRemovedText(text).value
        strs = [num for num in re.findall( target + r"(\d+)", text)]
        if not strs:
            return ''
        return strs[0]
    
    @staticmethod
    def extract_texts(text: str, target: str) -> list[str]:
        text = NcCommentOutRemovedText(text).value
        return [num for num in re.findall( target + r"\d+", text)]
