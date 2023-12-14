from string import ascii_lowercase

def rank(st, we, n):
    if not st:
        return 'No participants'
    st = st.split(',')
    if len(st) < n:
        return 'Not enough participants'
    letter_scores = {letter: value for value, letter in enumerate(ascii_lowercase, 1)}
    names_scores = [((sum(letter_scores.get(ch.lower()) for ch in name) + len(name)) * we[i], name) for i, name in enumerate(st)]
    names_sorted = sorted(names_scores, key=lambda pair: pair[1])
    names_sorted = sorted(names_sorted, key=lambda pair: pair[0], reverse=True)
    return names_sorted[n - 1][1]
