import time
from termcolor import colored


def say_for_secs(object, amountofsecs):
    print(object)
    time.sleep(amountofsecs)


def say_for_no_secs(object):
    print(object)


def say_with_color_for_secs(object, color, secs=float):
    say_for_secs(colored(object, color), secs)


def say_with_color_for_no_secs(object, color):
    say_for_no_secs(colored(object, color))


def __main__(self):
    say_for_no_secs(self)
