def alphabet_position(text):
    text_split = ''.join(text.lower().split())
    letters = [item for item in text_split if item.isalpha()]
    return ' '.join(str(ord(ch) - ord('a') + 1) for ch in letters)
    #return ret