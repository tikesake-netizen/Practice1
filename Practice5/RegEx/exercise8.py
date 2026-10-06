import re

text = "HelloWorldPythonProgramming"

result = re.split(r"(?=[A-Z])", text)

result = [word for word in result if word]

print(result)