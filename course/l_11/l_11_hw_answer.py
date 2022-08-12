'''прочитать 918-927 Lutz. 20 баллов'''

'''Скинуть файлик с примерами всех конструкций КРОМЕ менеджера контекста. With/as. 20 баллов'''

'''Задача 20 баллов написать функцию которая принимает от пользователя 2 аргумента и делит ондин на другой.
при попытке деления на ноль вывести пользователью "ай яй яй делить на ноль можно не многим" 
Все остальные исключения споймать и вывести их значение в текстовом формате.
И в любом случае вывести. " I 'am happy that you learn python"'''

def dividie_right(one: int or None =None, two: int or None =None):
    try:
        return one/two
    except:
        print('ай яй яй')


'''пройти тест 20 баллов https://holypython.com/advanced-python-exercises/exercise-3-try-except/ '''

'''Задача
повышенной
Интересности.Попробовать
посмотреть
на
написанный
код
и
сделать
его
более
надеждым.Любыt
изменения
приветствуюся.
просмотреть
каждую
программу
и
посмотреть
как
она
может
упасть.Попробовать
ее
зафейлить.
Во
время
тестирования
заметить
какие
ошибки
появляется
использзуя
исключения
изменить
код.И
не
только
исключения, а
и
фантазию.'''


def example1():
    for i in range(3):
        x = int(input("enter a number: "))
        y = int(input("enter another number: "))
        print(x, '/', y, '=', x / y)


def example2(L):
    print("\n\nExample 2")
    sum = 0
    sumOfPairs = []
    for i in range(len(L)):
        sumOfPairs.append(L[i] + L[i + 1])

    print("sumOfPairs = ", sumOfPairs)


def printUpperFile(fileName):
    file = open(fileName, "r")
    for line in file:
        print(line.upper())
    file.close()


def main():
    example1()
    L = [10, 3, 5, 6, 9, 3]
    example2(L)
    example2([10, 3, 5, 6, "NA", 3])
    example3([10, 3, 5, 6])

    printUpperFile("doesNotExistYest.txt")
    printUpperFile("./Dessssktop/misspelled.txt")


main()



# Решение http://tephra.smith.edu/dftwiki/index.php/CSC111_Exercises_with_Exceptions:_try/except
def example1():
    while True:
        try:
            x = int(input("enter a number: "))
            y = int(input("enter another number: "))
            print(x, '/', y, '=', x / y)
            break
        except ZeroDivisionError:
            print("Can't divide by 0!")
        except ValueError:
            print("That doesn't look like a number!")
        except:
            print("something unexpected happend!")


def example2(L):
    print("\n\nExample 2")
    print("L          = ", L)
    sum = 0
    sumOfPairs = []
    for i in range(len(L)):
        try:
            sumOfPairs.append(L[i] + L[i + 1])
        except IndexError:
            continue
        except TypeError:
            continue

    print("sumOfPairs = ", sumOfPairs)


def printUpperFile(fileName):
    try:
        file = open(fileName, "r")
    except FileNotFoundError:
        print("***Error*** File", fileName, "not found!")
        return False

    for line in file:
        print(line.upper())
    file.close()
    return True


def main():
    example1()

    L = [10, 3, 5, 6, 9, 3]
    example2(L)

    L = [10, 3, "NA", 6, 9, 3]
    example2(L)

    open("doesNotExistYest.txt", "w").close()

    printUpperFile("doesNotExistYest.txt")


    printUpperFile("./Dessssktop/misspelled.txt")


main()


'''Работу
с
файлами
мы
не
проходи.Тему
освещать
будем
но
можно
и
самому
глянуть
про
функцию
open()
что
она
делает
да
как.'''






























'''Написать функцию генератор с помощью range которая будет выводить числа по порядку и в обратном направлении.
''' # TODO: I do not give this task


def my_gen_back_forth(start, finish, step):
    yield from range(start, finish, step)
    yield from range(finish, start-1, -step)

for number in some(1, 10, 1):
    print(number)


'''Написать функцию с названием file_my() которая внутри будет содержать 
две переменные open closed.  '''# TODO: Додумать как создать подобие объекта
# файл и объяснить что нужно вызывать обязательно фунцию closed()

def file_my(open=False, closed=True):
    ...

book = file_my()

try:
    open(file_my())
except Exception as e:
    print('something')

'''>>> f = open('1.txt')
>>> ints = []
>>> try:
...     for line in f:
...         ints.append(int(line))
... except ValueError:
...     print('Это не число. Выходим.')
... except Exception:
...     print('Это что ещё такое?')
... else:
...     print('Всё хорошо.')
... finally:
...     f.close()
...     print('Я закрыл файл.')
...     # Именно в таком порядке: try, группа except, затем else, и только потом finally.
...
Это не число. Выходим.
Я закрыл файл.'''
