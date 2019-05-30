class Food(object):
    def __init__(self, name='', number=1):
        self.__name = name
        self.__number = number

    def show_menu(self):
        for i in self.__food_list:
            print(i.__name, ': ', i.__number)

    def get_food_name(self):
        return self.__name

    def get_food_number(self):
        return self.__number
