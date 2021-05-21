import operator

def calculator(x, y, op):
    if type(x) != int or type(y) != int or type(op) != str or op not in '+-*/':
        return 'unknown value'
    lookup = {'+': operator.add, '-': operator.sub,
             '*': operator.mul, '/': operator.truediv
    }
    return lookup[op](x, y)