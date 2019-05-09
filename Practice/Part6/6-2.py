import math


class Vecter:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        temp = Vecter()
        temp.x = self.x + other.x
        temp.y = self.y + other.y
        temp.z = self.z + other.z
        return temp

    def __sub__(self, other):
        temp = Vecter()
        temp.x = self.x - other.x
        temp.y = self.y - other.y
        temp.z = self.z - other.z
        return temp

    def __mul__(self, other):
        temp = Vecter()
        temp.x = self.x * other
        temp.y = self.y * other
        temp.z = self.z * other
        return temp

    def __truediv__(self, other):
        temp = Vecter()
        temp.x = self.x / other
        temp.y = self.y / other
        temp.z = self.z / other
        return temp

    @classmethod
    def dot_product(cls, self, other):
        temp = self.x * other.x + self.y * other.y + self.z * other.z
        return temp

    @classmethod
    def vector_product(cls, self, other):
        temp = Vecter()
        temp.x = self.y * other.z - other.y * self.z
        temp.y = -(self.x * other.z - other.x * self.z)
        temp.z = self.x * other.y - other.x * self.y
        return temp

    @classmethod
    def module(cls, self):
        temp = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        return temp

    @classmethod
    def vector_angle(cls, self, other):
        module1 = Vecter.module(self)
        module2 = Vecter.module(other)
        x = math.acos(Vecter.dot_product(self, other)
                      / (module1 * module2))
        return x

    def show(self, str=''):
        print(str, (self.x, self.y, self.z))


if __name__ == '__main__':
    v1 = Vecter(0, 2, 0)
    v2 = Vecter(0, -7, 0)
    v1.show('v1:')
    v2.show('v2:')
    v3 = v1 + v2
    v3.show('向量和：')
    v3 = v1 - v2
    v3.show('向量差：')
    v3 = v1 * 3
    v3.show('数乘：')
    v3 = v2 / 2
    v3.show('数除：')
    v3 = Vecter.vector_product(v1, v2)
    v3.show('向量积：')
    print('数量积：', Vecter.dot_product(v1, v2))
    print('向量夹角：', Vecter.vector_angle(v1, v2))
