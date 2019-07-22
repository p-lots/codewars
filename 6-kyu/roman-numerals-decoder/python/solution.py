def solution(roman):
    roman_lst = list(roman)
    lookup_table = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10,
        'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400,
        'D': 500, 'CM': 900, 'M': 1000}
    to_add = ''
    ret = 0
    while roman_lst:
        to_add = roman_lst.pop(0)
        if roman_lst:
            if lookup_table[roman_lst[0]] > lookup_table[to_add]:
                to_add += roman_lst.pop(0)
        ret += lookup_table[to_add]
        to_add = ''
    return ret