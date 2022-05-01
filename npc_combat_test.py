import random
import sys
from npc_combat import get_attack_value, get_blk_value, get_mod_value, get_mod_message


def test_get_attack_value():
    assert get_attack_value(1) == "Hi"
    assert get_attack_value(2) == "Mid"
    assert get_attack_value(3) == "Lo"
    assert get_attack_value(4) == "Lo"
    assert get_attack_value(5) == "Mid"
    assert get_attack_value(6) == "Hi"


def test_get_blk_value():
    assert get_blk_value(1) == "Hi"
    assert get_blk_value(2) == "Mid"
    assert get_blk_value(3) == "Lo"
    assert get_blk_value(4) == "Lo"
    assert get_blk_value(5) == "Mid"
    assert get_blk_value(6) == "Hi"


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


import combat_card
def test_get_selected_card(monkeypatch):
    min_cards_in_hand_where_player_would_be_asked_for_input = 2
    cards_remaining_in_hand = random.randint(2, sys.maxsize)
    player_choice = random.randint(min_cards_in_hand_where_player_would_be_asked_for_input, cards_remaining_in_hand)
    monkeypatch.setattr('builtins.input', lambda _: player_choice)
    actual = combat_card.get_selected_card(cards_remaining_in_hand)

    assert actual == player_choice
