import random
import sys

from combat_card import *


def test_get_combat_cards():
    actual = get_combat_cards()

    assert actual == [
        Combat_Card(CombatPosture.HIGH, CombatPosture.HIGH),
        Combat_Card(CombatPosture.HIGH, CombatPosture.MID),
        Combat_Card(CombatPosture.HIGH, CombatPosture.LOW),
        Combat_Card(CombatPosture.MID, CombatPosture.HIGH),
        Combat_Card(CombatPosture.MID, CombatPosture.MID),
        Combat_Card(CombatPosture.MID, CombatPosture.LOW),
        Combat_Card(CombatPosture.LOW, CombatPosture.HIGH),
        Combat_Card(CombatPosture.LOW, CombatPosture.MID),
        Combat_Card(CombatPosture.LOW, CombatPosture.LOW),
        Combat_Card(CombatPosture.MID, CombatPosture.LOW)
    ]


def test_combat_card_string_override():
    sut = Combat_Card(CombatPosture.HIGH, CombatPosture.LOW)

    actual = str(sut)

    assert actual == "Attack: HIGH, Block: LOW"


def test_get_selected_card(monkeypatch):
    min_remaining_cards_in_hand_where_player_would_be_asked_for_input = 2
    cards_remaining_in_hand = random.randint(min_remaining_cards_in_hand_where_player_would_be_asked_for_input, sys.maxsize)
    player_choice = random.randint(min_remaining_cards_in_hand_where_player_would_be_asked_for_input, cards_remaining_in_hand)
    monkeypatch.setattr('builtins.input', lambda _: player_choice)

    actual = get_selected_card(cards_remaining_in_hand)

    assert actual == player_choice


def test_get_player_mod_message():
    actual = get_player_mod_message()

    assert actual == '<!! Player mod messages are not yet implemented. !!>'
