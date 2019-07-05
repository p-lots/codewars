from collections import Counter

def find_most_frequent(l):
    if not l:
        return set([])
    c = Counter(l)
    c_inv = {}
    for key, val in c.items():
    	if val not in c_inv:
    		c_inv[val] = [key]
    	else:
    		c_inv[val].append(key)
    return set(c_inv[c.most_common()[0][1]])