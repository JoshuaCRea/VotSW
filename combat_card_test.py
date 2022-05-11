import random
import sys

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
