class Animal:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def show_breed(self):
        print("My breed is", self.breed)


dog = Dog("Buddy", "Labrador")
dog.introduce()
dog.show_breed()