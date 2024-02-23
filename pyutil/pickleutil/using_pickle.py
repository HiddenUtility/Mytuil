import pickle
from pathlib import Path
from pyutil.pathuil.directory_creator import DirecotryCreator
from pyutil.pickleutil.PickleFileOutputFailureError import PickleFileOutputFailureError


class UsingPickle:

    @staticmethod
    def __mkdir(path: Path):
        DirecotryCreator.mkdir(path)

    @staticmethod
    def load( filepath: Path | str)-> object:
        filepath = Path(filepath)
        if not filepath.exists(): 
            raise FileNotFoundError(f"{filepath}は在りません。")
        with open(filepath, "rb") as f:
            obj = pickle.load(f)
        return obj
    
    @classmethod
    def dump(cls, filepath: Path | str, obj: object, ok_mkdir=True, is_verified=False)-> None:
        filepath = Path(filepath)
        if ok_mkdir: cls.__mkdir(filepath.parent)
        if not filepath.parent.exists():
            raise NotADirectoryError(f"{filepath.parent}は在りません。")
        with open(filepath, "wb") as f:
            pickle.dump(obj, f)

        if is_verified:
            new = cls.load(filepath)
            if obj != new:
                raise PickleFileOutputFailureError("__eq__を実装していないか、保存に失敗しました。")
            