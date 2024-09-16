from lesson_16.a_employee import Employee

class Manager(Employee):

    __department: str

    def __init__(self, name: str, salary: int | float, department: str):
        super().__init__(name, salary)
        self.__department = department

    @property
    def department(self):
        return self.__department

