# 列表[]
import time

a = ['a', 'b', 'c', 'd']
a.reverse()
print(a)
a.sort()
print(a)
a.copy()
print(a)

result = []
start = time.time()
for i in range(100):
    result = result + [i]
print(len(result), ',', time.time() - start)

x = [None] * 2
x[0] = 1
print(x)
x = [[None] * 2] * 3
print(x)
x[1][1] = 5
print(x)

x = [1, 2, 1, 2, 1, 1, 1, 1]
print(x[::-1])
for i in x:
    if i == 1:
        x.remove(i)
print(x)
