"""Инструкция def создает переменную с ссылкой  на объект функции внутри. Пример ниже"""
def foo(): return 123
a = foo
b = a
c = b

# TODO: что будет лежать внутри? с

def some_name_for_function1():
    return


def some_name_for_function2():
    pass  # оператор заглушка


some_name_for_function1()  # -> None
some_name_for_function2()  # -> None


"""Аргументы 
Аргументы всегда передаются через операцию присваивания."""

def some_func_with_position(x: int, y: float) -> float:  # x, y - 2 позиционных параметра
    result = x * y
    print(result)
    return result


x1 = 3
x2 = 5.0
result1 = some_func_with_position(x1, x2)  # x=3, y=5

# simple example
def capitalizing_names(friend='my classmates'):  # friend='my classmates' - naming argument
    return friend.title()

def some_func_with_keys(some_key_arg='some_default_value') -> str:  # some_key_arg - именнованный аргумент.
    # 'some_default_value' - значение по умолчанию
    return some_key_arg + some_key_arg.replace('value', '****')


# При этом нет необходимости следить за порядком аргументов;
# Есть значение по умолчанию для аргументов, поэтому эти аргументы можно упускать.


result2 = some_func_with_keys()
result3 = some_func_with_keys(some_key_arg='some value some value some value')


# комбинации аргументов

def example(a, b, *args, x, y=None, z=2, u=5, **kwargs):
    type(args)  # tuple
    type(kwargs)  # dict
    pass

#TODO: тестик что будет возвращаться.
def example(*args, **kwargs):
    return args, kwargs

print(example(1,2,3,4, k=1, k2=2 ))



print(example({'a': 1990}))  # first variant


print(example(**{'a': 1990}))  # second variant

# 1. d ={'a': 1990}
# 2. example(**d) -> example(a=1990)


# Старайтесь не использовать мутабельные объекты в качестве параметров по умолчанию!
# Пример плохого использования
def change_list_bad_example(a, some_list=[]):
    some_list.append(a)
    return some_list


my_some_list1 = change_list_bad_example(1)
my_some_list2 = change_list_bad_example('zero')
my_some_list3 = change_list_bad_example('2')
print(my_some_list1, my_some_list2, my_some_list3)


#  [1, 'zero', '2'] [1, 'zero', '2'] [1, 'zero', '2']


def change_list_good_example(a, some_list=None):
    if not some_list:
        some_list = []
    some_list.append(a)
    return some_list


# Строки документации
# Строка документации - строка под def в тройных кавычках
def some_def_example():
    """This is example documentation"""
    return
