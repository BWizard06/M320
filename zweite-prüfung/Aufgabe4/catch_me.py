class Reader:
    def __init__(self):
        self.__in   = ''
        self.__val1 = 0
        self.__val2 = 0

    def read_tupel(self):
        print ("geben Sie 2 ganze Zahlen durch Komma getrennt ein, z.B. 5,6")
        x = self.__in = input("Ihre Eingabe: ").split(',')
        try:
            self.__val1 = int(x[0])
        except:
            raise NumberFormatException(x[0])

        try:
            self.__val2 = int(x[1])
        except:
            raise NumberFormatException(x[1])

    def compute(self):
        return self.__val1 / self.__val2

class NumberFormatException(Exception):

    def __init__(self, text):
        super().__init__(f"ERROR: {text} ist ein ungültiger Text!")


if __name__ == "__main__":
    reader = Reader()
    #
    try: 
        reader.read_tupel()
        print("Division = " + str(reader.compute()))

    except ZeroDivisionError:
        print("Division durch 0 nicht möglich")
    except NumberFormatException as num:
        print(num)


