import re

text = "Hello World, Python. RegEx"

result = re.sub(r"[ ,.]", ":", text)

print(result)