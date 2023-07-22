# The speeding car: "O='`o"
# The other cars: "X"
def car_crash(road):
    car = "O='`o"
    road = road.split('\n')
    for line in road:
        try:
            car_idx = line.index("O='`o")
            other_idx = line.rindex('X')
            if other_idx > car_idx:
                return True
        except:
            continue
    return False