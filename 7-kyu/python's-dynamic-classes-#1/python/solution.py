import re

def class_name_changer(cls, new_name):
    name_regex = re.compile('^[A-Z][A-Za-z0-9]+$')
    if not name_regex.match(new_name):
        raise Exception
    cls.__name__ = new_name