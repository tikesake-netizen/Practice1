import re

text = "Hello_123!"

result = re.findall(r"\W", text)

print(result)