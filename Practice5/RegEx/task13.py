import re

text = "I like Python and Java"

result = re.findall("Python|Java", text)

print(result)