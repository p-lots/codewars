def calculate(strng):
    strng = strng.split()
    num1, num2 = None, None
    oper = None
    for word in strng:
        if word.isdigit():
            if num1 is None:
                num1 = int(word)
            elif num2 is None:
                num2 = int(word)
        if word == 'gains':
            oper = '+'
        if word == 'loses':
            oper = '-'
    return num1 + num2 if oper == '+' else num1 - num2
