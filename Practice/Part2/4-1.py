a = '1234'
b = '1234'
print(id(a) == id(b))
a = '1234' * 10000
b = '1234' * 10000
print(id(a) == id(b))


file = open('4-1.txt', 'r')
string = file.read()
file.close()
print(string)
string = string.replace('i ', 'I ')
string = string.replace(' i ', ' I ')
print(string)
