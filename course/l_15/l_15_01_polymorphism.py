'''

Что такое полиморфизм?
В буквальном значении полиморфизм означает множество форм.
Полиморфизм — очень важная идея в программировании. Она заключается в использовании единственной
сущности(метод, оператор или объект) для представления различных типов в различных сценариях использования.
Давайте посмотрим на пример:

'''


class Animal:
    pass


class Mammals:
    pass


class Birds:
    pass


class Cats(Animal, Mammals):
    def voice(self):
        return 'kirry kirry'

    def __str__(self):
        return 'Cats'


class Dogs(Animal, Mammals):
    def voice(self):
        return 'gav gav'

    def __str__(self):
        return 'Dogs'


class Pigeon(Animal, Birds):
    def voice(self):
        return 'cur cur'

    def die(self):
        return 'Pigeon died'

    def is_live(self):
        return True


class Snake(Animal):
    def voice(self):
        return 'shhhh'


barsik = Cats()
bobik = Dogs()
wedding_gift = Pigeon()
rope = Snake()
# print('I am from  polimorf file!!!')


# print(__name__, "__NAME__  FROM POLIMORF FILE")

my_pets = [barsik, bobik, wedding_gift, rope]


# if __name__ == '__main__':
#     for pets in my_pets:
#         print(pets.voice(), 'voice')





####################################3
# declare our own string class
class StringMy:

    # magic method to initiate object
    def __init__(self, first_value: str):
        self.first_value = first_value

    # print our string object
    def __repr__(self):
        return 'Object: {}'.format(self.first_value)

    def __add__(self, second, *args):
        return f"{self.first_value} {second} 'From __add__ method'"


if __name__ == '__main__':
    # object creation
    string1 = StringMy('Hello')

    # concatenate String object and a string
    x = string1 + ' Geeks'
    print(x)
