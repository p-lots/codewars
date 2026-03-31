def is_kiss(words):
    total_words = len(words.split(' '))
    return 'Good work Joe!' if all(len(word) <= total_words for word in words.split(' ')) else 'Keep It Simple Stupid'
