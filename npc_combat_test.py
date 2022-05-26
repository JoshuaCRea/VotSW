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

    clash(player_atk, player_blk, uuid4(), player, npc_atk, npc_blk, npc_mod, npc)

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

    clash(player_atk, "LO", uuid4(), player, "LO", npc_blk, npc_mod, npc)

    assert player.hp == player_hp_before_clash - expected_player_damage


clash_test_data_player_mod_reversal = [
    ("Reversal", "LO", "LO", 1),
    ("Reversal", "LO", "HI", 0),
    (uuid4(), "LO", "LO", 0), # TODO: consider removing this once tests for other specials are written
    (uuid4(), "LO", "HI", 0),
]
@pytest.mark.parametrize("player_mod, player_blk, npc_atk, expected_npc_damage", clash_test_data_player_mod_reversal)
def test_clash_player_mod_reversal(player_mod, player_blk, npc_atk, expected_npc_damage):
    player = Character()
    npc = Character()
    npc_hp_before_clash = npc.hp

    clash("HI", player_blk, player_mod, player, npc_atk, "HI", uuid4(), npc)

    assert npc.hp == npc_hp_before_clash - expected_npc_damage


clash_test_data_player_mod_overwhelm = [
    ("HI", "LO", 0),
]
@pytest.mark.parametrize("player_blk, npc_atk, expected_player_damage", clash_test_data_player_mod_overwhelm)
def test_clash_player_mod_overwhelm(player_blk, npc_atk, expected_player_damage):
    player = Character()
    npc = Character()
    player_hp_before_clash = player.hp

    clash("HI", player_blk, "Overwhelm", player, npc_atk, "LO", uuid4(), npc)

    actual = player.hp
    expected = player_hp_before_clash - expected_player_damage
    assert actual == expected