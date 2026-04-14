def max_possible_score(points, seen): 
    return sum(score * 2 if q in seen else score for q, score in points.items())