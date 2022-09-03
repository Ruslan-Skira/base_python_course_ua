# TODO: before it need to repeat with the 'super' method
# __new__
class Class_my:

    def __new__(cls, *args, **kwargs):
        """
        Этот метод вызывается до создания самого объекта, перед методом __init__
        Он создает и возвращает новый объект класса, а затем этот вновь созданный объект инициализируется методом __init__
        """
        return super().__new__(cls, *args, **kwargs)

#TODO: before it need to learn getattr() hasattr(). Create your own hasattr by reading documentation

class Counter:
    def __new__(cls):  # python takes automatically cls= Counter obj.
        obj = super(Counter, cls).__new__(cls)
        if not hasattr(cls, 'objects_list'):
            cls.objects_list = []
        cls.objects_list.append(obj)
        return obj


c = Counter()
s = Counter()
print("Object created", s)
s1 = Counter()
print("Object created", s1)

class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'obj'):
            obj = super(Singleton, cls).__new__(cls)
            cls.obj = obj
        return cls.obj

s1 = Singleton()
s2 = Singleton()
print(f'id1{id(s1)} id2{id(s2)}')



# __slots__

class A:
    """__slots__  магический атрибут, который позволяет задать ограниченный набор атрибутов, которыми будет
    обладать экземпляр класса."""
    __slots__ = ['method_one']

    def __init__(self):
        self.method_one = 1
        self.data = False  # Oшибка

    def method_two(self): pass
