class Character:
    def __init__(self):
        self.hp = 5
        self.is_alive = True
        self.rep_rank = 3

    def receive_damage(self, damage_points):
        self.hp = self.hp - damage_points
        if self.hp <= 0:
            self.is_alive = False
