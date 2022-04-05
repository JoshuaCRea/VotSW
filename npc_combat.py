import random


def get_attack_value():
  atk = random.randint(1, 6)
  if atk == 1 or atk == 6:
    return "Attack High"
  elif atk == 2 or atk == 5:
    return "Attack Middle"
  elif atk == 3 or atk == 4:
    return "Attack Low"