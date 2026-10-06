import re

text = "color colour colr"

result = re.findall("colou?r", text)

print(result)