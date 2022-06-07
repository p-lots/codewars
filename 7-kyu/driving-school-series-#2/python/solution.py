def cost(mins):
    cost = 0
    if mins > 5:
        cost = 30
    mins -= 60
    while mins > 5:
        cost += 10
        mins -= 30
    return cost
