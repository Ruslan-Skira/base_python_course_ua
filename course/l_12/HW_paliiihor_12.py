from functools import reduce

"""Задача 1 10 баллов:
Написать 3 примера генераторных функций с различными последовательностями."""


def generator1():
    print("HW 2,3")
    yield "Monday"
    print("HW 4,7")
    yield "Tuesday"
    print("HW  exercises 123,7")
    yield "Wednesday"
    print("HW Free")
    yield "Thursday "
    print("HW Free")
    yield "Friday "
    print("HW Free")
    yield "Saturday"
    print("HW Free")
    yield "Sunday"


g1 = generator1()
try:
    print(next(g1))
    print(next(g1))
    print(next(g1))
    print(next(g1))
    print(next(g1))
    print(next(g1))
    print(next(g1))
    print(next(g1))
except StopIteration as s:
    print(s,"Week is finished")


def generator2():
    a = 0
    while a != 10:
        yield a + 1
        a += 1


g2 = generator2()
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))

g3 = (x for x in range(1, 10))
print(next(g3))
print(next(g3))
print(next(g3))
print(next(g3))

"""Задача 2 10 баллов:
Написать свою реализацию функции reduce() с описанием ее работы в однострочных и многострочных комментариях.
def my_reduce(): моя реализация. (постарайтесь по памяти реализовать.)"""


def funk_reduce(a, b):
    return (a + b) ** b


progression = reduce(funk_reduce, (1, 2, 3, 4, 5, 6))
print(progression)

factor_six = (1, 2, 3, 4, 5, 6)
factor = reduce(lambda a, b: a * b, factor_six)
print(factor)

user = reduce(lambda a, b: a.upper() + b, ("p", "a", "l", "i", "i"), "ihor ")
print(user)

"""Задача 3 30 баллов:
Написать функцию которая с помощью assert будет тестировать ваш самопистный reduce"""
def x2(*args):
    assert len(args) >= 5, "Слишком мало аргументов!" # Операнд > не в ту сторону повернут у вас бЬIл, для срабатования логики, assert вЬIзЬIвается когда False?
    return args[4]


def funk_reduce(a, b):
    assert isinstance(a,int) and isinstance(b,int) , " Только int"
    return (a + b) ** b

#print(x2(1,2,3))
#progression2 = reduce(funk_reduce, ("p", "a", "l", "i", "i"))
#print(progression2)

"""**Задача 4. 30 баллов:** 
Збудувати класс з методом котрий повертає всі атрибути єкземпляра класса.
В конструкторі __init__ вашого класу зробити довільну реалізацію.
"""
class Human:
    def __init__(self,age,gender,color,special=None):
        self.age=age
        self.gender=gender
        self.color=color
        self.spesial=special

adam=Human(25,'male','white','protect')
eva=Human(23,'female','black','cook')
print(eva.__dict__)
print(adam.__dict__)

"""Задача 5. 20 баллов. Пройти тест
https://holypython.com/advanced-python-exercises/exercise-4-classes/
Exercise 4-c: Jet Fighter Instances  -> Прошол"""
