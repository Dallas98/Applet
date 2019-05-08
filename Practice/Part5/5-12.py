def Sorted(array):
    Array = array[::]
    r = []
    while Array:
        m = min(Array)
        r.append(m)
        Array.remove(m)
    return r


x = [1, 6, 3, 8, 4, 9]
print(Sorted(x))

