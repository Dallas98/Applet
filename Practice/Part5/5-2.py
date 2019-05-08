import math


def is_prime(number):
    n = int(math.sqrt(number) + 1)
    for i in range(2, n):
        if (number % i) == 0:
            return 'NO'
    else:
        return 'YES'


