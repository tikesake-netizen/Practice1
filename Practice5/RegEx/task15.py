import re

text = "My age is 18 and my brother is 20."

result = re.findall(r"\d", text)

print(result)