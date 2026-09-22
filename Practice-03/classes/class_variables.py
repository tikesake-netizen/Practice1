class Student:
    university = "KBTU"

    def __init__(self, name):
        self.name = name


student1 = Student("Alex")
student2 = Student("John")

print(student1.name)
print(student2.name)
print(Student.university)