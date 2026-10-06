import re

text = "ct cat caat caaat"

result = re.findall("ca*t", text)

print(result)