class Customer:
	
    def __init__(self, name, reservation):
        self.__name = name
        self.__reservation = reservation

    @property
    def name(self):
        return self.__name

    @property
    def reservation(self):
        return self.__reservation

    def print(self):
        print(f"{self.__name} hat eine Reservation für den Anlass '{self.__reservation.event}'")

    