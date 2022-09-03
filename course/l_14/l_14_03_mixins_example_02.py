'''
Mixin классы - это концепция в программировании, в которой класс предоставляет функциональные возможности,
 но не предназначен для самостоятельного использования. Основная цель миксинов - предоставить какие-то
 дополнительные методы.
 В Python так называемые миксины — это классы, которые живут в обычном дереве наследования,
  но они остаются небольшими, чтобы избежать создания иерархий, которые слишком сложны для понимания программистом.
  В частности, миксины не должны иметь общих предков, кроме объекта, с другими родительскими классами.
'''


class Machine:
    def __init__(self, power=None, engine='ICE', *args, **kwargs):
        """ constructor
            Arguments:
                power (int) - engine power
                engine (str) - type of engine , default is Internal Combustion Engine
                """
        self.power = power
        self.engine = engine
        # super().__init__(power, engine, *args, **kwargs)

    def start_car(self):
        return 'Start Machine '


class CarMixin:
    """Mixin class to add functionality only for cars"""

    def __init__(self, model_name):
        self.model_name = model_name

    def start_car(self):
        return f'I starts the car Mixin '

    def light(self):
        return 'bright'


class Mercedes(Machine, CarMixin):
    # class Mercedes(CarMixin, Machine ):
    # def start_car(self):
    #     return f'HERE IS MERS {super().start_car()}'

    pass


m = Mercedes('clc300')
# print(m.start_car())
# print(Mercedes.__mro__)


my_car = Mercedes()


# dir(my_car)


# 2. Example change the place
class BMW(CarMixin, Machine):  # change the the place
    def start_car(self):
        return f'HERE IS MERS {super().start_car()}'


class Toyota(Machine, CarMixin):
    @property
    def start_car(self):
        return f'HERE IS Toyota {super().start_car()}'


if __name__ == '__main__':
    # my_car = BMW('m5')
    # print(dir(my_car))
    # print(my_car.start_car())
    # property example
    prius = Toyota()
    print(prius.start_car)

