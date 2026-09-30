import sys

current_folder = sys.path[0]
sys.path.pop(0)

import math

sys.path.insert(0, current_folder)


degree = float(input("Input degree: "))

radian = degree * math.pi / 180

print("Output radian:", radian)


height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = (base1 + base2) * height / 2

print("Expected Output:", area)


sides = int(input("Input number of sides: "))
side = float(input("Input the length of a side: "))

area = (sides * side ** 2) / (4 * math.tan(math.pi / sides))

print("The area of the polygon is:", area)


base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = base * height

print("Expected Output:", area)