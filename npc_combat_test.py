from npc_combat import roll_for_clash_value, get_kos_clash_values, get_mod_value, get_mod_message


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


def test_get_kos_clash_values():
    actual = get_kos_clash_values()

    kos_atk = actual[0]
    kos_blk = actual[1]
    kos_mod = actual[2]

    assert kos_atk in ['Hi', 'Lo', 'Mid']
    assert kos_blk in ['Hi', 'Lo', 'Mid']
    assert kos_mod in ['Wolf', 'Star', 'Normal']
