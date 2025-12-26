from abc import ABC, abstractmethod


class MissingValueStrategy(ABC):
    def __init__(self, df):
        self.df = df

    @abstractmethod
    def handle(self):
        pass


class DropMissing(MissingValueStrategy):
    def handle(self):
        self.df = self.df.dropna()
        return self.df


class FillMean(MissingValueStrategy):
    def handle(self):  # self.df.mean() = show mean of all column
        return self.df.fillna(self.df.mean(numeric_only=True))


class FillMode(MissingValueStrategy):
    def handle(self):
        return self.df.fillna(self.df.mode(numeric_only=True))
