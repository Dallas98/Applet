def demo(newitem, old_list=None):
    if old_list is None:
        old_list = []
    old_list.append(newitem)
    return old_list


def demo1(newitem, old_list=[]):
    old_list.append(newitem)
    return old_list


print(demo1('5', [1, 2, 3, 4]))
print(demo1('aaa', ['a', 'b']))
print(demo1('a'))
print(demo1('b'))
