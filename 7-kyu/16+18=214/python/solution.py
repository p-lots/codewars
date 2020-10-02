def add(num1, num2):
    num1, num2 = min(num1, num2), max(num1, num2)
    num1_str = str(num1)
    num2_str = str(num2)
    while len(num1_str) < len(num2_str):
        num1_str = '0' + num1_str
    ret = ''
    for lhs, rhs in zip(num1_str, num2_str):
        result = int(lhs) + int(rhs)
        ret += str(result)
    return int(ret)