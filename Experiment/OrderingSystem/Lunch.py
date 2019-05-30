from Experiment.OrderingSystem import Customer, Employee

class Lunch(object):
    def __init__(self, customer=Customer(), employee=Employee()):
        if not isinstance(customer, Customer) or not isinstance(employee, Employee):
            print('对象错误')
            return
        self.__customer = customer
        self.__employee = employee

    def get_employee(self):
        return self.__employee

    def get_customer(self):
        return self.__customer

    def order(self, name, number):
        self.__customer.place_order(self.__employee, name, number)

    def result(self):
        return '\n'.join(self.__customer.print_order())
