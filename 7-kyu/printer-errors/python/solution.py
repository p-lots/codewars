import re

def printer_error(s):
    return "{0}/{1}".format(len(re.findall('[nopqrstuvwxyz]', s)), len(s))