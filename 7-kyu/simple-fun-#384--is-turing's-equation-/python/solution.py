def is_turing_equation(s):
    eq_split = s.split('=')
    operands = eq_split[0].split('+')
    oper1 = int(operands[0][::-1])
    oper2 = int(operands[1][::-1])
    result = int(eq_split[1][::-1])
    return oper1 + oper2 == result