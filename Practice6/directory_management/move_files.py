
import shutil
from pathlib import Path

source_dir = Path("data")
target_dir = Path("data/moved")
target_dir.mkdir(parents=True, exist_ok=True)

source_file = source_dir / "example.txt"

if source_file.exists():
    destination = target_dir / source_file.name
    shutil.copy2(source_file, destination)
    print("File copied to:", destination)

for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    Path(f"data/{letter}.txt").touch(exist_ok=True)

print("Created 26 letter files.")

for item in source_dir.iterdir():
    if item.is_file():
        print(item.name)

print("All operations completed.")