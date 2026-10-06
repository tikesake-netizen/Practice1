import re

text = "hello_world Python_Code my_name test123 hello_world"

result = re.findall(r"\b[a-z]+_[a-z]+\b", text)

print(result)