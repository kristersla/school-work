class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class User:
  def __init__(self, username, role="Customer"):
    self.username = username
    self.role = role

  def say_user_info(self):
    print(f"my username is {self.username} and my role is {self.role}")

# Write your code below
class Admin(Employee, User):
  def __init__(self):
    super().__init__()
    User.__init__(self, self.id, "Admin")

  def say_id(self):
    super().say_id()
    print("I am an admin.")

class Manager(Admin):
    def say_id(self):
        print("I'm a manager!")
        super().say_id()

admin = Admin()
employee = Employee()
manager = Manager()

meeting = [employee, admin, manager]
for i in meeting:
  i.say_id()
  

# e1 = Employee()
# e2 = Employee()
# e3 = Admin()

# e3.say_user_info()