''' Closures
замыкания это функция вместе с привязанными к ней совокупностью данных.
замыкание это функция внутри которой(в теле ), есть ссылки на переменные которые были объявленные вне ее тела.
 '''

a = 1  # TODO: question Сколько объектов сколько переменных?
b = a

#### Пример с котиком, замыкание. ###
"""Задание написать функцию которая внутри будет содержать другую функции и возвращать ее объект.
Внешняя функция содержит переменную словарь с данными. А внутренняя функция его расширяет."""


def base_cat():
    cat_base_data: dict = {'pow': 4, 'weight': 3}

    def my_cat(color):
        cat_base_data['color'] = color

        return cat_base_data

    return my_cat


print(base_cat()('red'))





"""Задание написать 2 функции одна возвращает слово гав другая мяю"""


def decor_animal(function_internal):
    function = function_internal
    x= 1
    def wrapper():
        result = function()
        y = x+ 2
        if result == 'May':
            print('Cat')
        elif result == 'Gav':
            print("dog")
        else:
            print('Beast')
        return result

    return wrapper


@decor_animal
def cat():
    return 'May'


def dog():
    return 'Gav'


print(cat())


def wrapper_my(function):
    result = function()
    if result == 'May':
        print('Cat')
    elif result == 'Gav':
        print("dog")
    else:
        print('Beast')


def outer_func():
    car_list = ['moskvich', 'rollseroyce', 'bentley']  # enclosing for inner_func

    def inner_func():
        print('%s and it adres %s' % (car_list, id(car_list)))

    return inner_func


outter_func_first = outer_func()

print(outter_func_first())
dir(outter_func_first)
dir(outter_func_first.__closure__)
dir(outter_func_first.__closure__[0].cell_contents)
enclosing_variable = outter_func_first.__closure__[0].cell_contents
# enclosing_variable.('niva')

outter_func_first()



# Example 2
def multi(a):
    def remember_me(b):
        print(f'{a=}, {b=}')
        return a * b

    return remember_me


multi(3)(4)

multi_on_two = multi(2)
multi_on_two(7)


# info for lecture https://devpractice.ru/closures-in-python/ #Not working because ru
# Example 3


def make_closure():
    y = 1

    def inner(x):
        print(locals())
        return x + y

    y = 42
    return inner


make_closure()(100)  # What will be here??

"""Области видимости и значения по умолчанию применительно к переменным цикла.
"""
# Example 3
# example from https://ru.hexlet.io/courses/python-functions/lessons/closures/theory_unit
# пример замыкания переменной в цикле
listik = []
for num in range(20):
    def inside():
        print(num)


    listik.append(inside)

listik[7]()
"""
Нужно замкнуть переменную  в области видимости, которая завершится  сразу же  после  создания  замыкания.
"""
# Example 4
listik_n = []
for i in range(10):
    def make_print_my(num):
        def print_my():
            print(num)

        return print_my


    listik_n.append(make_print_my(i))

listik_n[7]()
""" еще один термин
    объект функции который сохраняет значения в объемлющих областях видимости, даже когда эти области могут прекратить свое
    существование.
"""


# lutz 492
# Example 5
def makeListOfFunctions() -> list:
    acts: list = []
    for i in range(5):
        acts.append(lambda x: i ** x)
    return acts


listOfFunc = makeListOfFunctions()

listOfFunc[0]  # поиск переменной в объемлющей области видимости производится во время вызова функции.
listOfFunc[0](2)  # Что будет здесь?
listOfFunc[3](2)  # Что будет, а здесь?


# Example 5, solve.
def makeListOfFunctionsSolve() -> list:
    acts: list = []
    for i in range(5):
        acts.append(lambda x, i=i: i ** x)  # Значения по умолчанию вычисляются в момент создания вложенной функции.
    return acts


listOfFunc = makeListOfFunctionsSolve()

listOfFunc[0]
listOfFunc[0](2)  # Что будет здесь?
listOfFunc[3](2)  # Что будет, а здесь?

# TODO: move to Decorators on lection
