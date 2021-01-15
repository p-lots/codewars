from collections import Counter
import operator

def most_frequent_item_count(collection):
    if not collection:
        return 0
    cnt = Counter(collection)
    return max(cnt.items(), key=operator.itemgetter(1))[1]