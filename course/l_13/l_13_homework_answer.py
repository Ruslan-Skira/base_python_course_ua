"""Task 1. 10 points. Написать пример класса с методом __call__()"""

"""
Task 2. 20 points. Написать свой класс как декоратор. И продебажить.
"""



class Functor:

    """Функтор(Функциональный объект, который можно использовать как функцию)
        example from  https://tirinox.ru/class-decorator/ and from https://realpython.com/primer-on-python-decorators/#classes-as-decorators
"""

    def __init__(self, func):
        self.func = func

    def __call__(self):
        print('before the functioon')
        self.func()
        print('after self func')


def print_me():
    print('I am function')