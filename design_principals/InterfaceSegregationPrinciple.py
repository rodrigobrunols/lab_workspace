"""
Prefer small, focused interfaces over large, general-purpose ones. Don't force classes to implement methods they don't
need. If a class only needs two methods from an interface with ten methods, that interface is too big.

"""

from abc import ABC, abstractmethod


class Workable:
    @abstractmethod
    def work(self) -> None:
        pass


class Feedable:
    @abstractmethod
    def eat(self) -> None:
        pass


class Restable:
    @abstractmethod
    def sleep(self) -> None:
        pass


class Human(Workable, Feedable, Restable):
    def work(self) -> None:
        print("Working")

    def eat(self) -> None:
        print("Eating")

    def sleep(self) -> None:
        print("Sleeping")


class Robot(Workable):
    def work(self) -> None:
        print("Working")
