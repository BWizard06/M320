from subject import Subject
from grade import Grade

class Classreport:
    """
    Beschreibt ein Klassenzeugnis mit einer Refernz zum Schüler und zum Fach. Ein Zeugnis besteht aus 3 Fachnoten.
    """

    def __init__(self):
        """
        Initialisiert ein Zeugnis Objekt
        """
        self.__subjects = []
        self.__student = None


    @property
    def subjects(self):
        return self.__subjects

    @property
    def student(self):
        return self.__student

    def size(self):
        return len(self.__subjects)

    @student.setter
    def student(self, student):
        self.__student = student

    def add_subject(self, subject):
        if len(self.__subjects) < 3:
            self.__subjects.append(subject)
        else:
            return 0

    def get_subject(self, index):
        return self.__subjects[index]

    def to_string(self):
        view = "Zeugnis\n"
        for count in range(len(self.__subjects)):
            view += self.__subjects[count].name + " " + str(self.__subjects[count].average) + "\n"
        return view

    def print(self):
        print(self.to_string())


if __name__ == "__main__":
    grade1 = Grade(4.0, "2022.20.12")
    grade2 = Grade(5.0, "2022.20.12")
    grade3 = Grade(3.0, "2022.20.12")
    de = Subject("duetsch")
    en = Subject("Englisch")
    math = Subject("Maths")
    de.add_grade(grade1)
    de.add_grade(grade2)
    en.add_grade(grade2)
    en.add_grade(grade3)
    math.add_grade(grade1)
    math.add_grade(grade3)
    zeugnis1 = Classreport()
    zeugnis1.add_subject(de)
    zeugnis1.add_subject(en)
    zeugnis1.add_subject(math)

    zeugnis1.print()