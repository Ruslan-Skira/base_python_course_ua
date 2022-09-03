"""
    команда yield(бросить) используется только для создания генераторов и в теле функции генератора.
    Мы не тратим время на хранение промежуточного результата  ни итогового результата. Но не позволяет использовать
    индексы.
    Ход выполнения функции прерывается на время. У генераторов локальные переменные сохраняют свое состояние.

"""


def generator_my():
    """
    генераторная функция которая возвращает генератор.

    """
    yield 'first iteration'
    yield 2
    yield 3
    yield 4
    yield 'Last iteration'


# 1. создание генератора генераторной функцией.
g = generator_my()

# 2. вызов генератора через метод __next__
# print(g.__next__())
# print(next(g))

# 3. вызов генератора через цикл
for element in g:
    print(element)


# Выполнение кода до Yield и после

def gen_func2():
    print('before yield')
    yield 1
    print('after yield')


gen = gen_func2()

next(gen)
next(gen)


def countdown(n):
    result = []
    while n != 0:
        result.append(n - 1)
        n -= 1
    return result


print(countdown(3))


def gen_countdown(n):
    while n != 0:
        yield n - 1
        n -= 1


gc = gen_countdown(5)

print(next(gc))
print(next(gc))
print(next(gc))
print(dir(gc))
print(type(gc))

# for i in gen_countdown(5):
#     print(i)
