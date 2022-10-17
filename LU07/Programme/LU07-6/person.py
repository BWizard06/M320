class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__adress = None

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def adress(self):
        return self.__adress

    @adress.setter
    def adress(self, adress):
        self.__adress = adress

    def print(self):
        print(f"""Angaben zu Kunde:
\tName: {self.name}  
\tAlter: {self.age}
\tAdresse: {self.adress}""")

