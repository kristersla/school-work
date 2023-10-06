class Employee:
    def __init__(self):
        self.id = None
        self._id = 10
        self.__id = 100


e = Employee()

print(dir(e))

    