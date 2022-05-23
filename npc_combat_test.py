from uuid import uuid4
import pytest
from npc_combat import roll_for_clash_value, get_npc_clash_values, get_mod_value, get_mod_message, clash
from character import Character


def test_roll_for_clash_value():
    assert roll_for_clash_value(1) == "Hi"
    assert roll_for_clash_value(2) == "Mid"
    assert roll_for_clash_value(3) == "Lo"
    assert roll_for_clash_value(4) == "Lo"
    assert roll_for_clash_value(5) == "Mid"
    assert roll_for_clash_value(6) == "Hi"


def test_get_mod_value():
    assert get_mod_value(1) == "Wolf"
    assert get_mod_value(2) == "Normal"
    assert get_mod_value(3) == "Normal"
    assert get_mod_value(4) == "Normal"
    assert get_mod_value(5) == "Normal"
    assert get_mod_value(6) == "Star"


def test_get_mod_message():
    assert get_mod_message("Star") == "Defense is reversal."
    assert get_mod_message("Wolf") == "Defense is reversal."
    assert get_mod_message("Any") == "No modification."
    assert get_mod_message("Other") == "No modification."
    assert get_mod_message("Mod Value") == "No modification."
    assert get_mod_message("2sx0d7e#@S53#DS%^)^") == "No modification."


def test_get_npc_clash_values():
    actual = get_npc_clash_values()

    atk = actual[0]
    blk = actual[1]
    mod = actual[2]

    assert atk in ['Hi', 'Lo', 'Mid']
    assert blk in ['Hi', 'Lo', 'Mid']
    assert mod in ['Wolf', 'Star', 'Normal']


clash_test_data_atk_blk = [
    ("LO", "LO", "LO", "LO", 0, 0),
    ("LO", "HI", "LO", "LO", 1, 0),
    ("LO", "LO", "LO", "HI", 0, 1),
    ("LO", "HI", "LO", "HI", 1, 1),
]
@pytest.mark.parametrize("player_atk, player_blk, npc_atk, npc_blk, expected_player_damage, expected_npc_damage", clash_test_data_atk_blk)
def test_clash_atk_blk(player_atk, player_blk, npc_atk, npc_blk, expected_player_damage, expected_npc_damage):
    player = Character()
    npc = Character()
    player_hp_before_clash = player.hp
    npc_hp_before_clash = npc.hp
    npc_mod = uuid4()

    clash(player_atk, player_blk, "foo", player, npc_atk, npc_blk, npc_mod, npc)

    assert player_hp_before_clash - player.hp == expected_player_damage
    assert npc_hp_before_clash - npc.hp == expected_npc_damage


clash_test_data_npc_mod = [
    ("Wolf", "LO", "LO", 1),
    ("Wolf", "LO", "HI", 0),
    ("Star", "LO", "LO", 1),
    ("Star", "LO", "HI", 0),
    (uuid4(), "LO", "LO", 0),
    (uuid4(), "LO", "HI", 0),
]
@pytest.mark.parametrize("npc_mod, player_atk, npc_blk, expected_player_damage", clash_test_data_npc_mod)
def test_clash_npc_mod(npc_mod, player_atk, npc_blk, expected_player_damage):
    player = Character()
    npc = Character()
    player_hp_before_clash = player.hp

    clash(player_atk, "LO", "foo", player, "LO", npc_blk, npc_mod, npc)

    assert player_hp_before_clash - player.hp == expected_player_damage


def test_clash_player_mod():
    player = Character()
    npc = Character()
    npc_hp_before_clash = npc.hp

    clash("foo1", "HI", "Reversal", player, "HI", "foo1", "foo3", npc)

    assert npc.hp == npc_hp_before_clash - 1
