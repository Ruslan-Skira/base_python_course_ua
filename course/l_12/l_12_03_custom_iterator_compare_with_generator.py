"""
    итерируемый объект - объект который предоставляет возможность обойти поочередно свои элементы.
    Может быть преобразован к итератору.

    Итератор - объект который поддерживает функцию next() помнит о том какой элемент будет следующим.
    Генератор - частный случай итератора, элементы которого можно итерировать только один раз.

    Генератор_2 - это функция которая создает или возвращает последовательность значений с использованием yield метода.
"""

# А это генератор выражений. Чтобы стразу не возвращать все значения.
squares = (number ** 2 for number in range(0, 100, 6))  # генератор является частным случаем итератора.

print(dir(squares))
print(type(squares))


def squares_generator_function(n):
    for e in range(0, n):
        yield e ** 2


squares_generator_function(3)  # Возвращает generator object

print(dir(squares_generator_function))
print(type(squares_generator_function))
print(type(squares_generator_function(4)))

'''Реализуем протокол итератора'''


class StringByLetter:
    """ Объект итератора"""

    def __init__(self, string):
        self.string = string
        self.str_len = len(string)
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position < self.str_len:
            letter = self.string[self.position]
            self.position += 1
            return letter.upper()
        raise StopIteration


string_by_letter_test = StringByLetter(' I will be PythonDev')

for letter in string_by_letter_test:
    print(letter)


# и тоже самое с помощью генератора.
def string_by_letter_generator(string_m: str):
    for letter in string_m:
        yield letter.upper()


for letter in string_by_letter_generator('I am a Python developer'):
    print(letter)
