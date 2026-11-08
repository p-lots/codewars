from string import ascii_lowercase as alphabet

def count_lonely_letters(text):
    letters = [ch for ch in text.lower() if ch in alphabet]
    return sum(letters.count(letter) == 1 and 
               (chr(ord(letter) - 1) not in letters) and 
               (chr(ord(letter) + 1) not in letters) 
               for letter in letters)
