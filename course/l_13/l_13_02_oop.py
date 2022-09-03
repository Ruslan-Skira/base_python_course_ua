# 1) Понятие класса и объекта
# Класс - это чертеж по которому создаются объекты

# 2) Объект - сущность созданная по определенному классу (чертежу),
# иногда его называют instance




# Инициализация и некоторые магические методы
class Cat3:
    average_weight = 4.1  # Атрибут класса

    def __new__(cls, *args, **kwargs):
        """
        Этот метод вызывается до создания самого объекта, перед методом __init__
        Он создает пустой объект в памяти
        """
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, name='', weight=average_weight):
        """
        В этот метод попадают все аргументы переданные в при создании объекта
        Он инициализирует объект, добавляя в него атрибуты
        """
        self.name = name
        self.weight = weight

    def __str__(self) -> str:  # Вызывается при приведении объекта к строке например функцией str()
        """Этот метод должен возвращать человеко-читаемое описание объекта"""
        return f"Cat with name: {self.name}"

    def __repr__(self) -> str:  # Вызывается, например, при выводе ошибки
        """
        Этот метод должен возвращать максимально-подробную информацию
        по воссозданию объекта
        """
        return f"Cat(name={self.name})"

    # Магические методы сравнения

    def __eq__(self, other):
        """Этот магический метод вызывается при использовании оператора '==' """
        return self.weight == other.weight

    def __le__(self, other):
        """Этот магический метод вызывается при использовании оператора '<=' """
        return self.weight <= other.weight

    def __ge__(self, other):
        """Этот магический метод вызывается при использовании оператора '>=' """
        return self.weight >= other.weight

    def __lt__(self, other):
        """Этот магический метод вызывается при использовании оператора '<' """
        return self.weight < other.weight

    def __gt__(self, other):
        """Этот магический метод вызывается при использовании оператора '>' """
        return self.weight > other.weight

    # вызов объекта как функции

    def __call__(self, action='Мурлыкать'):
        if action == 'Мурлыкать':
            print('Mrr-rrr mrr-rrr')
        else:
            print('Котик не хочет этого делать.')
        return ''

    def mur(self):
        print('murrrrrrr-rrrr-rr-mrrr-mrrrr')


# инициализация объектов
oleh = Cat3(name='Олег', weight=3)
kesha = Cat3(name='Кеша', weight=5)

# Сравнение объектов (котиков)
print(oleh == kesha)
print(oleh >= kesha)
print(oleh <= kesha)
print(oleh > kesha)
print(oleh < kesha)

# Вызов объекта (котика) как функции
oleh(action='Мурлыкать')
kesha(action='Играться')

kesha.mur()

##################### Примеры с котиками сложные 1######################
class Cat4:
    """
    class to show the @classmethod and @property
    """

    average_weight = 4.1  # Атрибут класса
    cats = []

    def __init__(self, name='', weight=average_weight, fluffiness=10):
        self.name = name
        self.weight = weight
        self.fluffiness = fluffiness  # пушистость

    @classmethod
    def get_av_weight(cls):
        if not cls.cats:
            return cls.average_weight
        sum_weight = 0
        cats_count = len(cls.cats)
        for cat in cls.cats:
            sum_weight += cat.weight
        return sum_weight / cats_count

    # этот декоратор говорит о том что этот метод будет использоваться классом, а не объектом

    @classmethod
    def is_fat_cat(cls, cat):
        assert isinstance(cat, cls), 'Это не объект класса Cat4'
        if cat.weight > cls.average_weight:
            return True
        return False

    # Этот декоратор позволяет обращатся к методу класса как к атрибуту,
    # не явно вызывая его
    @property
    def volume(self):
        return self.weight + (self.fluffiness // 5)

    @staticmethod
    def some_method(*args, **kwargs):
        """
        Иногда возникает потребность использовать класс
        просто для структурирования кода,
        без надобности использовать какие-либо поля класса,
        как своеобразный мешок для функций
        """
        return args, kwargs


c1 = Cat4()
print('Толстые ли эти котики?', Cat4.is_fat_cat(c1))
# print('Толстые ли эти котики?', Cat4.is_fat_cat(oleh))  => Вызовет ошибку


print(c1.volume)  # Вызовет метод volume, причем без использования оператора '()'

##################### Примеры с котиками сложные 2######################
class Cat:
    def __init__(self, color='Black', age=1):
        self.color = color
        self.age = age


murzik: Cat = Cat()
barsik: Cat = Cat(color='red')


##################### Примеры с котиками сложные 3######################

class Cat2:
    average_weight = 4.1  # Атрибут класса
    cats = []

    def __init__(self, color='Black', weight=0):
        if weight:
            weight = self.get_av_weight()

        # Обратите внимение, что внутри методов объектов будут доступны атрибуты класса
        self.color = color  # Атрибут объекта
        self.weight = weight  # Атрибут объекта

        self.cats.append(self)

    def get_av_weight(self):
        if not self.cats:
            return self.average_weight
        sum_weight = 0
        cats_count = len(self.cats)
        for cat in self.cats:
            sum_weight += cat.weight
        return sum_weight / cats_count


average_cat_weight = Cat2.average_weight  # Обращение к атрибуту класса

gosha = Cat2(weight=13)  # для обращения к атрибуту объекта нужно иметь объект!
gosha.weight = gosha.weight  # Обращение к атрибуту объекта

#################### Eще один вариант
"""Инициализация (от англ. initialization, инициирование)  создание, активация, подготовка к работе, определение параметров.
 Приведение программы или устройства в состояние готовности к использованию
 Приведение областей памяти в состояние, исходное для последующей обработки или размещения данных. [ГОСТ 19781 90]
 """


# TODO: способы вызова метода из объекта и почему в селф ничего не передаем
class T:
    def look(self):
        print(f'{T.__name__}')

    def __str__(self):
        return 'here will be smt interesting'


t = T()
t.look()
t.__class__.look(t)
f'{t}'


# TODO: show difference attribute class and attribute instance
class T():
    move = 'wtf is going here'

    def __init__(self):
        self.move = 123


t = T()

print(t.move)

print(T.move)


#

# TODO: Атрибуты
class Counter_my(object):
    all_counters = []

    def __init__(self, initial_count=0):
        Counter_my.all_counters.append(self)
        self.count = initial_count


c1 = Counter_my(2)
c2 = Counter_my(3)
assert len(Counter_my.all_counters) == 2
assert c1.all_counters is c2.all_counters


# TODO: Напишите свой класс родителя и ребенка и показать на примере инита как переписать c
#  super. Показать что будет если переписать до супер и после


class T():
    def __init__(self, *args, **kwargs):
        self.move = 123


class B(T):
    def __init__(self):
        super().__init__()
        self.move = 333


b = B()

b.move


# Наследоваание

class Transport:
    def __init__(self, max_move_speed=0):
        self.max_move_speed = max_move_speed

    def move(self):
        return f'move with speed {self.max_move_speed}'


class Car(Transport):
    def __init__(self, *args, model='', **kwargs):
        self.model = model
        super().__init__(*args, **kwargs)

        # super(Transport, self).__init__(*args, **kwargs)

    def move(self):
        return f'car move with speed {self.max_move_speed}'  # TODO: rewrite to "return f'car {super().move()}'"

    # TODO: покажи как работает метод __str__  в принте. и в строке f'{b1}


some_transport = Transport(max_move_speed=50)  # неявно вызывается демон ой __init__() поэтому он и магический.
car1 = Car(max_move_speed=350, model='Tesla X')


class AirPlane(Transport):
    def __init__(self, *args, wing_length=10, **kwargs):
        self.wing_length = wing_length
        super().__init__(*args, **kwargs)

    def move(self):
        parent_result = super().move()
        return f'{parent_result} При этом мы летим!'


class AirCar(Car, AirPlane):
    pass


# TODO: Create class User and 3 methods 1. get_age, 2. set_age(value), 3. delete_age


class Temperature:
    def __init__(self, *args, celsius=0):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9

    @fahrenheit.deleter
    def fahrenheit(self):
        self.celsius = 0


class Counter:
    def __new__(cls):
        obj = super(Counter, cls).__new__(cls)
        if not hasattr(cls, 'objects_list'):
            cls.objects_list = []
        cls.objects_list.append(obj)
        return obj


c = Counter()


class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'obj'):
            obj = super(Singleton, cls).__new__(cls)
            cls.obj = obj
        return cls.obj


s = Counter()
print("Object created", s)
s1 = Counter()
print("Object created", s1)
