import re

text = "HelloWorldPythonProgramming"

result = re.sub(r"(?<!^)([A-Z])", r" \1", text)

print(result)