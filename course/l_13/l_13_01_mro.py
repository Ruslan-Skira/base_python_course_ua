class FGrandFather():
    surname = 'Douglas'
    pass


class FGrandMother():
    pass


class MGrandFather():
    surname = 'Chita'

    pass


class MGrandMother():
    eyes_color = 'green'
    pass


class Mother(MGrandFather, MGrandMother):
    height = 150


class Father(FGrandFather, FGrandMother):
    pass


class Son(Father, Mother):
    # eyes_color = 'blue'
    pass


# mike = Son()


if __name__ == "__main__":  # точка входу в код.
    # print(mike.surname)
    # print(Son.__mro__)  # method resolution order

    i_am = Son()
    print(i_am.eyes_color)
    print(i_am.height)
    print(i_am.surname)
