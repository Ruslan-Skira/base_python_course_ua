from datetime import datetime

# decorators

def exponentiation_in_for() -> list:
    """Exponentiation list elements to 2 in for"""

    start = datetime.now()

    answer = []
    for element in range(10_000):
        answer.append(element ** 2)

    finish = datetime.now() - start

    print('FOR', finish)
    return answer


def exponentiation_in_list_compreh() -> list:
    """Exponentiation list elements to 2 in list comprehension"""
    start = datetime.now()
    answer = [el ** 2 for el in range(10_000)]
    print('LIST_COMP', datetime.now() - start)

    return answer


# exponentiation_in_for()
# exponentiation_in_list_compreh()


####################### VARIANT 2 ########################################
# show that function it is object in python isinstance(function, object)




def counting_time(function):
    """Decorator  counting time"""
    def wrapper():
        start = datetime.now()
        answer = function()
        print(datetime.now() - start)
        return answer

    return wrapper


@counting_time
def exponentiation_in_for() -> list:
    """Exponentiation list elements to 2 in for"""
    answer = []
    for element in range(10_000):
        answer.append(element ** 2)
    return answer

@counting_time
def exponentiation_in_list_compreh_new() -> list:
    """Exponentiation list elements to 2 in list comprehension"""
    answer = [el ** 2 for el in range(10_000)]
    return answer


exponentiation_in_for()

exponentiation_in_list_compreh_new()
#
#
# def function_time_track(function):
#     def wrapper(*args, **kwargs):
#         start = datetime.now()
#         fun = function(*args, **kwargs)
#         print(function.__name__, datetime.now() - start)
#         return fun
#
#     return wrapper
#
#
#
#
#
#
# @counting_time
# def exponentiation_in_for() -> list:
#     """Exponentiation list elements to 2 in for"""
#     answer = []
#     for element in range(10000):
#         answer.append(element ** 2)
#     return answer
#
#
# print(exponentiation_in_for(), 'With decor')
#
#
# def exponentiation_in_list_compreh() -> list:
#     """Exponentiation list elements to 2 in list comprehension"""
#     answer = [el ** 2 for el in range(10000)]
#     return answer
#
#
# function_time_track(exponentiation_in_for)()
# function_time_track(exponentiation_in_list_compreh)()
# #
# #
# # ####################### VARIANT 3 ########################################
# #
# def function_time_track(function):
#     def wrapper():
#         start = datetime.now()
#         fun = function()
#         print(function.__name__, datetime.now() - start)
#         return fun
#
#     return wrapper
#
#
# @function_time_track
# def exponentiation_in_for() -> list:
#     """Exponentiation list elements to 2 in for"""
#     answer = []
#     for element in range(10000):
#         answer.append(element ** 2)
#     return answer
#
#
# @function_time_track
# def exponentiation_in_list_compreh() -> list:
#     """Exponentiation list elements to 2 in list comprehension"""
#     answer = [el ** 2 for el in range(10000)]
#     return answer
#
#
# print(exponentiation_in_for())
# print(exponentiation_in_list_compreh())
#
#
# ####################### VARIANT 4 ########################################
#
# def function_time_track(function):
#     def wrapper(*args, **kwargs):
#         start = datetime.now()
#         fun = function(*args, **kwargs)
#         print(function.__name__, datetime.now() - start)
#         return fun
#
#     return wrapper
#
#
# @function_time_track
# def exponentiation_in_for(n) -> list:
#     """Exponentiation list elements to 2 in for"""
#     answer = []
#     for element in range(n):
#         answer.append(element ** 2)
#     return answer
#
#
# @function_time_track
# def exponentiation_in_list_compreh(n) -> list:
#     """Exponentiation list elements to 2 in list comprehension"""
#     answer = [el ** 2 for el in range(n)]
#     return answer
#
#
# print(exponentiation_in_for(30))
# print(exponentiation_in_list_compreh(30))
# #
# #
# # ####################### VARIANT 5 with arguments ##########################
# #
# def counting_time(arg):
#     def outer(function):
#         def wrapper(*args, **kwargs):
#             print(f'{arg}')
#             start = datetime.now()
#             answer = function(*args, **kwargs)
#             print(datetime.now() - start)
#             return answer
#
#         return wrapper
#
#     return outer
#
#
# @counting_time('interesting does it works')
# def fill_up_list(name: str, list_: list or None) -> list:
#     list_.append(name)
#     return list_
#
#
# test_list: list = []
# print(fill_up_list('Hoho', test_list))
