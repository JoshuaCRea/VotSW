import random
import sys

import pytest

import combat_card


def test_get_combat_cards():
    actual = combat_card.get_combat_cards()

    assert actual == [
        combat_card.Combat_Card("Hi", "Hi"),
        combat_card.Combat_Card("Hi", "Mid"),
        combat_card.Combat_Card("Hi", "Lo"),
        combat_card.Combat_Card("Mid", "Hi"),
        combat_card.Combat_Card("Mid", "Mid"),
        combat_card.Combat_Card("Mid", "Lo"),
        combat_card.Combat_Card("Lo", "Hi"),
        combat_card.Combat_Card("Lo", "Mid"),
        combat_card.Combat_Card("Lo", "Lo"),
        combat_card.Combat_Card("Mid", "Lo")
    ]


def test_get_selected_card(monkeypatch):
    min_remaining_cards_in_hand_where_player_would_be_asked_for_input = 2
    cards_remaining_in_hand = random.randint(min_remaining_cards_in_hand_where_player_would_be_asked_for_input, sys.maxsize)
    player_choice = random.randint(min_remaining_cards_in_hand_where_player_would_be_asked_for_input, cards_remaining_in_hand)
    monkeypatch.setattr('builtins.input', lambda _: player_choice)

    actual = combat_card.get_selected_card(cards_remaining_in_hand)

    assert actual == player_choice


def test_get_player_mod_message():
    actual = combat_card.get_player_mod_message()

    assert actual == '<!! Player mod messages are not yet implemented. !!>'


def test_get_two_hands():
    actual = combat_card.get_two_hands()

    assert len(actual) == 2

    assert len(actual[0]) == 5
    assert all([isinstance(card, combat_card.Combat_Card) for card in actual[0]])

    assert len(actual[1]) == 5
    assert all([isinstance(card, combat_card.Combat_Card) for card in actual[1]])


def test_get_current_hand_returns_round_one_hand_if_round_one_hand_not_empty():
    round_one_hand = [object]
    round_two_hand = [object]

    actual = combat_card.get_current_hand(round_one_hand, round_two_hand)

    assert actual == round_one_hand


def test_get_current_hand_returns_round_two_hand_if_round_one_hand_is_empty():
    round_one_hand = []
    round_two_hand = [object]

    actual = combat_card.get_current_hand(round_one_hand, round_two_hand)

    assert actual == round_two_hand


get_selected_card_special_test_data = [
    (1, "Normal"),
    (2, "School Special"),
    (3, "Random Special")
]
@pytest.mark.parametrize("player_option, expected", get_selected_card_special_test_data)
def test_get_selected_card_special(monkeypatch, player_option, expected):
    monkeypatch.setattr('builtins.input', lambda _: player_option)

    actual = combat_card.get_selected_card_special()

    assert actual == expected
