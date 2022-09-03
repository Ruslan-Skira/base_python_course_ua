class Door:

    def __enter__(self):
        print('inside the enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('inside the Exit')
        # print(exc_type, exc_val, exc_tb)
        # raise exc_type(f'{exc_val}, \n {exc_tb}')

    def broken_door(self):
        print('broken door method')
        raise Exception('The   door is broken')

    def enter_the_door(self):
        return self.__enter__()

    def close_door(self, *args):
        return self.__exit__(*args)

flat_door = Door()


# V1
# with Door() as room_door:
#     room_door.broken_door()

# V2
with Door():
    print('doing something')



# print(flat_door.__enter__())
# print(flat_door.__exit__(1,2,3))
# print(flat_door.enter_the_door())
# print(flat_door.close_door())


# try:
#     flat_door.enter_the_door()
#     flat_door.broken_door()
# except Exception as e:
#     print(e)
# finally:
#     print(flat_door.close_door(Exception,'text', 'tb'))

# company_door = Door()


# if __name__ == '__main__':
#     try:
#         with company_door as x:
#             x.broken_door()
#             print(x, '')
#             print('inside the door')
#     except Exception as e:
#         print(e)
#
#
#     ######## Files #####
#     # file = open('group_06_l_15.py', 'w')
#     # print(type(file))
#     # file.write("\nprint('hello from file group...')")
#     # file.close()
#
#
#     #### менеджер контекста #####
#
#
#     # with open('example_for_context_manager_06.txt', 'w') as file:
#     #     file.write('hello I am python dev')
