def count_animals(sentence):
    return sum(int(n) for n in filter(str.isdigit, sentence.split()))