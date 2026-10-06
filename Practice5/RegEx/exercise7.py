import re

text = "hello_world my_name python_programming"

result = re.sub(r"_([a-z])", lambda m: m.group(1).upper(), text)

print(result)