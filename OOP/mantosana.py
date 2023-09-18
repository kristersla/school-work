class Employee:
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        return f", my id is {self.id}."

class Admin(Employee):

    def say_id(self):
        
        id_num = super().say_id()
        print(f"I am an admin{id_num}")

class Manager(Admin):
    def say_id(self):
        print("I'm a manager!")
        super().say_id()

e1 = Employee()
e2 = Employee()
e3 = Admin()
e4 = Manager()

e3.say_id()
e4.say_id()