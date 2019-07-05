def golf_score_calculator(par_string, score_string):
    return sum(int(score_string[i]) - int(par_string[i]) for i in range(len(par_string)))