from random import randint
from math import floor


def roll_skill() -> int:
    rolls = []
    for _ in range(0, 4):
        rolls.append(randint(1, 6))

    skill_value = (sum(rolls) - min(rolls))
    return skill_value


def modifier(number) -> int:
    return floor((number-10) / 2)


class Character:
    def __init__(self):
        self.strength = roll_skill()
        self.dexterity = roll_skill()
        self.constitution = roll_skill()
        self.intelligence = roll_skill()
        self.wisdom = roll_skill()
        self.charisma = roll_skill()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self): return roll_skill()
