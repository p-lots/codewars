def name_in_str(strng, name):
    name = [char for char in name.lower()]
    for ch in strng.lower():
        if name and ch == name[0]:
            name.pop(0)
    return len(name) == 0