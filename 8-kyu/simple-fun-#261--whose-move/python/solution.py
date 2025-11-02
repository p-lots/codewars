def whose_move(last_player, win):
    if win:
        return last_player
    return 'black' if last_player == 'white' else 'white'
