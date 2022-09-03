"""https://docs.python.org/3/library/functools.html#functools.reduce"""
from functools import reduce

'''Функция reduce применяет функции к парам элементов и накапливает результат'''


def f(a, b):
    return a, b


progression = reduce(f, (1, 2, 3, 4, 5, 6), 21)
print(progression)  # в консоли в скобках показано то с какими аргументами будут проходить расчеты.


def my_sum(first, second):
    return first + second


progression = reduce(lambda a, b: a - b, (1, 2, 3,), 100)

print(progression)

# v2 example
letters = ["P", "Y", "T", "H", "O", "N"]
word = reduce(lambda x, y: x + y, letters, 'language ')
print(word)

# v3 example
factorial = (5, 4, 3, 2, 1)
factorial_five = reduce(lambda one, two: one * two, factorial)
print(factorial_five)

# v4 example
from operator import add

lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
concat_list = reduce(add, lists)
print(concat_list)


# эквивалент функции reduce. Советую разовраться как работает.
def reduce_my(function, iterable, initializer=None):
    it = iter(iterable)  # make iterator
    if initializer is None:
        value = next(it)  # take next value
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value
