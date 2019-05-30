from Experiment.OrderingSystem.Employee import Employee


class Customer(object):
    def __init__(self, customer_name, name_list, number_list):
        self.__name = customer_name
        self.__name_list = name_list
        self.__number_list = number_list

    def get_customer_name(self):
        return self.__name

    def place_order(self, employee, food_name, number):
        if not isinstance(employee, Employee):
            print('参数错误')
            return
        menu = employee.take_order(food_name, number)
        self.__name_list.append(food_name)
        self.__number_list.append(number)
        return menu

    def print_order(self):
        result = []
        for i in range(len(self.__name_list)):
            temp = []
            temp.append(self.__name_list[i])
            temp.append(':')
            temp.append(self.__number_list[i])
            result.append(''.join(temp))
        return result
