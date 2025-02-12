def deemojify(emote_string):
    emoji_dict = {
        ':)': '0', 
        ':D': '1', 
        '>(': '2', 
        '>:C': '3', 
        ':/': '4', 
        ':|': '5', 
        ':O': '6', 
        ';)': '7', 
        '^.^': '8', 
        ':(': '9'
    }
    digits = emote_string.split('  ')
    translated_str = []
    for word in digits:
        word_split = word.split(' ')
        translated_word = [emoji_dict[emote] for emote in word_split]
        letter = chr(int(''.join(ch for ch in translated_word)))
        translated_str.append(letter)
    return ''.join(translated_str)
