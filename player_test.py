import random

from player import Player


def test_player_initial_attributes():
    sut = Player()

    assert sut.hp == 5
    assert sut.is_alive == True


def test_receive_damage_reduces_hp_by_damage_points():
    sut = Player()
    initial_hp = sut.hp
    damage_points = random.randint(1, initial_hp)

    sut.receive_damage(damage_points)
    actual = sut.hp

    assert actual == initial_hp - damage_points


def test_reducing_hp_to_zero_sets_is_alive_to_false():
    sut = Player()
    initial_hp = sut.hp

    sut.receive_damage(initial_hp)
    actual = sut.is_alive

    assert actual == False


def test_reducing_hp_below_zero_sets_is_alive_to_false():
    sut = Player()
    initial_hp = sut.hp

    sut.receive_damage(initial_hp + 1)
    actual = sut.is_alive

    assert actual == False
