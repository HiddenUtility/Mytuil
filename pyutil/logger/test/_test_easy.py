import asyncio
import random
from pathlib import Path
from shutil import rmtree
from pyutil.logger.easy.easy_logger import EasyLogger


class TestMyLogger:
    def __init__(self) -> None:
        if Path("log").exists():
            rmtree(Path("log"))
        self.__logger = EasyLogger()

    async def __run_task(self, name: str):
        self.__logger.start(name)
        await asyncio.sleep(random.choice(list(range(1,11))))
        self.__logger.end(name)
    
    async def run(self):
        self.__logger.start()
        tasks = [asyncio.create_task(self.__run_task(f"{i}君")) for i in range(1,11)]
        [await t for t in tasks]
        self.__logger.end()


