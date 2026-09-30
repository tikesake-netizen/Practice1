def squares(n):
    for i in range(n + 1):
        yield i ** 2


for number in squares(5):
    print(number)


n = int(input("Enter n: "))

even_numbers = (str(i) for i in range(n + 1) if i % 2 == 0)

print(",".join(even_numbers))



def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


print("Numbers divisible by 3 and 4:")

for number in divisible_by_3_and_4(50):
    print(number)


def squares_range(a, b):
    for i in range(a, b + 1):
        yield i ** 2


print("Squares from a to b:")

for number in squares_range(2, 6):
    print(number)



def countdown(n):
    while n >= 0:
        yield n
        n -= 1


print("Countdown:")

for number in countdown(5):
    print(number)