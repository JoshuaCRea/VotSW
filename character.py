class Character:
    def __init__(self):
        self.hp = 5
        self.standing = True
        self.rep_rank = 3
        self.injured = False

    def receive_damage(self, damage_points):
        self.hp = self.hp - damage_points
        if self.hp <= 0:
            self.standing = False
