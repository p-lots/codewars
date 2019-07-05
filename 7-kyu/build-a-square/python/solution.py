def generateShape(n):
    return '\n'.join((''.join('+' for _ in range(n)) for _ in range(n)))