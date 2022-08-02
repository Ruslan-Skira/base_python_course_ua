# функція може викликати інші функції
def foo1():
    print('first')


def foo2():
    foo1()
    print('wait')


def foo():
    foo2()
    print('end')


# Рекурсія - називається виклик фунції самоЇ себе.

# V1 count down


def count_down_to_zero(counter: int) -> None:
    """
    Функія працює як зворотнії лічильник.

    Кожна рекурсивна функція будується з двох частин: базовий типу функції та рекурсивної частини.
    :arg counter - integer,
    :return None

    """
    print(counter)
    if counter == 0:  # базова частина
        return
    else:
        count_down_to_zero(counter - 1)  # рекурсивна частина


# V2  Count down
def count_down_to_zero_v2(counter: int) -> None:

    if counter < 10:
        counter += 1
        count_down_to_zero_v2(counter)
    print(counter)  # enclosed




def factorial_with_rec(x):
    # Определяем выход и рекурсии
    """
    Факториал числа — это произведение натуральных чисел от 1 до самого числа (включая данное число).
    Обозначается факториал восклицательным знаком «!».
    Слово факториал произошло от латинского factor (делающий, производящий).
    5! = 1*2*3*4*5
    """
    if x == 1 or x == 0:
        return 1
    previouse = factorial_with_rec(x - 1)

    arg = previouse * x
    return arg


print(factorial_with_rec(5))
if __name__ == '__main__':
    # example 0
    foo()

    # example 1
    count_down_to_zero(10)
    # example 2
    count_down_to_zero_v2(1)
    # example 3
    factorial_with_rec(5)

