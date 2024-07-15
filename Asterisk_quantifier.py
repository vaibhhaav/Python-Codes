import re

s = """ CPython, IronPython, and JPython ae major Python's implementation"""
matches = re.finditer('\w*Python',s)

for match in matches:
    print(match)