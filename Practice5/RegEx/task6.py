import re

text = "Python is easy. I like Python."

result = re.findall("Python", text)

print(result)