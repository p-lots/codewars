def calculate(num1, operation, num2): 
    if operation not in '+-*/':
        return None
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return None
        return num1 / num2
    