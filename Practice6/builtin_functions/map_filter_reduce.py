
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

total = reduce(lambda x, y: x + y, numbers)
print("Reduce sum:", total)

print("Length:", len(numbers))
print("Sum:", sum(numbers))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sorted descending:", sorted(numbers, reverse=True))

print("Integer:", int("123"))
print("Float:", float("12.5"))
print("String:", str(100))
print("Boolean:", bool(1))