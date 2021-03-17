def string_task(s):
    return ''.join('' if ch in 'aeiouy' else f'.{ch}' for ch in s.lower())
