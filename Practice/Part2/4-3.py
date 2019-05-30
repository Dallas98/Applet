import re

string = 'This is is is a a desk desk'
pattern = re.compile(r'(?P<f>\b\w+\b)\s(?P=f)')
while True:
    match = pattern.search(string)
    if match:
        string = string.replace(match.group(0), match.group(1))
    else:
        break
print(string)
