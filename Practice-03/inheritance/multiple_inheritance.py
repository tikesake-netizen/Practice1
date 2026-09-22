class Father:
    def father_method(self):
        print("This is a method from Father")


class Mother:
    def mother_method(self):
        print("This is a method from Mother")


class Child(Father, Mother):
    def child_method(self):
        print("This is a method from Child")


child = Child()

child.father_method()
child.mother_method()
child.child_method()