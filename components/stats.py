from enum import Enum


class Stat(object):
    def __init__(self, uid, current, max):
        self.uid = uid
        self.current = current
        self.max = max

    def __str__(self):
        return str(self.current)

    def __int__(self):
        return int(self.current)

    def modify_current(self, value):
        self.current += value

    def modify_max(self, value):
        self.max += value


class StatModifier(object):
    def __init__(self, uid, value):
        self.uid = uid
        self.value = value


class CharacterStats(object):
    def __init__(self):
        self.health = Stat(Stats.Health, 1, 1)
        self.mana = Stat(Stats.Mana, 1, 1)
        self.strength = Stat(Stats.Strength, 1, 1)
        self.dexterity = Stat(Stats.Dexterity, 1, 1)
        self.constitution = Stat(Stats.Constitution, 1, 1)
        self.intelligence = Stat(Stats.Intelligence, 1, 1)
        self.charisma = Stat(Stats.Charisma, 1, 1)
        self.wisdom = Stat(Stats.Wisdom, 1, 1)


class Stats(Enum):
    Health = 'health'
    Mana = 'mana'
    Strength = 'strength'
    Dexterity = 'dexterity'
    Constitution = 'constitution'
    Intelligence = 'intelligence'
    Charisma = 'charisma'
    Wisdom = 'wisdom'
