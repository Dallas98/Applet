file = open('4-1.txt', 'r')
string = file.read()
file.close()
print(string)
string = string.replace('i ', 'I ')
string = string.replace(' i ', ' I ')
print(string)