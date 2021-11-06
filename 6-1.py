import time
import colorama


class TrafficLight:

    def __init__(self, c):
        self.__color = c

    def running(self):
        color = colorama.Fore.BLACK
        if self.__color == "red":
            color = colorama.Fore.RED
        elif self.__color == "yellow":
            color = colorama.Fore.YELLOW
        elif self.__color == "green":
            color = colorama.Fore.GREEN
        print(color + self.__color)


dict = {"red": 7, "yellow": 2, "green": 7}
while True:
    for k, v in dict.items():
        tl = TrafficLight(k)
        tl.running()
        time.sleep(v)
