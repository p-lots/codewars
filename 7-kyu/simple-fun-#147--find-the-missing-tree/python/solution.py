from collections import Counter

def find_the_missing_tree(trees):
    counts = Counter(trees)
    biggest = max(counts.values())
    for tree, cnt in counts.items():
        if cnt == biggest - 1:
            return tree
