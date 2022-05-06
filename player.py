INITIAL_HP = 5
INITIAL_COMBAT_STONES = 2
INITIAL_REPUTATION_RANK = 1
INITIAL_POWER = 0
INITIAL_AGILITY = 0
INITIAL_STAMINA = 0
INITIAL_CHI = 0
INITIAL_WIT = 0



class Player:
    def __init__(self, town):
        self.town = town
        self.hp = INITIAL_HP
        self.combat_stones = INITIAL_COMBAT_STONES
        self.reputation_rank = INITIAL_REPUTATION_RANK
        self.pow = INITIAL_POWER
        self.agi = INITIAL_AGILITY
        self.sta = INITIAL_STAMINA
        self.chi = INITIAL_CHI
        self.wit = INITIAL_WIT
