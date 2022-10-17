from student import Student
from classreport import Classreport

class Schoolclass:
    """
    Beshcriebt ein Schulklasse. Die Schulklasse hat eine Designation und seine Schüler. In einer Klasse gibt es
    20 Schüler.
    """

    def __init__(self, designation):
        """
        Initialisiert einn Schulklasse Objekt.
        :param designation: Designation
        """
        self.__designation = designation
        self.__students = []


    @property
    def designation(self):
        return self.__designation

    def add_student(self, a_student):
        #if len(self.__students) == 20:
            self.__students.append(a_student)

    @property
    def student(self, index):
        return self.__students[index]

    @property
    def size (self):
        return len(self.__students)

    def print_student_list(self):
        print("Liste aller Schüler:")
        for student in self.__students:
            print(student.name)

    def print_student_report(self, students):
        total = []
        for student in students.report.subjects:
            total.append(student.get_average())
        result = sum(total) / len(total)
        result = 0.5 * round(result / 0.5)
        print("Durchschnittsnote vom " + students.name + ": \t" + str(result))
        for x in students.report.subjects:
            print(x.name + ":\t\t\t\t\t\t" + str(x.get_average()))