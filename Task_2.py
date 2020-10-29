from abc import abstractmethod


class Clothes:

    clothes_list = []

    @abstractmethod
    def __init__(self, material):
        self.material = material

    @abstractmethod
    def cloth_counter(self):
        pass


class Coat(Clothes):

    def __init__(self, size, material):
        self.size = size
        super().__init__(material)

    @property
    def cloth_counter(self):
        return round(float(self.size) / 6.5 + 0.5, 2)


class Suit(Clothes):

    def __init__(self, height, material):
        self.height = height
        super().__init__(material)

    @property
    def cloth_counter(self):
        return round(float(self.height) * 2 * 0.3, 2)


coat = Coat(48, 'Wool')
print(f'{coat.cloth_counter} meters of {coat.material} will be spent to make a Coat')
suit = Suit(2, 'Cotton')
print(f'{suit.cloth_counter} meters of {suit.material} will be spent to make a Suit')
# Не хватило сил и времени на подумать))
print(f'Complete cloth consumption: {suit.cloth_counter + coat.cloth_counter} meters')
