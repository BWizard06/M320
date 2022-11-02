class Grade:
    def __init__(self, value: float, date):
        self.__value = value
        self.__date = date
    
    @property
    def value(self):
        return self.__value
    
    @property
    def date(self):
        return self.__date
        