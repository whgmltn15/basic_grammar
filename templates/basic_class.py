import random

class make_character:

    def __init__(self):
        self.hp = random.randrange(1, 20)
        self.mp = random.randrange(1, 40)
        self.q = random.randrange(1, 4)
        self.p = random.randrange(0, -5)

    def attack(self):
        return self.q

    def attacked(self):
        return self.p