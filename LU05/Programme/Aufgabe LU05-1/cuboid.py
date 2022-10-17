from point import Point

class Cuboid:

    def __init__(self, u):
        self.__u = u
        self.__points = []
        self.__points.append(Point(-u, u))
        self.__points.append(Point(u, u))
        self.__points.append(Point(u, -u))
        self.__points.append(Point(-u, -u))

    def point(self, index):
        return self.__points[index]

    
    def area(self):
        return (2*self.__u)*(2*self.__u)

    def scale(self, factor):
        self.__u = self.__u * factor
        for point in self.__points:
            point.x = point.x * factor
            point.y = point.y * factor

    def __str__(self):
        return f"Eck ---> Fläche: {self.area()}, Punkte: {self.point(0)}, {self.point(1)}, {self.point(2)}, {self.point(3)}"
