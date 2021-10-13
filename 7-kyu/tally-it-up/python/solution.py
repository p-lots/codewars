def score_to_tally(score):
    tally_marks = ['', 'a', 'b', 'c', 'd', 'e']
    return ('e <br>' * (score // 5)) + tally_marks[score % 5]