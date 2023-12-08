from pathlib import Path
from ziputil import UsingZip

class Test:
    def __init__(self) -> None:
        pass
    def run(self):
        pass

if __name__ == "__main__":
    fs = [f for f in Path(r"F:\test").glob("*") if f.is_file()]
    for f in fs:
        test = UsingZip(f)
        test.to_zip()

