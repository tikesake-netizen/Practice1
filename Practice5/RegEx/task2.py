import re

text = "I like Python. Python is easy. I use Python every day."

result = re.findall("Python", text)

print(result)