from classreport import Classreport


class Student:
    """
    Diese Klasse beschreibt ein Schüler. Der Schüler hat einen Namen
    und eine Referenz zur Schulklasse (schoolclass) und dem Klassenzeugnis (classreport).
    """

    def __init__(self, name, Classreport):
        """
        Initialisiert ein Schüler Objekt
        :param designation: Designation???
        """
        self.__name = name
        self.__the_class = None
        self.__report = Classreport


    @property
    def name(self):
        return self.__name

    @property
    def ref2school_class(self):
        return self.__the_class

    @ref2school_class.setter
    def ref2school_class(self, school_class):
        self.__the_class = school_class

    @property
    def report(self):
        return self.__report

    def print_report(self, student):
        print(self.__report.print)
#evtl. beziehungen ändern