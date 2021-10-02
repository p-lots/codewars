def cool_string(s):
    return all(ch.isalpha() for ch in s) and all(lhs.isupper() != rhs.isupper() or lhs.islower() != rhs.islower() for lhs, rhs in zip(s, s[1:]))
