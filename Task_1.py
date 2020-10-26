import time
from colorama import Fore


class TrafficLight:
    # атрибут
    __color = None

    # метод
    def running(self):
        def color_change(new_color, time_wait):
            TrafficLight.__color = new_color
            print(TrafficLight.__color)
            time.sleep(time_wait)
        while True:
            color_change(Fore.RED + '●', 7)
            color_change(Fore.YELLOW + '●', 2)
            color_change(Fore.GREEN + '●', 9)


a = TrafficLight()
a.running()
