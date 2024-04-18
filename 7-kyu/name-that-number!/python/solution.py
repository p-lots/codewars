def name_that_number(x):
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if x < 10:
        return ones[x]
    elif 10 <= x < 20:
        return teens[x % 10]
    else:
        tens_place = x // 10
        ones_place = x % 10
        return f'{tens[tens_place]} {ones[ones_place]}' if ones_place > 0 else f'{tens[tens_place]}'
