import uuid

import player


def test_when_constructed_then_hp_is_5():
    sut = player.Player(uuid.uuid4())

    assert sut.hp == 5


def test_when_constructed_then_combat_stones_is_2():
    sut = player.Player(uuid.uuid4())

    assert sut.combat_stones == 2


def test_when_constructed_then_reputation_rank_is_1():
    sut = player.Player(uuid.uuid4())

    assert sut.reputation_rank == 1


def test_when_constructed_then_stats_are_0():
    sut = player.Player(uuid.uuid4())

    assert sut.pow == 0
    assert sut.agi == 0
    assert sut.sta == 0
    assert sut.chi == 0
    assert sut.wit == 0


def test_when_constructed_then_town_is_ctor_value():
    town = uuid.uuid4()

    sut = player.Player(town)

    assert sut.town == town
