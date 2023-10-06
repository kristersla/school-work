class School:
    
    def __init__(self, name, level, numberOfStudents):

        self.name= name
        self.level = level
        self.numberOfStudents = numberOfStudents

    def get_name(self):

        return self.name

    def get_level(self):

        return self.level
    
    def get_numberOfStudents(self):

        return self.numberOfStudents
    
    def set_numberOfStudents(self, new_student):

        self.numberOfStudents = new_student

    def __repr__(self):

        return f"A {self.level} school named {self.name} with {self.numberOfStudents} students. "

print(School("Rigas 64. vidusskola", "high", 889))

class PrimarySchool(School):
    
    def __init__(self, name, numberOfStudents, level = "Primary", pickupPolicy = "pickup after 3pm"):

        super().__init__(name, level, numberOfStudents)
        self.pickupPolicy = pickupPolicy

    def get_pickupPolicy(self):

        return self.pickupPolicy

    def __repr__(self):
        return super().__repr__() + f"Pickup Policy: {self.pickupPolicy}"

primary_school = PrimarySchool("Rigas 64. vidusskola", 889)
print(primary_school)

class MiddleSchool(School):

    def __init__(self, name, level, numberOfStudents):
        super().__init__(name, level, numberOfStudents)

class HighSchool(School):

    def __init__(self, name, level, numberOfStudents, sportTeams = ['basketball', 'tennis']):

        super().__init__(name, level, numberOfStudents)
        self.sportTeams = sportTeams
    
    def get_sportTeams(self):

        self.sportTeams

    def __repr__(self):
        return super().__repr__() + f"Sport teams: {self.sportTeams}"        


high_school = HighSchool("Rigas 64. vidusskola", "high", 889)
print(high_school)