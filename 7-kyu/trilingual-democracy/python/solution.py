from collections import Counter

# input is a string of three chars from the set 'D', 'F', 'I', 'K';
# output is a single char from this set
def trilingual_democracy(group):
    group_set = set(group)
    match len(group_set):
        case 1:
            return group[0]
        case 2:
            group_counter = Counter(group)
            return [lang for lang, cnt in group_counter.items() if cnt == 1][0]
        case 3:
            return [lang for lang in ['D', 'F', 'I', 'K'] if lang not in group][0]
