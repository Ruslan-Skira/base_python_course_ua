
"""# Задача 4. 30 баллов: Создать класс с методом которого можно будет возвращать область видимости созданного экземпляра класса.
# В конструкторе(__init__) вашего класса пускай будут те параметры которые вы захотите.
"""


class AreaOfVisibility:

    def __init__(self, name):
        self.name = name

    def visibility(self):
        if self in locals().values():
            return "Class instance in locals"
        else:
            return "Class instance in globals"


check = AreaOfVisibility('test')
print(check)
print(check.visibility())
from pprint import pprint
pprint(globals().values())
pprint(locals().values())

# Task explanation
class B:
    y = locals()

    def __init__(self):
        self.name = "B class"

    def local_scope(self):
        l = locals()
        return l

    def get_var(self):
        return vars(), vars(self), self.__dict__