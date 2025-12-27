from abc import abstractmethod, ABC


class Person(ABC):
    def __init__(self, name, address, phone, email):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__email = email


class Customer(Person):
    def __init__(self, name, address, phone, email):
        self.__bookings = []  # List of bookings
        super().__init__(name, address, phone, email)

    # booking here refers to an instance of the Booking class
    def create_booking(self, booking):
        pass

    def update_booking(self, booking):
        pass

    def delete_booking(self, booking):
        pass


class Admin(Person):
    def __init__(self, name, address, phone, email):
        super().__init__(name, address, phone, email)

    # show here refers to an instance of the ShowTime class
    def add_show(self, show):
        pass

    def update_show(self, show):
        pass

    def delete_show(self, show):
        pass

    def add_movie(self, movie):
        pass
    
    def delete_movie(self, movie):
        pass
