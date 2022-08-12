"""
    команда yield(бросить, сдаться) используется только для создания генераторов и в теле функции генератора.
    Мы не тратим время на хранение промежуточного результата  ни итогового результата. Но не позволяет использовать
    индексы.
    Ход выполнения функции прерывается на время. У генераторов локальные переменные сохраняют свое состояние.

"""




def countdown(n):
    result = []
    while n != 0:
        result.append(n - 1)
        n -= 1
    return result


print(countdown(3))


def gen_countdown(n):
    while n != 0:
        yield n - 1
        n -= 1


gc = gen_countdown(5)

print(next(gc))
print(next(gc))
print(next(gc))
print(dir(gc))
print(type(gc))

for i in gen_countdown(5):
    print(i)
