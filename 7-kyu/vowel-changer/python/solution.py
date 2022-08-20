def vowel_change(txt, vow):
    trans_str = vow * 5
    return txt.translate(str.maketrans('aeiou', trans_str))
