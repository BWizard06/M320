from subject import Subject
from grade import Grade

class ClassReport: 

    def __init__(self):
        self.__subjects = []
        self.__student = None
    
    @property
    def student(self):
        return self.__student
    
    @student.setter
    def set_student(self, student):
        self.__student = student
    
    def add_subject(self, subject):
        self.__subjects.append(subject)
    
    def subject(self, index): 
        return self.__subjects[index]
    
    def subjects(self):
        return self.__subjects

    def report_average(self):
        sum = 0.0
        for subject in self.__subjects:
            sum += subject.average
        return round(sum / len(self.__subjects), 2)
    
    def print(self):
        print(f"""Noten: """)
        for subject in self.__subjects:
            print(f"""\t{subject.name}: {subject.average}""") 
        print(f"Zeugnisschnitt: {self.report_average()}\n")

    def print_details(self, subject):
        for grade in subject.grades():
            print(f"\t{grade.value} am {grade.date}")




