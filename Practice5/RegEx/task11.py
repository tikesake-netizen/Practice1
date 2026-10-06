import re

text = "cat bat rat hat"

result = re.findall("[cr]at", text)

print(result)