from collections import Counter

def yahtzee_upper(dice):
    score_count = Counter(dice)
    scores = [roll * count for roll, count in score_count.items()]
    upper_score = max(scores)
    return upper_score
