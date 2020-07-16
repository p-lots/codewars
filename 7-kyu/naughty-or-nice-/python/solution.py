def get_nice_names(people):
    return [dct['name'] for dct in people if dct['was_nice']]

def get_naughty_names(people):
    return [dct['name'] for dct in people if not dct['was_nice']]