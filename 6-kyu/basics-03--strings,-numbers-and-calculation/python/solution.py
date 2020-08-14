def evaluate_expression(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2

def calculate_string(st):
    num1, num2 = '', ''
    oper = ''
    for ch in st:
        if ch.isdigit() or ch == '.':
            if len(oper) == 0:
                num1 += ch
            else:
                num2 += ch
        elif ch in '+-*/':
            oper = ch
    return str(round(evaluate_expression(float(num1), float(num2), oper)))