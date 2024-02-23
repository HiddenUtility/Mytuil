
import matplotlib
matplotlib.use("Agg")

from abc import ABC, abstractmethod

class PlotMaker(ABC):
    @abstractmethod
    def plot(self):...



