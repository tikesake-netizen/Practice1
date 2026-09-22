def unique_elements(numbers):
    unique = []

    for number in numbers:
        if number not in unique:
            unique.append(number)

    return unique


numbers = [1, 2, 2, 3, 4, 4, 5, 1, 6]

print(unique_elements(numbers))