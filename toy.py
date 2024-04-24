import random

class Toy:
    def __init__(self, name, quantity, weight):
        self.id = random.randint(1, 1000)
        self.name = name
        self.quantity = quantity
        self.weight = weight
