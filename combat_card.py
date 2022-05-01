class Combat_Card:
    def __init__(self, attack, block):
        self.attack = attack
        self.block = block

    def __str__(self):
        return f'Card - Attack: {self.attack}, Block: {self.block}'

    def __eq__(self, other):
        return self.attack == other.attack and \
               self.block == other.block


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
