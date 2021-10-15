def test(r):
    average = round(sum(r) / len(r), 3)
    high_count = r.count(10) + r.count(9)
    avg_count = r.count(8) + r.count(7)
    low_count = len(r) - high_count - avg_count
    marks = {'h': high_count, 'a': avg_count, 'l': low_count}
    ret = [average, marks]
    if marks['a'] == 0 and marks['l'] == 0:
        ret.append('They did well')
    return ret