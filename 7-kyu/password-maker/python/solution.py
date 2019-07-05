def make_password(phrase):
    ret = ''
    for word in phrase.split():
        if word[0] == 'i' or word[0] == 'I':
            ret += '1'
        elif word[0] == 'o' or word[0] == 'O':
            ret += '0'
        elif word[0] == 's' or word[0] == 'S':
            ret += '5'
        else:
            ret += word[0]
    return ret
