year = input("请输入年份：")
year = eval(year)
if year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0):
    print('这是闰年')
else:
    print('平年')

import random

nums = [random.randint(0, 50) for i in range(20)]
print(nums)
x = nums[::2]
x.sort(reverse=True)
nums[::2] = x
print(nums)

nums = [random.randint(0, 100) for i in range(50)]
print(nums)
i = len(nums) - 1
while i >= 0:
    if nums[i] % 2 == 1:
        del nums[i]
    i -= 1
print(nums)

x = input('input a num:')
x = eval(x)
t = x
i = 2
result = []
while True:
    if t == 1:
        break
    if t % i == 0:
        result.append(i)
        t /= i
    else:
        i += 1
print(x, '=', '*'.join(map(str, result)))

print(sum(range(1, 100)[::2]))

x = input('请输入一个值：')
x = eval(x)
if x < 0 or x >= 20:
    y = 0
elif 0 <= x < 5:
    y = x
elif 5 <= x < 10:
    y = 3 * x - 5
elif 10 <= x < 20:
    y = 0.5 * x - 2
print(y)
