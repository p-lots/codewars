# -*- coding: utf-8 -*-
def dative(word):
    front_vowel = u'eéiíöőüű'
    back_vowel = u'aáoóuú'
    for letter in word[::-1]:
        if letter in front_vowel:
            return word + 'nek'
        elif letter in back_vowel:
            return word + 'nak'
    return word