class Student:
    def __init__(self, name, year, attendances):
        self.name = name
        self.year = year
        
        self.grades = []
        self.attendance = attendances

    def add_grade(self, grade):
        if isinstance(grade, Grade):
            self.grades.append(grade)
    
    def get_average(self):
        total = sum(grade.score for grade in self.grades)
        return total / len(self.grades) if self.grades else 0

    def attendance(self, date, value):
        self.attendance.append(date, value)

    def __repr__(self):
        return self.attendance
    
    
roger = Student("Roger van der Weyden", 10, {"15/09/2023": True})
sandro = Student("Sandro Botticelli", 12, {"15/09/2023": False})
pieter = Student("Pieter Bruegel the Elder", 8, {"15/09/2023": True})

class Grade:
    
    minimum_passing = 65
    
    def __init__(self, score):
        self.score = score
    
    def is_passing(self):
        return self.score >= self.minimum_passing


pieter_grade = Grade(100)
pieter.add_grade(pieter_grade.score)

pieter.add_grade(pieter_grade)
print(pieter.get_average())
