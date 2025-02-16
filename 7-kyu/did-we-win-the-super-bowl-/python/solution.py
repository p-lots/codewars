def did_we_win(plays):
    yards_gained = 0
    for play in plays:
        if not play:
            break
        elif play[1] == 'turnover':
            return False
        elif play[1] == 'sack':
            yards_gained -= play[0]
        elif play[1] in ['run', 'pass']:
            yards_gained += play[0]
    return yards_gained > 10
