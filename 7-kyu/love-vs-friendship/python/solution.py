def words_to_marks(s):
    return sum(ord(ch) - ord('a') + 1 for ch in s)