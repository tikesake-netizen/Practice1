def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) // 2
    chickens = numheads - rabbits
    return chickens, rabbits


chickens, rabbits = solve(5, 14)

print("Chickens:", chickens)
print("Rabbits:", rabbits)