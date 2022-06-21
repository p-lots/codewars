import re

def is_valid(idn):
    return len(idn) > 0 and re.match(r'^[a-z_\$][a-z_\$0-9]*$', idn, re.I) != None
