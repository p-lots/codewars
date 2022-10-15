import math

def gcdi(x, y):
    x, y = abs(x), abs(y)
    return math.gcd(x, y)

def lcmu(a, b):
    a, b = abs(a), abs(b)
    t = gcdi(a, b)
    return a // t * b if t > 0 else 0

def som(a, b):
    return a + b

def maxi(a, b):
    return max(a, b)

def mini(a, b):
    return min(a, b)

def oper_array(fct, arr, init):
    ret = [fct(arr[0], init)]
    for elem in arr[1:]:
        ret.append(fct(ret[-1], elem))
    return ret
