def star_sign(date):
    if date.month == 1 and date.day >= 21 or date.month == 2 and date.day <= 19:
        return 'Aquarius'
    elif date.month == 2 and date.day >= 20 or date.month == 3 and date.day <= 20:
        return 'Pisces'
    elif date.month == 3 and date.day >= 21 or date.month == 4 and date.day <= 20:
        return 'Aries'
    elif date.month == 4 and date.day >= 21 or date.month == 5 and date.day <= 21:
        return 'Taurus'
    elif date.month == 5 and date.day >= 22 or date.month == 6 and date.day <= 21:
        return 'Gemini'
    elif date.month == 6 and date.day >= 22 or date.month == 7 and date.day <= 22:
        return 'Cancer'
    elif date.month == 7 and date.day >= 23 or date.month == 8 and date.day <= 23:
        return 'Leo'
    elif date.month == 8 and date.day >= 24 or date.month == 9 and date.day <= 23:
        return 'Virgo'
    elif date.month == 9 and date.day >= 24 or date.month == 10 and date.day <= 23:
        return 'Libra'
    elif date.month == 10 and date.day >= 24 or date.month == 11 and date.day <= 22:
        return 'Scorpio'
    elif date.month == 11 and date.day >= 23 or date.month == 12 and date.day <= 21:
        return 'Sagittarius'
    return 'Capricorn'