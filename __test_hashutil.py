from pathlib import Path
from hashutil import FileHashCheacker

if __name__ == '__main__':
    fs = [f for f in Path(r"F:\test").glob("*") if f.is_file()]
    for f in fs:
        test = FileHashCheacker(f)
        print(test.to_hash())