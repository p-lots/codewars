def scoreboard(strng):
    first, second = None, None
    scores = ["nil", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for word in strng.split():
        if word in scores:
            if first == None:
                first = scores.index(word)
            elif second == None:
                second = scores.index(word)
    return [first, second]