
from pathlib import Path

file_path = Path("sample.txt")

file_path.write_text("Hello, Python!\nThis is Practice 6.\nThird line.", encoding="utf-8")

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

with open(file_path, "r", encoding="utf-8") as file:
    print(file.readline())

with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()
    print(lines)