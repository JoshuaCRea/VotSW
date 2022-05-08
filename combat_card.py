from enum import Enum, auto, unique


class Combat_Card:
    def __init__(self, attack, block):
        self.attack = attack
        self.block = block

    def __str__(self):
        return f'Card - Attack: {self.attack}, Block: {self.block}'

    def __eq__(self, other):
        return self.attack == other.attack and \
               self.block == other.block


@unique
class CombatPosture(Enum):
    LOW = auto()
    MID = auto()
    HIGH = auto()


def get_combat_cards():
    return [
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


def get_selected_card(cards_remaining_in_hand):
    selected_card_number = int(input(f'\nPlayer, please select a card [1-{cards_remaining_in_hand}]: '))
    return selected_card_number


def get_player_mod_message():
    return "<!! Player mod messages are not yet implemented. !!>"
