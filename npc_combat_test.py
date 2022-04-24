from npc_combat import get_mod_message


def test_special_mod_wolf():
    assert get_mod_message("Wolf") == "Defense is reversal."


def test_special_mod_star():
    assert get_mod_message("Star") == "Defense is reversal."


def test_default_mod():
    assert get_mod_message("Any") == "No modification."
    assert get_mod_message("Other") == "No modification."
    assert get_mod_message("Mod Value") == "No modification."
    assert get_mod_message("2sx0d7e#@S53#DS%^)^") == "No modification."