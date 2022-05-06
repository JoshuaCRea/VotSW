import random
import sys
import uuid

import player


def test_when_constructed_then_hp_is_initial_hp():
    initial_hp = random.randint(1, sys.maxsize)
    town = uuid.uuid4()

    sut = player.Player(initial_hp, town)

    assert sut.hp == initial_hp


def test_when_constructed_then_town_is_ctor_value():
    initial_hp = random.randint(1, sys.maxsize)
    town = uuid.uuid4()

    sut = player.Player(initial_hp, town)

    assert sut.town == town
