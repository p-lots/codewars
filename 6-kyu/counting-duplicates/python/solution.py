def duplicate_count(text):
    text = text.lower()
    char_set = []
    counted_set = []
    ret = 0
    for ch in text:
        if ch not in char_set:
            char_set.append(ch)
        elif ch not in counted_set:
            ret += 1
            counted_set.append(ch)
    return ret