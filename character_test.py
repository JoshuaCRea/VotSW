import random

from character import Character


def test_character_initial_attributes():
    sut = Character()

    assert sut.hp == 5
    assert sut.standing == True
    assert sut.rep_rank == 3
    assert sut.injured == False


def test_receive_damage_reduces_hp_by_damage_points():
    sut = Character()
    initial_hp = sut.hp
    damage_points = random.randint(1, initial_hp)

    sut.receive_damage(damage_points)
    actual = sut.hp

    assert actual == initial_hp - damage_points


def test_reducing_hp_to_zero_sets_standing_to_false():
    sut = Character()
    initial_hp = sut.hp

    sut.receive_damage(initial_hp)
    actual = sut.standing

    assert actual == False


def test_reducing_hp_below_zero_sets_standing_to_false():
    sut = Character()
    initial_hp = sut.hp

    sut.receive_damage(initial_hp + 1)
    actual = sut.standing

    assert actual == False
