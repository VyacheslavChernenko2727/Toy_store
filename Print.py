from toy_store import ToyStore

toy_store = ToyStore()
toy_store.add_toy("Кукла", 10, 30)
toy_store.add_toy("Мяч", 20, 50)
toy_store.update_weight(1, 40)

winners = toy_store.distribute_toys(5)
for winner in winners:
    print("Победитель:", winner.name)