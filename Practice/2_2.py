import random

print([3] in [1, 2, 3, 4])

x = [random.randint(0, 100) for i in range(1000)]
d = set(x)
for num in d:
    print(num, ':', x.count(num))

x = input('请输入一个列表：')
x = eval(x)
start, stop = eval(input('请输入开始与结束下标：'))
print(x[start:stop + 1])

keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]
dictionary = dict(zip(keys, values))
key = input("Please input a key:")
key = eval(key)
print(dictionary.get(key, '您输入的键不存在'))


import random
x = [random.randint(0, 100) for i in range(20)]
print(x)
y = x[0:10]
y.sort()
x[0:10] = y
y = x[10:20]
y.sort(reverse=True)
x[10:20] = y
print(x)
