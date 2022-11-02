class Subject:

    def __init__(self, name):
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

    def value(self, index):
        return self.__grades[index].value
    
    def date(self, index):  
        return self.__grades[index].date
    
    
    def grades(self):
        return self.__grades

    @property
    def average(self):
        sum = 0.0
        for zahl in range(self.size):
            sum += self.value(zahl)
        return round(sum / self.size, 2)
