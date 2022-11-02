class Candel: 

    def __init__(self, size, burning_time):
        if size != 0: 
            self.__size = size 
        else:
            self.__size = -1
        if burning_time != 0:
            self.__burning_time = burning_time
        else:
            self.__burning_time = -1

    @property
    def size(self):
        return self.__size

    @property
    def burning_time(self):
        return self.__burning_time

    def burn(self):
        pass
