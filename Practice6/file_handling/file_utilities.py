
import os
import shutil
from pathlib import Path

path = Path("notes.txt")

print("Path exists:", path.exists())

if path.exists():
    print("Filename:", path.name)
    print("Parent:", path.parent)
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

    with open(path, "r", encoding="utf-8") as file:
        line_count = sum(1 for line in file)

    print("Number of lines:", line_count)

    shutil.copy2(path, "notes_extra_backup.txt")

items = ["Apple", "Banana", "Orange"]

with open("fruits.txt", "w", encoding="utf-8") as file:
    file.writelines(item + "\n" for item in items)

source = Path("notes_extra_backup.txt")
destination = Path("notes_extra_copy.txt")

if source.exists() and source.is_file():
    shutil.copyfile(source, destination)
    print("Content copied successfully.")

delete_path = Path("notes_extra_copy.txt")

if delete_path.exists() and delete_path.is_file():
    if os.access(delete_path, os.W_OK):
        delete_path.unlink()
        print("File deleted successfully.")
else:
    print("Nothing to delete.")