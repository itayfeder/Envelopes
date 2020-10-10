import random


class Envelope:
    def __init__(self):
        self.money = random.randint(1, 1000)
        self.used = False