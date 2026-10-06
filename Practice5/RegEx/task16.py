import re

text = "Age: 18"

result = re.findall(r"\D", text)

print(result)