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

    @staticmethod
    def look_hungry_cat():
        return 'Iam hungry, give me food my slave'




c1 = Cat4()
Cat4.look_hungry_cat()

# print('Толстые ли эти котики?', Cat4.is_fat_cat(c1))
# print('Толстые ли эти котики?', Cat4.is_fat_cat(oleh))  => Вызовет ошибку


# print(c1.volume)  # Вызовет метод volume, причем без использования оператора '()'
