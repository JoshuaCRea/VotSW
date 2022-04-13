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


class Card:
    def __init__(self, attack, block):
        self.attack = attack
        self.block = block


card1 = Card("Hi", "Hi")
card2 = Card("Hi", "Mid")
card3 = Card("Hi", "Lo")

print(card1.attack)
print(card1.block)
print(card2.attack)
print(card2.block)
print(card3.attack)
print(card3.block)
