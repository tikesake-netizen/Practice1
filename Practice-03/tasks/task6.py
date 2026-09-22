numbers = [2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13]

is_prime = lambda number: number > 1 and all(number % divisor != 0 for divisor in range(2, int(number ** 0.5) + 1))

prime_numbers = list(filter(is_prime, numbers))

print("Prime numbers:", prime_numbers)