import re

def find_glasses(lst):
    for idx, elem in enumerate(lst):
        if re.search(r'O-+O', elem):
            return idx
