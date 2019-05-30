from Experiment.OrderingSystem.Food import Food


class Employee(object):
    def __init__(self, name=''):
        self.__name = name

    def get_employee_name(self):
        return self.__name

    def take_order(self, name='', number=''):
        if not isinstance(number, int):
            print('请输入数字')
            return
        if number <= 0:
            raise Exception('数量不能为负')
        food_order = Food(name, number)
        return food_order
