""" 二叉树实验 """


class BinaryTree:
    def __init__(self, value):
        self._left = None
        self._right = None
        self._data = value

    def insert_left_child(self, value):
        if self._left:
            print('left child tree already exists')
        else:
            self._left = BinaryTree(value)
            return self._left

    def insert_right_child(self, value):
        if self._right:
            print('right child tree already exists')
        else:
            self._right = BinaryTree(value)
            return self._right

    def show(self):
        print(self._data)

    # 先序遍历
    def pre_order(self):
        print(self._data)
        if self._left:
            self._left.pre_order()
        if self._right:
            self._right.pre_order()

    # 后序遍历
    def post_order(self):
        print(self._data)
        if self._left:
            self._left.post_order()
        if self._right:
            self._right.post_order()
        print(self._data)

    # 中序遍历
    def in_order(self):
        if self._left:
            self._left.in_order()
        print(self._data)
        if self._right:
            self._right.in_order()


if __name__ == '__main__':
    print('Please use me as a module')
