import re

def to_camel_case(text):
    if not text:
        return ''
    text_split = re.split('\-|\_', text)
    ret = text_split[0]
    for i in range(1, len(text_split)):
        ret += text_split[i][0].upper() + text_split[i][1:]
    return ret