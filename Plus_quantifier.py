import re
s = "Python 3.10 was released in 2021"

matches = re.finditer('\d+',s)

for match in matches:
    print(match)