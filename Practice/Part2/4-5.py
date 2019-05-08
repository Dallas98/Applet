import re

string = input("Please input a string:")
pattern = re.compile(r'\b[a-zA-Z]{3}\b')
print(set(pattern.findall(string)))
