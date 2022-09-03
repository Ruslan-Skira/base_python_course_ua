from course_03.l_13.l_13_04_property import Temperature

from course_03.l_14.tests import test_function  # Абсолютний імпорт
from tests import test_function  # відносний імпорт

from datetime import datetime
"""Import
1. Пошук модуля
2. Компіляція в байт-код як що потрібно
3. Запускают код модуля
це виконується один раз бо інтерпритатор зберігає в словнику sys.modules"""




kharkiv = Temperature(9)


print(f'{kharkiv.fahrenheit=}')
test_function(kharkiv.fahrenheit_function, 32)

# test_function(temperature, 33)
