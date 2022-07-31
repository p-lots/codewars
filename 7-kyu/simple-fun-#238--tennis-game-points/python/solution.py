LOOKUP = {'love': 0, '15': 1, '30': 2, '40': 3}

def tennis_game_points(score):
    player1_score, player2_score = score.split('-')
    if player2_score == 'all':
        player2_score = player1_score
    return LOOKUP[player1_score] + LOOKUP[player2_score]
