import math

class Circle:

    def __init__(self, u):
        self.__radius = u

    @property
    def radius(self):
        return self.__radius

    def area(self):
        return round((self.__radius * self.__radius) * math.pi, 0)

    def scale(self, factor):
        self.__radius = self.__radius * factor

    def __str__(self):
        return (f"Kreis -> Fläche: {self.area()}, Radius: {self.__radius}")
