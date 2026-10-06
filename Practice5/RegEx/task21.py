import re

text = "cat category scatter cat"

result = re.findall(r"\bcat\b", text)

print(result)