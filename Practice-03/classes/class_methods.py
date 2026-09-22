class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)

    def study(self, subject):
        print(self.name, "is studying", subject)


student = Student("Alex")
student.greet()
student.study("Python")