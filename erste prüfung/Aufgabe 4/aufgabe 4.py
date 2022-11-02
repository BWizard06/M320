class ExampleClass:

    def __init__(self, avalue, thisisasecondvalue, i):
        '''
        Initialisiert das Objekt.
        :param avalue: ein beliebiger Wert
        :param thisisasecondvalue: ein weitere beliebiger Wert
        :param i: Startwert für Counter
        '''
        self.__vale = avalue
        self.__otherValue = thisisasecondvalue
        self.__counter = i

    @property
    def counter(self):
        return self.__counter
