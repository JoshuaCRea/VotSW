import player


TOWN_OPTIONS = {
    1: "Leap-Creek",
    2: "Blackstone",
    3: "Firefen",
    4: "Undervale",
    5: "Pouch"
}


def create_player():
    selected_town = _select_town()
    return player.Player(selected_town)


def get_intro_statement():
    return 'You are a student of kung fu in the Valley of the Star. ' +\
           'You were born and raised in one of the five towns of the valley. ' +\
           f'They are: {TOWN_OPTIONS[1]}, {TOWN_OPTIONS[2]}, {TOWN_OPTIONS[3]}, {TOWN_OPTIONS[4]}, and {TOWN_OPTIONS[5]}.'


def _select_town():
    for k, v in TOWN_OPTIONS.items():
        print(f'{k}. {v}')
    choice = int(input("Choose a town from the preceeding list to be your home: "))
    return TOWN_OPTIONS[choice]
