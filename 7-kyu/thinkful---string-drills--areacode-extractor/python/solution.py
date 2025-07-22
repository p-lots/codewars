import re

def area_code(text):
    regexp = r'\((\d{3})\)'
    m = re.search(regexp, text)
    if m:
        return m.group(1)
