import re
s = 'What color / colour do you like?'

matches = re.finditer('colou?r',s)

for match in matches:
    print(match)