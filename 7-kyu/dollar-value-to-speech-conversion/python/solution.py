def dollar_to_speech(value):
    val = value.replace('$', '')
    if val[0] == '-':
        return 'No negative numbers are allowed!'
    dollars, cents = map(int, val.split('.'))
    if cents == 0:
        return f'{dollars} dollar{"s" if dollars != 1 else ""}.'
    if dollars == 0:
        return f'{cents} cent{"s" if cents > 1 else ""}.'
    return f'{dollars} dollars and {cents} cents.'
