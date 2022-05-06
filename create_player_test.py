import random
import uuid

import create_player


EXPECTED_TOWN_OPTIONS = {
    1: "Leap-Creek",
    2: "Blackstone",
    3: "Firefen",
    4: "Undervale",
    5: "Pouch"
}


def test_create_player(monkeypatch):
    selected_town = uuid.uuid4()
    monkeypatch.setattr(create_player, "_select_town", lambda: selected_town)

    actual = create_player.create_player()

    assert actual.town == selected_town


def test_select_town(monkeypatch):
    selected_town_number = random.choice(list(EXPECTED_TOWN_OPTIONS.keys()))
    monkeypatch.setattr('builtins.input', lambda _: selected_town_number)

    actual = create_player._select_town()

    assert actual == EXPECTED_TOWN_OPTIONS[selected_town_number]


def test_get_intro_statement():
    actual = create_player.get_intro_statement()

    assert actual == "You are a student of kung fu in the Valley of the Star. " +\
                     "You were born and raised in one of the five towns of the valley. " +\
                     "They are: Leap-Creek, Blackstone, Firefen, Undervale, and Pouch."
