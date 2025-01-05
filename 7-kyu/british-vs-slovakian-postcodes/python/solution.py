import re # you can use re, but do not have to

def which_postcode(postcode):
    GB_REGEX = r'^[a-z]{1,2}[0-9]{1,2} [0-9][a-z]{2}$'
    SK_REGEX = r'^[0-9]{3} [0-9]{2}$'
    code_trimmed = postcode.strip()
    if re.match(GB_REGEX, code_trimmed, re.IGNORECASE) is not None:
        return 'GB'
    if re.match(SK_REGEX, code_trimmed) is not None:
        return 'SK'
    return 'Not valid'
    