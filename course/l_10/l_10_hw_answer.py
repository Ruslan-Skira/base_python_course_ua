'''
 Написать функцию которая будет добовлять код страны
 к номеру телефона с помощью  замыкания
 внешний вид вызова функции.
 my_number = full_telephone_number('+044')
 my_number('838372893')
 +044838372893 результат.
 '''



def full_telephone_number(code):
    def country_code(number):
        return code + number

    return country_code



my_number = full_telephone_number('+044')
my_number('838372893')


'''Сложнячок
'''


cache = input('Введите данные:')
print(cache)


# def caсhe_new_date(cache):
#     value=int(input('Введите данные:'))
#     value2=int(input('Введите данные:'))
#     c = [value,value2]
#     data=value+value2
#     if data in d.data():
#         d[data] = c
#         print('Данные уже есть мы вернем данные из памяти',*d.data())
#     else:
#         d[data] = c
#         print('Записали новое значение')
#     x= x+1


cache = dict()
print(cache)
cache.hash(cache)

def cache_hash(caсhe_new_date):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            print('Функция вызываеться впервые')
            cache[args] = caсhe_new_date(*args)

        return cache[args]

    return wrapper

# @cache_hash