
names = ["Ali", "Dana", "Arman"]
grades = [90, 85, 95]

print("Students with indexes:")
for index, name in enumerate(names, start=1):
    print(index, name)

print("Names and grades:")
for name, grade in zip(names, grades):
    print(name, grade)

students = dict(zip(names, grades))
print("Student dictionary:", students)

print("Total students:", len(names))
print("Average grade:", sum(grades) / len(grades))