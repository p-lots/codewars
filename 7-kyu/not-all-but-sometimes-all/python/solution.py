def remove(text, what):
    replaced = ''.join(ch for ch in text)
    for ch, count in what.items():
        replaced = replaced.replace(ch, '', count)
    return replaced
