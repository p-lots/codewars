def last_survivor(letters, coords): 
    letters = [letter for letter in letters]
    for coord in coords:
        del letters[coord]
    return ''.join(letters)
