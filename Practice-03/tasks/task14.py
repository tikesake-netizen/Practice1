import math


def sphere_volume(radius):
    return (4 / 3) * math.pi * radius ** 3


radius = float(input("Enter radius: "))

print("Volume:", sphere_volume(radius))