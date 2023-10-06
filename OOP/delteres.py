class Employee():
  new_id = 1
  def __init__(self, name=None):
    self.id = Employee.new_id
    Employee.new_id += 1
    self._name = name

  # Write your code below
  def get_name(self):
    return self._name

  def set_name(self, name):
    self._name = name

  def del_name(self):
    del self._name
  

e1 = Employee("Maisy")
e2 = Employee()