import re

file = open('4-2.txt', 'r')
string = file.read()
file.close()
print(string)
pattern = re.compile(r'(?:[\w])I(?:[\w.])')
while True:
    result = pattern.search(string)
    if result:
        if result.start(0) != 0:
            string = string[:result.start(0) + 1] + 'i' + string[result.end(0) - 1:]
        else:
            string = string[:result.start(0)] + 'i' + string[result.end(0) - 1:]
    else:
        break
print(string)
