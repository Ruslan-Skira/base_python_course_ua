"""
Scope - область видимости
Namespaces - пространство имен
Существуют для избегания проблем с поиском имен.
name = 'Neo'"""
x = 1  # global scope

def namespace():  # имя функций тоже заносится в пространство имен но выше
    """Пространство имен это словарь с именами и значениями.
     Вместе с определением пространства имен python соответственно
    определяет и области видимости. """

    print(locals())  # Локальное пространство имен
    name = 'Trinity'
    print(locals())
    age = 50
    print('Function namgespace():', locals())


print('External namespace', locals())

""" Область видимости это цепочка пространств имен которое начинается от локального
и длится до глобального или до встроенного.
Область видимости определяет то в каком пространстве имен
Python  будет искать определение конкретного имени конкретной переменной и в каком
порядке он этот поиск будет производить. Для порядка поиска есть абривиатура LEGB"""

product = 'bread'  # Global variables


def changing_product():
    product = 'Milk'  # locals relates to changing_products and enclosed for showing_enclosed
    print('Local: ', product)

    def showing_enclosed():
        nonlocal product
        print('Inside showing enclosed', product)
        product = 'Cola'
        print('Enclosed scope: ', product)

    showing_enclosed()
    print(product, '----')


changing_product()

print('Global:', product)
