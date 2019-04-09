# _1_10
x = input("Please input:")
try:
    x = int(x)
    if x >= 100:
        print(int(x // 100))
    else:
        print("请输入三位以上数字")
except BaseException:
    print("请输入数字")
