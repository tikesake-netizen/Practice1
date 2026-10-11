
import os
from pathlib import Path

base = Path("data")
nested = base / "documents" / "reports"

nested.mkdir(parents=True, exist_ok=True)

(base / "example.txt").write_text("Sample file", encoding="utf-8")
(nested / "report.txt").write_text("Sample report", encoding="utf-8")

print("Current directory:", os.getcwd())
print("Directory contents:", os.listdir(base))

print("Directories:")
for item in base.iterdir():
    if item.is_dir():
        print(item)

print("Files:")
for item in base.rglob("*"):
    if item.is_file():
        print(item)

print("Text files:")
for item in base.rglob("*.txt"):
    print(item)

print("Exists:", base.exists())
print("Readable:", os.access(base, os.R_OK))
print("Writable:", os.access(base, os.W_OK))
print("Executable:", os.access(base, os.X_OK))

print("Filename:", nested.name)
print("Parent directory:", nested.parent)

os.makedirs("data/extra/folder", exist_ok=True)