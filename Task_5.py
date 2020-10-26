class Stationery:

    title = 'Stationery'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        print('Достаем ручки и пишем')


class Pencil(Stationery):

    def draw(self):
        print('Чертить можно только карандашом')


class Handle(Stationery):

    def draw(self):
        print('Важную информацию можете подчеркнуть маркером')


scissors = Stationery()
scissors.draw()

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()