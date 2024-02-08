from abc import ABC, abstractstaticmethod


class BuildProcess(ABC):
    @abstractstaticmethod
    def run(self):...