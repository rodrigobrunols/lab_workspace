from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    @abstractmethod
    def update(self, symbol: str, price: float):
        pass


class Subject(ABC):
    @abstractmethod
    def notify(self):
        pass

    def attach(self, observer):
        pass

    def detach(self):
        pass


class Stock(Subject):
    def __init__(self, symbol: str):
        self._observers = []
        self.symbol = symbol
        self.price = 0.0

    def notify(self):
        for observer in self._observers:
            observer.update(self, self.symbol, self.price)

    def set_price(self, price: float):
        self.price = price
        self.notify()


class PriceDisplay(Observer):

    def update(self, symbol: str, price: float):
        print(f"PriceDisplay updated: {symbol}: {price}")
