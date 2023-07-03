def fizz_buzz_custom(string_one='Fizz', string_two='Buzz', num_one=3, num_two=5):
    ret = []
    for i in range(1, 101):
        to_append = ''
        if i % num_one == 0:
            to_append += string_one
        if i % num_two == 0:
            to_append += string_two
        if to_append == '':
            to_append = i
        ret.append(to_append)
    return ret
