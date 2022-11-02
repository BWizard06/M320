from student import Student
from classreport import ClassReport
from schoolclass import SchoolClass
from subject import Subject
from grade import Grade


i1a = SchoolClass("I1A")    

# Student 1

student1_report = ClassReport()
student1_subject1 = Subject("Mathe")
student1_subject2 = Subject("Deutsch")
student1_subject3 = Subject("Englisch")
student1_grade1 = Grade(4.0, "26.06.2022")
student1_grade2 = Grade(5.0, "27.06.2022")
student1_grade3 = Grade(5.5, "14.06.2022")
student1_grade4 = Grade(4.5, "15.06.2022")
student1_grade5 = Grade(6.0, "14.06.2022")
student1_grade6 = Grade(4.9, "15.06.2022")
student1_subject1.add_grade(student1_grade1)
student1_subject1.add_grade(student1_grade2)
student1_subject2.add_grade(student1_grade3)
student1_subject2.add_grade(student1_grade4)
student1_subject3.add_grade(student1_grade5)
student1_subject3.add_grade(student1_grade6)
student1_report.add_subject(student1_subject1)
student1_report.add_subject(student1_subject2)
student1_report.add_subject(student1_subject3)
student1 = Student("Ben", student1_report)
i1a.add_student(student1)

student1.print_report()

# Student 2
student2_report = ClassReport()
student2_subject1 = Subject("Mathe")
student2_subject2 = Subject("Deutsch")
student2_subject3 = Subject("Englisch")
student2_grade1 = Grade(5.5, "26.06.2022")
student2_grade2 = Grade(5.9, "27.06.2022")
student2_grade3 = Grade(5.2, "14.06.2022")
student2_grade4 = Grade(5.4, "15.06.2022")
student2_grade5 = Grade(2.0, "14.06.2022")
student2_grade6 = Grade(3.9, "15.06.2022")
student2_subject1.add_grade(student2_grade1)
student2_subject1.add_grade(student2_grade2)
student2_subject2.add_grade(student2_grade3)
student2_subject2.add_grade(student2_grade4)
student2_subject3.add_grade(student2_grade5)
student2_subject3.add_grade(student2_grade6)
student2_report.add_subject(student2_subject1)
student2_report.add_subject(student2_subject2)
student2_report.add_subject(student2_subject3)
student2 = Student("Furda", student2_report)
i1a.add_student(student2)

student2.print_report()

# Student 3
student3_report = ClassReport()
student3_subject1 = Subject("Mathe")
student3_subject2 = Subject("Deutsch")
student3_subject3 = Subject("Englisch")
student3_grade1 = Grade(2.5, "26.06.2022")
student3_grade2 = Grade(2.3, "27.06.2022")
student3_grade3 = Grade(2.7, "14.06.2022")
student3_grade4 = Grade(2.2, "15.06.2022")
student3_grade5 = Grade(3.9, "14.08.2022")
student3_grade6 = Grade(2.5, "15.02.2022")
student3_subject1.add_grade(student3_grade1)
student3_subject1.add_grade(student3_grade2)
student3_subject2.add_grade(student3_grade3)
student3_subject2.add_grade(student3_grade4)
student3_subject3.add_grade(student3_grade5)
student3_subject3.add_grade(student3_grade6)
student3_report.add_subject(student3_subject1)
student3_report.add_subject(student3_subject2)
student3_report.add_subject(student3_subject3)
student3 = Student("Shahin", student3_report)
i1a.add_student(student3)


student3.print_report()
student3.print_details(student3_subject3)

i1a.print_student_list()