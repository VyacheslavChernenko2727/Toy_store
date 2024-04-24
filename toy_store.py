from toy import Toy
import random
class ToyStore:
    def __init__(self):
        self.toys = []

    def add_toy(self, name, quantity, weight):
        toy = Toy(name, quantity, weight)
        self.toys.append(toy)

    def update_weight(self, toy_id, weight):
        for toy in self.toys:
            if toy.id == toy_id:
                toy.weight = weight

    def select_toy(self):
        total_weight = sum(toy.weight for toy in self.toys)
        rand = random.uniform(0, total_weight)
        cumulative_weight = 0
        for toy in self.toys:
            cumulative_weight += toy.weight
            if rand <= cumulative_weight:
                return toy

    def distribute_toys(self, num_winners):
        winners = []
        for _ in range(num_winners):
            selected_toy = self.select_toy()
            if selected_toy:
                winners.append(selected_toy)
                selected_toy.quantity -= 1
                self.toys.remove(selected_toy)
        return winners