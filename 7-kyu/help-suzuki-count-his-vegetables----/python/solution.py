from collections import Counter

def count_vegetables(strng):
    strng_split = strng.split()
    strng_split = [elem for elem in strng_split if elem != 'chopsticks']
    strng_count = Counter(strng_split)
    strng_count = [(k, v) for k, v in strng_count.items()]
    return sorted([(cnt, elem) for elem, cnt in strng_count], key=lambda elem: (elem[0], elem[1]), reverse=True)
