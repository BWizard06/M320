class Grade:
    """
    Beschreibt eine Note mit der Note (value) und einem Datum (date)
    """

    def __init__(self, value, date):
        """
        Initialisiert ein Noten Objekt.
        :param value: Note
        :param date: Datum
        """
        if 1 <= value <= 6:
            self.__value = value
        else:
            self.__value = -1.0
        self.__date = date

    @property
    def value(self):
        return self.__value

    @property
    def date(self):
        return self.__date
