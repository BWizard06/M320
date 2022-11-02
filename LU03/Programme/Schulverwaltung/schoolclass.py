class SchoolClass:

    def __init__(self, designation):
        self.__designation = designation
        self.__students = []

    @property
    def designation(self):
        return self.__designation

    def add_student(self, student):
        if len(self.__students) < 20:
            self.__students.append(student)

    def student(self, index):
        return self.__students[index]
    
    def size(self):
        return len(self.__students)
    
    def print_student_list(self):
        print(f"Alle Studenten der Klasse {self.designation}:")
        for student in self.__students:
            print(f"\t{student.name}")
    
    def print_student_report(self, student):
        student.print_report()