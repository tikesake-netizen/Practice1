import re

text = "ha haha hahaha ho hoho"

result = re.findall(r"(ha)+", text)

print(result)