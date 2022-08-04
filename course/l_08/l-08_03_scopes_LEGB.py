def example1(x: int, y: int):
    # Идентификаторы 'x' и 'y' являются:
    # - local для example1()
    # - nonlocal для example2()

    def example2(a, b):

        
        return a + 2, b + 3  # 'a' - локальный идентификатор функции cube()

    return max(
        *example2(x, y), *example2(y, x)
    )
    # Функция max() находится во встроенной области видимости


# Идентификаторы 'q', 'w' и 'e' имеют глобальную область видимости
q, w, e = 1, 2, 4
print(example1(q, w))  # 8

# По умолчанию,
# идентификаторы из других областей доступны только для чтения
x = 'someeee'


def example_with_global():
    x = 'zzzzzzz'  # не поменяет значение x вне функции,
    # а создаст новый идентификатор x для локальной области видимости

    # Но есть способ поменять глобальную переменную
    global x
    # Теперь мы можем менять x
    x = 2
    # И Тs


def func():
    def first_inner_func():
        value = 100  # 'value' - локальный идентификатор

    value = 10
    first_inner_func()
    print(value)  # 10

    def second_inner_func():
        nonlocal value
        value = 100  # nonlocal позволяет использовать value из func()

    second_inner_func()
    print(value)  # 100

#TODO: что будет?
def f():
    print(i)

for i in range(10):
    i += 1

'E уровень Enclosed с 2.2 - это локальные области видимости объемлющих инструкций def '
x = 99
def f1():
    x = 88
    def f2():
        print(x)
    f2()
f1()

# TODO: вопросы для проверки
# 1
x = 'spam'
def f():
    print(x)
f()
# 2
x = 'spam'
def f():
    x = 'add'

f()
print(x)

# 3
x = 'spam'
def f():
    x = 'add'
    print(x)

f()
print(x)
# 4
x = 'spam'
def f():
    global x
    x = 'add'

f()
print(x)

# 5
x = 'spam'
def f():
    x = 'add'
    def nested():
        print(x)
    nested()

f()
x

# 6
def f():
    x = 'add'
    def nested():
        nonlocal x
        x = 'Spam'
    nested()
    print(x)

f()
# 7
"Назовите три или более способов сохранять информаци о состоянии в функциях"