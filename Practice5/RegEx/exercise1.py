import re

text = "a ab abb abbb ac"

result = re.findall(r"ab*", text)

print(result)