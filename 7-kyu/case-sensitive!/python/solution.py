import string

def case_sensitive(s):
    if not s:
        return [True, []]
    return [s.islower(), list(filter(lambda ch: ch in string.ascii_uppercase, [letter for letter in s]))]