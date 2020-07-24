def scrabble_score(st): 
    return sum(dict_scores.get(ch, 0) for ch in st.upper())