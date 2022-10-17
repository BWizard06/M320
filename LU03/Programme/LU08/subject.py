from grade import Grade


class Subject:
    """
    Diese Klasse beschreibt ein Fach mit dem Namen (name) und den dazugehörigen Noten (grades).
    Jedes Fach muss aus min. 2 bis max. 4 Noten bestehen.
    """

    def __init__(self, name):
        """
        Initialisert ein Fach Objekt
        :param name: Name des Fachs
        """
        self.__name = name
        self.__grades = []


    @property
    def name(self):
        return self.__name

    def add_grade(self, grade):
        if self.size < 4:
            self.__grades.append(grade)

    @property
    def size(self):
        return len(self.__grades)


    def get_value(self, index):
        if index < self.size:
            grade = self.__grades[index]
            return grade.value
        else:
            return None


    def get_date(self, index):
        if index < self.size:
            grade = self.__grades[index]
            return grade.date
        else:
            return None

    @property
    def average(self):
        sum = 0.0
        for zahl in range(self.size):
            sum += self.get_value(zahl)
        return sum / self.size

if __name__ == "__main__":
    sub = Subject("mathe")
    sub.add_grade(Grade(4.0, "1.1.11"))
    sub.add_grade(Grade(5.0, "2.2.22"))
    print(sub.average)
