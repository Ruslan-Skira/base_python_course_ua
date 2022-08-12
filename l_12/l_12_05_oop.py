# 1) Понятие класса и объекта
"""Класс - это чертеж по которому создаются объекты

2) Объект - сущность созданная по определенному классу (чертежу),
иногда его называют instance


Переходим к котикам
OOP позволяет объединить данные и поведение"""


class Cat(object):
    def __init__(self, color='Black', age=1, name='murzik'):
        self.color = color
        self.age = age
        self.name = name

    def may(self):
        print(self.name, 'MAY')


murzik: Cat = Cat()

barsik: Cat = Cat(color='red')

'''self ссылка сама на себя на объект'''


# 3) Атрибуты классов и объектов (иногда их называют поля)

class Cat2:
    average_weight = 4.1  # Атрибут класса
    cats = []

    def __init__(self, color='Black', weight=0):
        """создан для инициализации объекта не создания! За создание отвечает другой метод"""
        if weight:
            weight = self.get_av_weight()

        # Обратите внимание, что внутри методов объектов будут доступны атрибуты класса
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

    def __str__(self) -> str:  # Вызывается при приведении объекта к строкеЮ например функцией str()
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


class Cat4:
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


# Наследование

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
        return f'car move with speed {self.max_move_speed}'


some_transport = Transport(max_move_speed=50)
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


class Counter:
    def __new__(cls):
        obj = super(Counter, cls).__new__(cls)
        if not hasattr(cls, 'objects_list'):
            cls.objects_list = []
        cls.objects_list.append(obj)
        return obj


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
