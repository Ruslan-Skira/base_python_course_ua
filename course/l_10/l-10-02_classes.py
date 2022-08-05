""" Лекция Классы 1"""


# Аналог классов
def MainCat():
    """Manufacture for producing cats"""
    color = 'black'

    def my_kitty(name, color=color):
        volume = '60db'
        ma_age = 20
        return f'my cat {name} is {color} sreaming {volume} live forever {ma_age}'

    return my_kitty


chernushok = MainCat()
chernushok('Chernushok', color='white')






# Синтаксис классов.







class Cat:
    """I'm increment one to the variable int"""
    pows = 4  # атрибут класса
    weight = 3

    def __init__(self, name, color='black', home='Village'):  # конструктор
        self.name = name  # Запись атрибута
        self.color = color
        self.home = home
        self.mood = True

    # def home_cat(self):
    #     self.home = 'flat'
    #
    # def irritating(self):
    #     self.mood = False


"""Классы являются по сути фабриками по созданию объектов, со своими областями видимости. 
фактически ООП сводиться к object.attribute"""

mycat = Cat('name')
file_my = open('temp.txt', 'w')
print(mycat.__dict__, file=file_my)
print(vars(mycat), file=file_my)
file_my.close()



print(mycat.__class__)


# TODO create class Counter with methods increment(value plus one), get_value(return value)
class Counter:
    """Counter from zero or your value"""
    def __init__(self, initial=0):
        """конструктор"""
        self.value = initial  #аттрибути екз классу

    def increment(self):
        self.value += 1

    def get_value(self):
        return self.value


counter = Counter(2)
counter.increment()
counter.get_value()

# Создадим класс который хранит количество всех своих экземпляров и своих экземлпяров

class Dog:
    all_dogs_counter = 0  # атрибут класса
    all_dogs = []

    def __init__(self):
        Dog.all_dogs_counter += 1  # атрибут экземпляра класса
        Dog.all_dogs.append(self)


""" Модификаторы доступа
1. публичные и приватные 
"""

class BankAccount:
    """Class for all bank classes"""
    bank_name_main: str = 'Main bank'
    _bank_vip_adress_main: str = 'moon'
    __bank_owner_big_boss: str = 'Ops'


privat = BankAccount()

print(privat.bank_name_main)

print(privat._bank_vip_adress_main)


print(privat.__bank_owner_big_boss)  # Nope it is secret


print(privat._BankAccount__bank_owner_big_boss)




# print(BankAccount.__doc__)
#
# print(BankAccount.__name__)
print(BankAccount.__module__)
print(BankAccount.__bases__)
privat.__class__


BankAccount.__dict__   # словарь атрибутов класса

privat.__dict__  # словарь атрибутов экземпляра класса

# vars and __dict__ the same

"""__slots__ фиксирует какие атрибуты доступны
"""

class A:
    __slots__ = ["name", "sername"]

a = A()
a.name = 'N'
a.sername = 'S'
a.midle_name = 'Nope'  #AttributeError
a.__dict__  # Error







