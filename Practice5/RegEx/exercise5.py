import re

texts = ["ab", "a123b", "abb", "cab", "abc"]

for text in texts:
    if re.match(r"^a.*b$", text):
        print(text, "YES")
    else:
        print(text, "NO")