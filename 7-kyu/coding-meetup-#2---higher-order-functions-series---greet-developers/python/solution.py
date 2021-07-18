def greet_developers(lst):
    ret = []
    for dct in lst:
        to_append = dct
        to_append['greeting'] = f'Hi {dct["firstName"]}, what do you like the most about {dct["language"]}?'
        ret.append(to_append)
    return ret
