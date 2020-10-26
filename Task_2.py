def multiplication(**kwargs):
    result = 1
    for i in kwargs:
        result *= i
        return result


class Road:

    # Конструктор
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self._weight = 25
        self._layers = 5

    def volume_count(self):
        print(f'Complete asphalt weight: {int(self._length * self._width * self._weight * self._layers / 1000)} tons')


way = Road(3000, 5)
way.volume_count()
