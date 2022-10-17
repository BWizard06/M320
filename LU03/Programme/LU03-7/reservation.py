class Reservation:

    def __init__(self, number, event):
        self.__number = number
        self.__event = event
        self.__customer = None

    @property
    def number(self):
        return self.__number

    @property
    def event(self):
        return self.__event

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        self.__customer = customer

    def print(self):
        print(f"Reservation {self.__number} ({self.__event}) für Kunde {self.__customer.name}")
