def spoonerize(words):
    words_split = words.split()
    first_half = words_split[1][0] + words_split[0][1:]
    second_half = words_split[0][0] + words_split[1][1:]
    return ' '.join([first_half, second_half])
