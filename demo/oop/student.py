class Student:
    # Class attribute / static attribute
    courses = {'Python': 8000, 'Java': 10000, 'AWS': 15000}
    count = 0

    @staticmethod      # Decorator
    def getcount():
        return Student.count

    # Constructor
    def __init__(self, name, course, feepaid=0):
        # Object attributes
        self.name = name
        self.course = course
        self.feepaid = feepaid
        Student.count += 1

        # Method

    def show(self):
        print("Name     :", self.name)
        print("Course   :", self.course)
        print("Feepaid  :", self.feepaid)

    def pay(self, amount):
        self.feepaid += amount

    def totalfee(self):
        return Student.courses[self.course]

    def due(self):
        return self.totalfee() - self.feepaid


s1 = Student("Scott", "Java", 5000)  # create object
s1.show()  # call method
print(s1.totalfee())
print(s1.due())
s2 = Student("Anders", "Python")
s2.pay(3000)
s2.pay(2000)

print(f"No. of students : {Student.getcount()}")
