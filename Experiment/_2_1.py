import math

k = 0
x = 0
print(x)
for k in range(1000):
    x += math.factorial(4 * k) * (1103 + 26390 * k) / (pow(math.factorial(k), 4) * pow(396, 4 * k))
x *= (2 * math.sqrt(2) / 9801)
x = 1 / x
print(x)
print(math.pi)
