from __future__ import annotations
from copy import copy

from xml.dom import minidom
from xml.etree import ElementTree
from xml.etree.ElementTree import Element

from pathlib import Path

from pyutil.pathuil import DirecotryCreator


class XmlUtility:
    """xml簡単操作
    ミューダブルなオブジェクト
    辞書を突っ込んでエレメントを追加できる。
    dumpでファイル出力
    """
    __root : Element
    def __init__(self, root :Element = Element('root')) -> None:
        self.__root = root

            
    def dump(self, dest_filepath: Path, unicode = 'utf-8'):
        """xmlで出力する

        Args:
            dest_filepath (Path): 出力するファイル名
            unicode (str, optional): _description_. Defaults to 'utf-8'.
        """
        DirecotryCreator(dest_filepath.parent)
        
        doc = minidom.parseString(ElementTree.tostring(self.__root, unicode))
        with open(dest_filepath,'w') as f:
            doc.writexml(f, encoding=unicode, newl='\n', indent='', addindent='  ')

    @classmethod
    def set_dict(cls, element : Element, data: dict) -> None:
        """Elementオブジェクトにサブエレメントを辞書でセットする。
        辞書入れ子なら再回帰でセットできる。

        Args:
            element (Element): _description_
            data (dict): _description_
        """
        
        for k, v in data.items():
            sub_element = ElementTree.SubElement(element, k)
            if isinstance(v, dict):
                cls.set_dict(sub_element, v)
            else:
                sub_element.text = str(v)

    def load_dict(self, data: dict) -> XmlUtility:
        """辞書を取り込んで要素を追加する。
         属性は設定できない

        Args:
            data (dict): 取り込みたいデータ。辞書入れ子なら再回帰でセットできる。

        Returns:
            XmlUtility: new
        """
        new = copy(self.__root)
        self.set_dict(new, data)
        return XmlUtility(new)


    
    def to_root_element(self) -> Element:
        """rootエレメントを返す
        Element操作は手動でやってくれ。

        Element.iter() 配下 (その子ノードや孫ノードなど) の部分木全体を再帰的にイテレートするいくつかの役立つメソッドを持っています
        Element.findall() はタグで現在の要素の直接の子要素のみ検索します。
        Element.find() は特定のタグで 最初の 子要素を検索し、 
        Element.text は要素のテキストコンテンツにアクセスします。
        Element.get() は要素の属性にアクセスします:

        """
        return self.__root

    def load_xml(self, src: Path):
        return XmlUtility(ElementTree.parse(src).getroot())


