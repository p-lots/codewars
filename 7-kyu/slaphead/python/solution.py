def bald(s):
    count = s.count('/')
    second = ''
    first = s.replace('/', '-')
    if count > 5:
        second = 'Hobo!'
    elif count > 2:
        second = 'Careless!'
    elif count == 2:
        second = 'Homer!'
    elif count == 1:
        second = 'Unicorn!'
    else:
        second = 'Clean!'
    return [first, second]