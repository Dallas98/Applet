from collections import Counter

cnt = Counter()

for word in open("F:\\大三\\春季学期\\Python\\实验\\EXP2\\words.txt", 'r'):
    cnt[word] += 1
print(cnt)

dic = {}
f = open("F:\\大三\\春季学期\\Python\\实验\\EXP2\\words.txt", 'r')
file = f.read()
text = ""
f.close()
for x in file:
    if (x == '\n' or x == ',' or x == '.' or x == ';' or x == '?'):
        text += ' '
    else:
        text += x
list1 = text.split(" ")
i = 0
length = len(list1)
while (i < length):
    if (list1[i].isalnum() == False or list1[i] == ""):
        list1.pop(i)
        length -= 1
    else:
        i += 1
for word in list1:
    if word not in dic.keys():
        dic[word] = 1
    else:
        dic[word] = dic.pop(word) + 1
for word in dic.keys():
    print(word + ":%d" % (dic[word]))
