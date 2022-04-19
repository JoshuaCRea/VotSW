'''
Card 1 ATK Hi BLK Hi
Card 2 ATK Hi BLK Mid
Card 3 ATK Hi BLK Lo
Card 4 ATK Mid BLK Hi
Card 5 ATK Mid BLK Mid
Card 6 ATK Mid BLK Lo
Card 7 ATK Lo BLK Hi
Card 8 ATK Lo BLK Mid
Card 9 ATK Lo BLK Lo
Card 10 ATK Mid BLK Lo

Beginning of fight, random of five of these held by player
Other five reamin in list
'''


class Combat_Card:
    def __init__(self, attack, block):
        self.attack = attack
        self.block = block

    def __str__(self):
        return f'Card - Attack: {self.attack}, Block: {self.block}'


def get_combat_cards():
    card1 = Combat_Card("Hi", "Hi")
    card2 = Combat_Card("Hi", "Mid")
    card3 = Combat_Card("Hi", "Lo")
    card4 = Combat_Card("Mid", "Hi")
    card5 = Combat_Card("Mid", "Mid")
    card6 = Combat_Card("Mid", "Lo")
    card7 = Combat_Card("Lo", "Hi")
    card8 = Combat_Card("Lo", "Mid")
    card9 = Combat_Card("Lo", "Lo")
    card10 = Combat_Card("Mid", "Lo")

    combat_cards = [card1, card2, card3, card4, card5, card6, card7, card8, card9, card10]
    return combat_cards
