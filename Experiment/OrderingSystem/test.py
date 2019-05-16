import tkinter
import tkinter.messagebox
from tkinter.messagebox import askyesno
import tkinter.ttk
#from Experiment.OrderingSystem import Customer, Employee, Lunch

employees = ['商家1', '商家2', '商家3']

flag = False


class Customer():
    def __init__(self, name='Andy', namelist=[], numlist=[]):
        self.__name = name
        self.__namelist = namelist
        self.__numlist = numlist

    def getn(self):
        return self.__name

    def placeOrder(self, employee, name, number):
        if not isinstance(employee, Employee):
            raise Exception('information wrong')
        nf = employee.takeOrder(name, number)
        self.__namelist.append(name)
        self.__numlist.append(number)
        return nf

    def printOrder(self):
        result = []
        for i in range(len(self.__namelist)):
            tp = []
            tp.append(self.__namelist[i])
            tp.append(':')
            tp.append(self.__numlist[i])
            result.append(''.join(tp))
        return result


class Employee():
    def __init__(self, name='Nobody'):
        self.__name = name

    def getn(self):
        return self.__name

    def takeOrder(self, name='', number=''):
        if number.isdigit() == False:
            raise Exception('information wrong')
        num = int(number)
        if num <= 0:
            raise Exception('information wrong')
        newfood = Food(name, num)
        return newfood


class Food():
    def __init__(self, name='unknown', num=1):
        self.__name = name
        self.__num = num

    @classmethod
    def getfood(cls):
        return ['京酱肉丝', '番茄炒蛋', '黄焖鸡', '水煮鱼']

    def show(self):
        for i in self.__foodlist:
            print(i.__name, ' : ', i.__num)

    def getname(self):
        return self.__name

    def getnum(self):
        return self.__num


class Lunch():
    def __init__(self, customer=Customer(), employee=Employee()):
        if not isinstance(customer, Customer) or not isinstance(employee, Employee):
            raise Exception('customer or employee wrong')
        self.__customer = customer
        self.__employee = employee

    def gete(self):
        return self.__employee

    def getc(self):
        return self.__customer

    def order(self, name, number):
        self.__customer.placeOrder(self.__employee, name, number)

    def result(self):
        return '\n'.join(self.__customer.printOrder())


def Start():
    global mylunch
    customer = Customer(entryC.get())
    employee = Employee(entryE.get())
    mylunch = Lunch(customer, employee)
    root.destroy()
    menu()


def menu():
    def Order():
        name = entryName.get()
        num = entryNum.get()
        c = mylunch.getc().getn()
        e = mylunch.gete().getn()
        if askyesno(e, c+'：您确定下单?'):
            flag = True
        else:
            flag = False
        if flag:
            try:
                mylunch.order(name, num)
                tkinter.messagebox.showinfo(title='订单信息', message='成功')
            except:
                tkinter.messagebox.showinfo(title='订单信息', message='失败')
        else:
            tkinter.messagebox.showinfo(title='订单信息', message='失败')
        varName.set('')
        varNum.set('')

    def Print():
        text.set(mylunch.result())

    Menu = tkinter.Tk()
    Menu.title('菜单')
    Menu['height'] = 400
    Menu['width'] = 400
    text = tkinter.StringVar(value='')
    varName = tkinter.StringVar(value='')
    varNum = tkinter.StringVar(value='')
    labelName = tkinter.Label(Menu, text='菜名:', justify=tkinter.RIGHT, width=80)
    labelName.place(x=30, y=30, width=100, height=50)
    # entryName = tkinter.Entry(Menu, width=100, textvariable=varName)
    entryName = tkinter.ttk.Combobox(Menu, values=tuple(Food.getfood()), width=100)
    entryName.place(x=150, y=30, width=200, height=50)
    labelNum = tkinter.Label(Menu, text='数量:', justify=tkinter.RIGHT, width=80)
    labelNum.place(x=30, y=100, width=100, height=50)
    entryNum = tkinter.Entry(Menu, width=100, textvariable=varNum)
    entryNum.place(x=150, y=100, width=200, height=50)
    button1 = tkinter.Button(Menu, text='下单', command=Order)
    button1.place(x=50, y=170, width=50, height=50)
    button2 = tkinter.Button(Menu, text='打印', command=Print)
    button2.place(x=300, y=170, width=50, height=50)
    t = tkinter.Label(Menu, textvariable=text, height=50, width=100)
    t.place(x=150, y=250, height=100, width=100)
    Menu.mainloop()


root = tkinter.Tk()
root.title('欢迎')
root['height'] = 400
root['width'] = 400
CustomerName = tkinter.StringVar(value='')
labelC = tkinter.Label(root, text='顾客:', justify=tkinter.RIGHT, width=50)
labelC.place(x=30, y=30, width=100, height=50)
entryC = tkinter.Entry(root, width=100, textvariable=CustomerName)
entryC.place(x=150, y=30, width=200, height=50)
labelE = tkinter.Label(root, text='商家:', justify=tkinter.RIGHT, width=50)
labelE.place(x=30, y=100, width=100, height=50)
entryE = tkinter.ttk.Combobox(root, values=tuple(employees), width=100)
entryE.place(x=150, y=100, width=200, height=50)
StartLunch = tkinter.Button(root, text='点餐', command=Start)
StartLunch.place(x=150, y=250, height=100, width=100)
root.mainloop()
