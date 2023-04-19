def ensure_question(s):
    return s if s and s[-1] == '?' else f'{s}?'
