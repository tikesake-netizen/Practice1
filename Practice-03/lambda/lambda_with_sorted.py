students = [
    ("Alex", 20),
    ("John", 18),
    ("Bob", 22)
]

result = sorted(students, key=lambda student: student[1])

print(result)