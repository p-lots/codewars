from math import ceil

def wallpaper(l, w, h):
    number_words = ["zero", "one", "two", "three", "four", "five",
               "six", "seven", "eight", "nine", "ten",
               "eleven", "twelve", "thirteen", "fourteen", "fifteen",
               "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
    if not (l > 0.0 and w > 0.0 and h > 0.0):
        return number_words[0]
    index = int(ceil(((2.0 * w * h) + (2.0 * h * l)) * 1.15 / 5.2))
    return number_words[index]