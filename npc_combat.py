import random


def get_attack_value():
    atk = random.randint(1, 6)
    if atk == 1 or atk == 6:
        return "Attack High"
    elif atk == 2 or atk == 5:
        return "Attack Middle"
    elif atk == 3 or atk == 4:
        return "Attack Low"


def get_blk_value():
    blk = random.randint(1, 6)
    if blk == 1 or blk == 6:
        return "Defend High"
    elif blk == 2 or blk == 5:
        return "Defend Middle"
    elif blk == 3 or blk == 4:
        return "Defend Low"


def get_mod_value():
    mod = random.randint(1, 6)
    if mod == 1:
        return "Wolf"
    elif mod == 6:
        return "Star"
    else:
        return "Normal"