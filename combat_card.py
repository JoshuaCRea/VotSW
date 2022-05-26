import random


class Combat_Card:
    def __init__(self, attack, block):
        self.attack = attack
        self.block = block

    def __str__(self):
        return f'Card - Attack: {self.attack}, Block: {self.block}'

    def __eq__(self, other):
        return self.attack == other.attack and \
               self.block == other.block


card_special_options = {
    1: "Normal",
    2: "Reversal",
}


def get_combat_cards():
    return [
        Combat_Card("Hi", "Hi"),
        Combat_Card("Hi", "Mid"),
        Combat_Card("Hi", "Lo"),
        Combat_Card("Mid", "Hi"),
        Combat_Card("Mid", "Mid"),
        Combat_Card("Mid", "Lo"),
        Combat_Card("Lo", "Hi"),
        Combat_Card("Lo", "Mid"),
        Combat_Card("Lo", "Lo"),
        Combat_Card("Mid", "Lo")
    ]


def get_selected_card(cards_remaining_in_hand):
    selected_card_number = int(input(f'\nPlayer, please select a card [1-{cards_remaining_in_hand}]: '))
    return selected_card_number


def get_two_hands():
    combat_cards = get_combat_cards()
    random.shuffle(combat_cards)
    round_one_hand = combat_cards[0:5]
    round_two_hand = combat_cards[5:10]
    return round_one_hand, round_two_hand


def get_current_hand(round_one_hand, round_two_hand):
    if len(round_one_hand) > 0:
        return round_one_hand
    return round_two_hand


def get_selected_card_special():
    selected_card_special_num = int(input(f'Player, please select a Special [1-{len(card_special_options)}]: '))
    return card_special_options[selected_card_special_num]
