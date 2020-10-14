def find_nth_occurrence(substring, strng, occurrence=1):
    curr_occ = 0
    for i in range(len(strng)):
        if strng[i:i + len(substring)] == substring:
            curr_occ += 1
        if curr_occ == occurrence:
            return i
    return -1
