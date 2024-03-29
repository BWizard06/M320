from classreport import Classreport
from grade import Grade
from schoolclass import Schoolclass
from student import Student
from subject import Subject

if __name__ == "__main__":
    i2a = Schoolclass("I2a")
    clre1 = Classreport()
    clre2 = Classreport()
    clre3 = Classreport()
    de = Subject("Deutsch")
    mathe = Subject("Mathe")
    wr = Subject("WR")
    bzz = Subject("BZZ")
    en = Subject("Englisch")
    clre1.add_subject(mathe)
    clre1.add_subject(wr)
    clre1.add_subject(de)
    clre1.add_subject(en)
    clre1.add_subject(bzz)
    clre2.add_subject(mathe)
    clre2.add_subject(wr)
    clre2.add_subject(de)
    clre2.add_subject(en)
    clre2.add_subject(bzz)
    clre3.add_subject(mathe)
    clre3.add_subject(wr)
    clre3.add_subject(de)
    clre3.add_subject(en)
    clre3.add_subject(bzz)
    grade1 = Grade(4.0, "1.1.2022")
    grade2 = Grade(5.5, "2.2.2003")
    grade3 = Grade(6.0, "9.8.2002")
    grade4 = Grade(3.5, "3.3.2005")
    grade5 = Grade(2.5, "4.5.2009")
    grade6 = Grade(4.0, "3.4.2002")
    de.add_grade(grade1)
    de.add_grade(grade2)
    mathe.add_grade(grade3)
    mathe.add_grade(grade4)
    wr.add_grade(grade5)
    wr.add_grade(grade6)
    bzz.add_grade(grade1)
    bzz.add_grade(grade6)
    en.add_grade(grade4)
    en.add_grade(grade2)
    student1 = Student("Amk", clre1)
    student2 = Student("Safi", clre2)
    student3 = Student("lol", clre3)
    i2a.add_student(student1)
    i2a.add_student(student2)
    i2a.add_student(student3)
    i2a.print_student_list()
    student1.print_report(student1)