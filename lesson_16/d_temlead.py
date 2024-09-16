from lesson_16.b_manager import Manager
from lesson_16.c_test_engineer import TestEngineer

class TeamLead(Manager, TestEngineer):

    __team_size: int

    def __init__(self, name: str, salary: int | float, department: str, team_size: int):
        super().__init__(name, salary, department)
        self.__team_size = team_size

    @property
    def team_size(self):
        return self.__team_size


