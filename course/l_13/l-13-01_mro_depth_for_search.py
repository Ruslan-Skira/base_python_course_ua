class FGrandFather():
    # surname = 'Douglas'
    pass


class FGrandMother():
    pass


class MGrandFather():
    pass


class MGrandMother():
    pass


class Mother(MGrandFather, MGrandMother):
    height = 150
    surname = 'Chita'


class Father(FGrandFather, FGrandMother):
    # surname = 'Duglassito'
    eyes_color = 'green'
    pass


# class Neigbor():pass

class Son(Mother, Father):
    # eyes_color = 'blue'
    pass


# mike = Son()


if __name__ == "__main__":  # точка входу в код.
    # print(mike.surname)
    # print(Son.__mro__)  # method resolution order

    i_am = Son()
    print(i_am.eyes_color)
    print(i_am.height)
