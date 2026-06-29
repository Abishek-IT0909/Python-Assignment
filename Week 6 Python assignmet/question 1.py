class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


s1 = Student("Abishek", 20, [90,95,98])
s2 = Student("Ankit", 21, [70, 60, 80])
s3 = Student("Anish", 19, [82,88, 91])
print(s1.average_grade())
print(s2.average_grade())
print(s3.average_grade())