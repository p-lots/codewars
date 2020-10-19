def num_key_strokes(text):
    return sum(2 if ch.isupper() or ch in '!@#$%^&*()_+{}|:"<>?~' else 1 for ch in text)