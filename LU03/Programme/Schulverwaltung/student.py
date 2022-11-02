from classreport import ClassReport

class Student:

    def __init__(self, name, report: ClassReport):
        self.__name = name
        self.__report = report
        self.__the_class = None
    
    @property
    def name(self):
        return self.__name
    
    @property
    def report(self):
        return self.__report
    
    @property
    def the_class(self):
        return self.__the_class
    
    @the_class.setter
    def the_class(self, the_class):
        self.__the_class = the_class

    
    def print_report(self):
        print(f"Zeugnis für {self.name}")
        self.report.print()

    def print_details(self, subject):
        print(f"Alle Einzelnoten des Faches {subject.name} für {self.name}")
        self.report.print_details(subject)