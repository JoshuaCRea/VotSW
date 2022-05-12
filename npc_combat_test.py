import pytest
from npc_combat import roll_for_clash_value, get_npc_clash_values, get_mod_value, get_mod_message, clash
from player import Player


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

    kos_atk = actual[0]
    kos_blk = actual[1]
    kos_mod = actual[2]

    assert kos_atk in ['Hi', 'Lo', 'Mid']
    assert kos_blk in ['Hi', 'Lo', 'Mid']
    assert kos_mod in ['Wolf', 'Star', 'Normal']


clash_test_data = [
    ("LO", "LO", "LO", "LO", 0, 0),
    ("LO", "HI", "LO", "LO", 1, 0),
    ("LO", "LO", "LO", "HI", 0, 1),
    ("LO", "HI", "LO", "HI", 1, 1),
]
@pytest.mark.parametrize("player_atk, player_blk, npc_atk, npc_blk, expected_player_damage, expected_npc_damage", clash_test_data)
def test_clash(player_atk, player_blk, npc_atk, npc_blk, expected_player_damage, expected_npc_damage):
    player = Player()
    npc = Player()
    player_hp_before_clash = player.hp
    npc_hp_before_clash = npc.hp

    clash(player_atk, player_blk, player, npc_atk, npc_blk, npc)

    assert player_hp_before_clash - player.hp == expected_player_damage
    assert npc_hp_before_clash - npc.hp == expected_npc_damage
