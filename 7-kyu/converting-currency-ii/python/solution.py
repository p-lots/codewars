def solution(to_cur, values):
    curr_conv = {'USD': 1.1363636, 'EUR': 1.0/1.1363636}
    pre = '$' if to_cur == 'USD' else ''
    post = '€' if to_cur == 'EUR' else ''
    return [f'{pre}{(amt * curr_conv[to_cur]):0,.2f}{post}' for amt in values]