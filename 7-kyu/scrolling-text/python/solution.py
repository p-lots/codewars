def scrolling_text(text):
    return [text[i:].upper() + text[:i].upper() for i in range(len(text))]