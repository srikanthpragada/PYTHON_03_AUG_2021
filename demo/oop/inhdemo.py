from abc import ABC, abstractmethod


# Abstract class
class Doctor(ABC):
    def __init__(self, name, dept):
        self.__name = name
        self.__dept = dept

    @property
    def name(self):
        return self.__name

    @property
    def department(self):
        return self.__dept

    @abstractmethod
    def getsalary(self):
        pass


class ResidentDoctor(Doctor):
    def __init__(self, name, dept, salary):
        super().__init__(name, dept)
        self.salary = salary

    def getsalary(self):
        return self.salary


class Consultant(Doctor):
    def __init__(self, name, dept, visits, charge):
        super().__init__(name, dept)
        self.visits = visits
        self.charge = charge

    def getsalary(self):
        return self.visits * self.charge


c = Consultant("Dr. James", "Ped", 10, 1000)
print(c.name, c.department, c.getsalary())

print(isinstance(c, Consultant))
print(isinstance(10, int))
print(issubclass(ResidentDoctor, Doctor))
print(issubclass(ResidentDoctor, object))
print(ResidentDoctor.__bases__)

d = Doctor("Abc","Neuro")
