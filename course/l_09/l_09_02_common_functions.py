# Общие функции

x = 2
y = x

id(2)  # id объекта  id(x) == id(y)
type(2)  # отображает тип объекта
help(2)  # отображает справку по объекту

# Проверка типов

isinstance(2, int)  # Возвращает True или False,
# в зависимости от того, соответствует ли объект(первый arg,) типу(второй arg)
# существует второй вариант использования
isinstance(x, (int, float, complex))  # Возвращает True или False,
# в зависимости от того, соответствует ли объект(первый arg,) любому типу в tuple (второй arg)
x = 2
z = x > 0

# Преобразование в bool
bool(0), bool(0.0), bool(""), bool(''), bool(), bool(None), bool([]), bool(tuple())
# => (False, False, False, False, False, False)

