def add_length(str_):
    return ['{0} {1}'.format(word, len(word)) for word in str_.split()]