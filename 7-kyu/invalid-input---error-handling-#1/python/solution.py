def get_count(words=''):
    ret = {'vowels': 0, 'consonants': 0}
    if not words or not isinstance(words, str):
        return ret
    ret['vowels'] = sum(1 for ch in words.lower() if ch in 'aeiou')
    ret['consonants'] = sum(1 for ch in words.lower() if ch not in 'aeiou' and ch.isalpha())
    return ret
