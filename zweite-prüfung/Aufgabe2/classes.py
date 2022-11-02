class Transport:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end

    def from_to(self):
        print(f"gehe von {self.__start} nach {self.__end}")


class Automobile(Transport):

    def __init__(self, start, end, volume):
        super().__init__(start, end)
        self.__volume = volume

    def fuel_avaiable(self):
        print(f"mit {self.__volume}l im Tank")

class Truck(Automobile):

    def __init__(self, start, end, volume, material):
        super().__init__(start, end, volume)
        self.__material = material

    def transport(self):
        print(f"und transportierer {self.__material}")
