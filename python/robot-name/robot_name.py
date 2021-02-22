from string import ascii_uppercase
import random


class Robot:
    def __init__(self):
        self.name = self.__gen_name()

    def reset(self):
        self.name = self.__gen_name()

    def __gen_name(self):
        random.seed()
        name = ''

        for i in range(0, 5):
            if i < 2:
                name += random.choice(ascii_uppercase)
            else:
                name += str(random.randint(0, 9))

        return name
