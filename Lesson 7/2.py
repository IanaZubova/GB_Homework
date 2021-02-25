from abc import ABC


class AbstractClothes(ABC):

    @property
    def measure(self):
        pass


class Clothes(AbstractClothes):

    def __init__(self, name):
        self.name = name


class Costume(Clothes):

    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def measure(self):
        calc_costume = self.height * 2 + 0.3
        return calc_costume


class Coat(Clothes):

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def measure(self):
        calc_coat = self.size / 6.5 + 0.5
        return calc_coat


new_costume = Costume('Brioni', 56)
new_coat = Coat('Dior', 42)

print(new_costume.measure)
print(new_coat.measure)