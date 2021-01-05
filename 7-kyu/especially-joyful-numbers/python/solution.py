def number_joy(n):
    digit_sum = sum(map(int, str(n)))
    digit_sum_rev = int(str(digit_sum)[::-1])
    return digit_sum * digit_sum_rev == n
