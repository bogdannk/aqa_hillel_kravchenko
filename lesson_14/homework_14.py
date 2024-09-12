class Student:

    def __init__(self, first_name: str, last_name: str, age: int, average_grade: int | float):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self._average_grade = average_grade

    def update_average_grade(self, new_average_grade):
        if new_average_grade > 100:
            raise ValueError("You have entered an incorrect average grade point average, it cannot be more than 100,"
                             " try again.")
        else:
            self._average_grade = new_average_grade

    def student_info_output(self):
        print(f"Student {self.first_name} {self.last_name} is {self.age} years old "
              f"and has a grade point average of {self._average_grade}")


"""Create an object of class"""
first_student: Student = Student("Bogdan", "Kravchenko", 36, 98)
first_student.student_info_output()  # Student Bogdan Kravchenko is 36 years old and has a grade point average of 98

"""Updating a student's grade point average"""
first_student.update_average_grade(99)
first_student.student_info_output()  # Student Bogdan Kravchenko is 36 years old and has a grade point average of 99
