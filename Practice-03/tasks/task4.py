import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Coordinates:", self.x, self.y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point):
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)


point1 = Point(2, 3)
point2 = Point(5, 7)

point1.show()

point1.move(4, 6)
point1.show()

print("Distance:", point1.dist(point2))