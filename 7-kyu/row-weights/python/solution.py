def row_weights(array):
    team_one = sum(array[i] for i in range(0, len(array), 2))
    team_two = sum(array[i] for i in range(1, len(array), 2))
    return (team_one, team_two)