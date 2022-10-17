from circle import Circle
from cuboid import Cuboid

class Circlecuboid:

    def __init__(self, u):
        self.__circle = Circle(u)
        self.__cuboid = Cuboid(u)


    @property
    def circle(self):
        return self.__circle
    
    @property
    def cuboid(self):
        return self.__cuboid

    def area_difference(self):
        return round(self.__cuboid.area() - self.__circle.area(), 0)

    def scale(self, factor):
        self.__circle.scale(factor)
        self.__cuboid.scale(factor)
        print(f"\nEs wurde um den Faktor {factor} skaliert")

    def __str__(self):
        return (f"""Kreiseck: 
\t{self.__circle}
\t{self.__cuboid}
\tFlächendifferenz: {self.area_difference()}""")
