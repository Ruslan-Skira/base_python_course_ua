# Итераторы - все объекты которые могут участвовать в цикле

a = [1, 2]  # Итерируемый объект. iterable

b = a.__iter__()  # метод __iter__ возвращает специальный объект - iterator.
с = b.__iter__()  # Интересным является то,
# что большинство итераторов возвращают себя при вызове у них метода __iter__()

# b - объект-итератор.

b.__next__()  # Именно его использует цикл for i in …  для получения i:


# При этом, если следующего объекта нет - будет вызвано исключение, и его необходимо будет обработать

# Итого - Итератор - это такой объект, который реализует в два метода - __iter__ и __next__


# Генераторы - это такие объекты, которые могут учавствовать в цикле, но только один раз. Это разновидность Итераторов
# v1 создание генератора через функцию
def yield_example():
    yield 1
    yield 2
    yield 3


ye = yield_example()
print(ye.__next__())
print(ye.__next__())
print(ye.__next__())







def my_generator(in_range=10):
    current_i = 0
    while current_i < in_range:
        current_i += 1
        yield current_i


for i in my_generator(in_range=15):
    print(i)


def manual_call(generator):
    while True:
        print(
            'manual_call', generator.__next__()
        )


generator_obj = my_generator(in_range=12)
manual_call(generator_obj)

# Для объявления генераторов есть специальный синтаксис:
my_new_generator = (5 for i in range(5) if i > 3)  #

#TODO: Почему можно сделать сет, дикт, лист comprehension и нельзя сделать tuple comrehension.
print(my_new_generator.__class__)
type(my_new_generator)

# yield from
# V2: Example with yield_example
def yield_from_example():
    yield from yield_example()
    yield from yield_example()
yfe = yield_from_example()

for i in yfe:
    print(i)

# V1: Example with range


def some():
    yield from range(4)
    yield from range(7, 12)


for i in some():
    print(i)

