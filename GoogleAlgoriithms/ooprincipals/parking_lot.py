from enum import Enum
from abc import ABC, abstractmethod


class Type(Enum):
    SMALL = 0
    LARGE = 1
    BIKE = 2


class ParkingSpot(ABC):
    def __init__(self, id, isFree, vehicle, type:Type):
        self.id = id
        self.isFree = isFree
        self.vehicle = vehicle
        self.type = type

    @abstractmethod
    def assign_vehicle(self):
        pass

    @abstractmethod
    def remove_vehicle(selfs):
        pass


class Compact(ParkingSpot):
    def __init__(self, id, is_free=None, vehicle=None):
        super().__init__(id, is_free, vehicle, Type.SMALL)

    def assign_vehicle(self):
        pass

    def remove_vehicle(selfs):
        pass


class Large(ParkingSpot):
    def __init__(self, id, is_free=None, vehicle=None):
        super().__init__(id, is_free, vehicle, Type.LARGE)

    def assign_vehicle(self):
        pass

    def remove_vehicle(selfs):
        pass


class Bike(ParkingSpot):
    def __init__(self, id, is_free=None, vehicle=None):
        super().__init__(id, is_free, vehicle, Type.BIKE)

    def assign_vehicle(self):
        pass

    def remove_vehicle(selfs):
        pass


class Vehicle(ABC):
    def __init__(self, license_no, type:Type):
        self.license_no = license_no
        self.type = type

    @abstractmethod
    def assign_ticket(self):
        pass


class Car(Vehicle):
    def __init__(self, license_no):
        super().__init__(license_no, Type.SMALL)

    def assign_ticket(self):
        pass


class Truck(Vehicle):
    def __init__(self, license_no):
        super().__init__(license_no, Type.LARGE)

    def assign_ticket(self):
        pass


class Account(ABC):
    def __init__(self, user_name, password):
        self.__username = user_name
        self.__password = password


class Admin(Account):
    def __init__(self, user_name, password):
        super().__init__(user_name, password)


class ParkingLot(object):
    def __init__(self, name, address):
        self.name = name
        self.address = address


def main():
    parking_log_instance = ParkingLot("My Parking Lot", "Fifty Avenue")


if __name__ == "__main__":
    main()
