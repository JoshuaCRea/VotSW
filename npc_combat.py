import random


def roll_for_clash_value(num):
    if num == 1 or num == 6:
        return "Hi"
    elif num == 2 or num == 5:
        return "Mid"
    elif num == 3 or num == 4:
        return "Lo"


def get_mod_value(num):
    if num == 1:
        return "Wolf"
    elif num == 6:
        return "Star"
    else:
        return "Normal"


def get_mod_message(mod_value):
    if mod_value == "Wolf":
        return "Defense is reversal."
    if mod_value == "Star":
        return "Defense is reversal."
    return "No modification."


def get_kos_clash_values():
    kos_atk = roll_for_clash_value(random.randint(1, 6))
    kos_blk = roll_for_clash_value(random.randint(1, 6))
    kos_mod = get_mod_value(random.randint(1, 6))
    return kos_atk, kos_blk, kos_mod
