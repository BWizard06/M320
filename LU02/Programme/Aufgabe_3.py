class Bicycle:

    def __init__(self, type="Mountain-Bike", size=48):
            
        self.type = type
        self.size = size
        self.__color = "gray"

    @property
    def type(self):
        return self.__type
    
    @type.setter
    def type(self, type):
        self.__type = type

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size


    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    def print(self):
        print(f"""Fahrrad: 
        Art: {self.__type}
        Rahmengrösse: {self.__size}
        Farbe: {self.__color}
        """)



if __name__ == '__main__':
    fahrrad1 = Bicycle()
    fahrrad2 = Bicycle("racebike")
    fahrrad3 = Bicycle("citybike", 42)

    fahrrad3.color = "red"

    fahrrad1.print()
    fahrrad2.print()
    fahrrad3.print()








