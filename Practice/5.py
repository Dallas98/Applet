# 判断一个数是否为素数
import math


def prime_number(number):
    if number <= 1:
        return '输入不正确'
    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            return True
    return False


