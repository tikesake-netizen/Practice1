class Shape:
    def __init__(self):
        self.area = 0


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def calculate_area(self):
        self.area = self.length * self.width
        print("Area:", self.area)


rectangle = Rectangle(10, 5)
rectangle.calculate_area()