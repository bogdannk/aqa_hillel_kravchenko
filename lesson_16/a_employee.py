from abc import ABC, abstractmethod

class Employee(ABC):
    __name: str
    __salary: int | float

    def __init__(self, name: str, salary: int | float):
        self.__name = name
        self.__salary = salary

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

