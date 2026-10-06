import re

text = "ab abb abbb abbbb ac a"

result = re.findall(r"ab{2,3}", text)

print(result)