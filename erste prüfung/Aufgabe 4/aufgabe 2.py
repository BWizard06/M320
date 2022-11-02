class Workplace:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


class Employee:

    def __init__(self, name, workplace):
        self.__name = name
        self.__workplace = workplace

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def to_string(self):
        print(f"{self.__name} arbeitet in Zimmer {self.__workplace.name}")



if __name__ == "__main__":
    workplace = Workplace("25")
    employee = Employee("Martin", workplace)
    employee.to_string()