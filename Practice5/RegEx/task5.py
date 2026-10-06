import re

text = "cat cot cut"

result = re.findall("c.t", text)

print(result)