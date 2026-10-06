import re

text = "Hello hello World WORLD Python python Test test"

result = re.findall(r"\b[A-Z][a-z]+\b", text)

print(result)