# x = 1
# def cat():
#     print(cat)
#     return 'may'
#
# cat()
def foo1():
    print('first')

def foo2():
    foo1()
    print('wait')

def foo():
    foo2()
    print('end')

# foo()
# Рекурсия

def r(x: int) -> None:
    if x < 10:
        x += 1
        r(x)

    print(x)  # enclosed


r(1)



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
