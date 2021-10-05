def sort_vowels(s):
    return '\n'.join(f'|{ch}' if ch.lower() in 'aeiou' else f'{ch}|' for ch in s) if isinstance(s, str) else ''