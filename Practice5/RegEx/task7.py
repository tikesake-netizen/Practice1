import re

text = "I am learning Python"

result = re.findall("Python$", text)

print(result)