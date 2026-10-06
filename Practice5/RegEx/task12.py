import re

text = "cat caat caaat caaaat"

result = re.findall("ca{2}t", text)

print(result)