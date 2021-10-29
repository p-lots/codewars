def expression_out(exp):
    NUMBERS = {'1': 'One', '2': 'Two', '3': 'Three',
               '4': 'Four', '5': 'Five', '6': 'Six',
               '7': 'Seven', '8': 'Eight', '9': 'Nine', '10': 'Ten'}
    operand1, operator, operand2 = exp.split()
    return f'{NUMBERS[operand1]} {OPERATORS[operator]}{NUMBERS[operand2]}' if operator in OPERATORS else 'That\'s not an operator!'
