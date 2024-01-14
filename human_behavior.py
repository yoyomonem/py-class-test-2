import time
from termcolor import colored
from typing import *


class HumanBehavior:
    def say_for_secs(self, text: str, secs: float | int):
        print(text)
        time.sleep(secs)

    def say_for_no_secs(self, text: str):
        print(text)

    def say_with_color_for_secs(self, text: str, color: str | None = None, on_color: str | None = None,
                                attrs: Iterable[str] | None = None, secs: float | int = 2):
        self.say_for_secs(colored(text, color, on_color, attrs), secs)

    def say_with_color_for_no_secs(self, text: str, color: str | None = None, on_color: str | None = None,
                                   attrs: Iterable[str] | None = None):
        self.say_for_no_secs(colored(text, color, on_color, attrs))
