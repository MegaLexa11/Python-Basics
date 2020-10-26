from random import choice
from time import sleep


class Car:

    # Атрибуты
    name = 'Lada'
    speed = 60
    color = 'white'
    is_police = False

    # Методы
    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self):
        direction = choice(['поворот налево', 'поворот направо', 'разворот'])
        print(f'{self.name} выполнила {direction}')

    def show_speed(self):
        print(f'{self.name} движется со скоростью {self.speed} км/час')


class SportCar(Car):

    # Атрибуты
    name = 'Chevrolet camaro'
    speed = 160
    color = 'Yellow'
    is_police = False


class PoliceCar(Car):

    # Атрибуты
    name = 'Police Hyundai'
    speed = 70
    color = 'White'
    is_police = True


class TownCar(Car):

    # Атрибуты
    name = 'Renault Logan'
    speed = 80
    color = 'Metallic'
    is_police = False

    # Методы
    def show_speed(self):
        if self.speed <= 60:
            print(f'{self.name} движется со скоростью {self.speed} км/час')
        else:
            print(f'Скорость превышена на {self.speed - 60} км/час')


class WorkCar(Car):
    # Атрибуты
    name = 'Gaz Barguzin'
    speed = 41
    color = 'White'
    is_police = False

    # Методы
    def show_speed(self):
        if self.speed <= 40:
            print(f'{self.name} движется со скоростью {self.speed} км/час')
        else:
            print(f'Скорость превышена на {self.speed - 40} км/час')


def chase(car):
    police = PoliceCar()
    print(f'{police.name} заметила превышение скорости у {car.name}')
    police.go()
    police.turn()
    sleep(8)
    if police.speed > car.speed:
        print(f'{police.name} догнала нарушителя')
        car.stop()
        police.stop()
    else:
        print(f'{car.name} оторвалась от погони')


gaz = WorkCar()
gaz.go()
gaz.turn()
gaz.show_speed()
if gaz.speed > 40:
    chase(gaz)
else:
    gaz.stop()

# Разделитель для отображения
sleep(5)
print('')

chevrolet = SportCar()
chevrolet.go()
chevrolet.turn()
chevrolet.show_speed()
chevrolet.stop()
sleep(5)

# Разделитель для отображения
sleep(5)
print('')

renault = TownCar()
renault.go()
renault.turn()
renault.show_speed()
if renault.speed > 60:
    chase(renault)
else:
    renault.stop()
