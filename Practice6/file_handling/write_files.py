
from pathlib import Path

file_path = Path("notes.txt")

with open(file_path, "w", encoding="utf-8") as file:
    file.write("First line\n")
    file.write("Second line\n")

with open(file_path, "a", encoding="utf-8") as file:
    file.write("Third line\n")

with open(file_path, "r", encoding="utf-8") as file:
    print(file.read())

numbers = [10, 20, 30, 40, 50]
with open("numbers.txt", "w", encoding="utf-8") as file:
    file.writelines(f"{number}\n" for number in numbers)

print("Files created successfully.")