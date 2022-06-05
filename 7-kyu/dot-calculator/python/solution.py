def calculator(txt):
    txt_split = txt.split(' ')
    term1 = len(txt_split[0])
    oper = txt_split[1]
    term2 = len(txt_split[2])
    result = 0
    if oper == '+':
        result = term1 + term2
    elif oper == '-':
        result = term1 - term2
    elif oper == '*':
        result = term1 * term2
    elif oper == '//':
        result = term1 // term2
    return '.' * result
