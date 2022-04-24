import random


def get_attack_value(num):
    if num == 1 or num == 6:
        return "Hi"
    elif num == 2 or num == 5:
        return "Mid"
    elif num == 3 or num == 4:
        return "Lo"


def get_blk_value(num):
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
