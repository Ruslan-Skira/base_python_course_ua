import pprint


class Cell:
    def __init__(self, **kwargs):
        self.color = 'Transparent'

    def population(self):
        return 'two'


class Animal:
    def __init__(self, voice='voiceAnimal', fur="None", blood=None):
        self.fur = fur
        self.voice_animal = voice
        self.blood = blood

    def voice(self):
        return self.voice_animal

    def population(self):
        return 'three'


class Cat(Cell, Animal):
    def __init__(self, name=None, **kwargs):
        self.color = 'NOT TRANSPERENT'

        super().__init__(blood='red', **kwargs)  # важный момент до и после супер.

        self.voice_animal = 'May'
        self.name = name

    def voice(self):
        return super().voice(), self.name

    def get_blood_color(self):
        return self.blood

    def population(self):
        return super().population() + 'cats'


murzik = Cat('murzik')
print(vars(murzik))

pprint.pprint(dir(murzik))
print(murzik.voice())
print(murzik.get_blood_color())

a = Animal()
print(a.voice())
