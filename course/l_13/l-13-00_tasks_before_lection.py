# Eще один вариант
"""Инициализация (от англ. initialization, инициирование)  создание, активация, подготовка к работе, определение параметров.
 Приведение программы или устройства в состояние готовности к использованию
 Приведение областей памяти в состояние, исходное для последующей обработки или размещения данных. [ГОСТ 19781 90]
 """


def f():
    return 1


def f1():
    return f()


x = f1()




# TODO: способы вызова метода из объекта и почему в селф ничего не передаем
class T:
    def look(self):
        print(f'{T.__name__}')

    def __str__(self):
        return 'here will be smt interesting'


# V1
t = T()
t.look()

# V2
t2 = T()
t2.__class__.look(t2)
print(f'{t}')


# TODO: show difference attribute class and attribute instance
class T():
    move = 'wtf is going here'  # Атрибут класса

    def __init__(self):
        self.move = 123  # Атрибут экземпляра класса


t = T()

print(t.move)

print(T.move)


#

# TODO: Атрибуты
class Counter_my(object):
    all_counters = []

    def __init__(self, initial_count=0):
        Counter_my.all_counters.append(self)
        self.count = initial_count


c1 = Counter_my(2)
c2 = Counter_my(3)
assert len(Counter_my.all_counters) == 2
assert c1.all_counters is c2.all_counters


# TODO: Напишите свой класс родителя и ребенка и показать на примере инита
#  как c помощью 'super' дописать в коструктор атрибут экземпляра класса. т.е. self


class T:
    def __init__(self):
        self.move = 'move'


class B(T):
    __slots__ = ['attribute_of_my_object']

    def __init__(self):
        super(B, self).__init__()  # python 2
        self.move_fast = 'move_very_fast'


b = B()

print(b.move_fast)
print(b.move)
