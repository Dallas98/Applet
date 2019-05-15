from

class Customer(object):
    def __init__(self):
        pass

    def place_order(self, employee, food_name, number):
        if not isinstance(employee, Employee):
