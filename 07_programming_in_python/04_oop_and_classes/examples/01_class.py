class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def passed(self):
        return self.score >= 50

student = Student("Ahsan", 91)
print(student.name)
print(student.passed())
