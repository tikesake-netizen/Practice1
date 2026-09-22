class Shape:
    def __init__(self):
        self.area = 0

    def calculate_area(self):
        print("Area:", self.area)


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def calculate_area(self):
        self.area = self.length * self.length
        print("Area:", self.area)


square = Square(5)
square.calculate_area()