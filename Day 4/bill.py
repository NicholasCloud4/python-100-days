import random

friends = ["Alice", "Bob", "Charlie", "David"]
print(friends)

# Randomly select a friend to pay the bill
payer = random.choice(friends)
print(f"{payer} will pay the bill.")