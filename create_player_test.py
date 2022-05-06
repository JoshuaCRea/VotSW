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

    actual = create_player.create_player(selected_town)

    assert actual.town == selected_town


def test_select_town(monkeypatch):
    selected_town_number = random.choice(list(EXPECTED_TOWN_OPTIONS.keys()))
    monkeypatch.setattr('builtins.input', lambda _: selected_town_number)

    actual = create_player._select_town()

    assert actual == EXPECTED_TOWN_OPTIONS[selected_town_number]
