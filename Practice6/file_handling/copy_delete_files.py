
import shutil
from pathlib import Path

source = Path("notes.txt")
backup = Path("notes_backup.txt")
copy = Path("notes_copy.txt")

if source.exists() and source.is_file():
    shutil.copy2(source, backup)
    shutil.copyfile(source, copy)
    print("Files copied successfully.")

if backup.exists():
    print("Backup size:", backup.stat().st_size, "bytes")

file_to_delete = Path("notes_copy.txt")

if file_to_delete.exists() and file_to_delete.is_file():
    if file_to_delete.stat().st_mode:
        file_to_delete.unlink()
        print("Copy deleted successfully.")
else:
    print("File does not exist.")