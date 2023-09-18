class Student:
    def __init__(self, year, name, attendance):
        self.name = name
        self.year = year
        self.grades = []
        self.attendance = attendance
    def add_grade(self, grade):
        if isinstance(grade, Grade):
            self.grades.append(grade)
    def get_average(self):
        total = sum(grade.score for grade in self.grades)
        return total / len(self.grades) if self.grades else 0

class Grade:
    minimum_passing = 65
    def __init__(self, score):
        self.score = score
    def is_passing(self):
        if self.score > self.minimum_passing:
            print(f"Score has passing score")

        
Roger = Student(10, "Roger van der Weyden", {"04062024": True})
Sandro = Student(12, "Sandro Botticelli", {"04062024": False})
Pieter = Student(8, "Pieter Bruegel the Elder", {"04062024": False})

grade1 = Grade(100)
Pieter.add_grade(grade1)
print(Pieter.get_average())

print(Pieter.is_passing())
    