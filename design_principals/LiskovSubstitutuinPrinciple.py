from abc import ABC, abstractmethod

"""
Subclasses must work wherever the base class works. If you have a method that accepts a Bird, passing in a Penguin 
shouldn't break things even though penguins can't fly. This means your subclasses can't violate the expectations 
set by the parent class.
"""


class Bird(ABC):
    @abstractmethod
    def eat(self):
        pass


class FlyingBird(Bird):
    @abstractmethod
    def fly(self):
        pass


class Penguin(Bird):
    def eat(self):
        print("Penguin eating")


class Sparrow(FlyingBird):
    def eat(self):
        print("Sparrow eating")

    def fly(self):
        print("Sparrow flying")
