import re

text = "Hello_123!"

result = re.findall(r"\w", text)

print(result)