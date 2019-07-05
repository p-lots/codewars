def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def arithmetic(a, b, operator):
    lookup_table = { "add": add(a, b), "subtract": subtract(a, b), "multiply": multiply(a, b), "divide": divide(a, b) }
    return lookup_table[operator]