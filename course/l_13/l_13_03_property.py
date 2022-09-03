"""getters and setters

"""


# TODO: Create class User and 3 methods 1. get_age, 2. set_age(value), 3. delete_age

class User_my:
    def __init__(self, age_user=None):
        self.age_user = age_user

    @property
    def age(self):
        return self.age_user

    @age.setter
    def age(self, value):
        self.age_user = value

    @age.deleter
    def age(self):
        self.age_user = 0


class Temperature:
    """Class Temperature create object with possibility to work with celsius and fahrenheit"""

    def __init__(self, *args, celsius=0):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9

    @fahrenheit.deleter
    def fahrenheit(self):
        self.celsius = 0

    def fahrenheit_function(self):
        return self.celsius * 9 / 5 + 32




u1 = User_my()

if __name__ == '__main__':
    print(u1.age)  # getter
    u1.age = 24  # Setter
    print(u1.age)
    del u1.age  # deletter
    print(u1.age)
