def cap_me(arr):
    return [name[0].upper() + name[1:].lower() if name else "" for name in arr] if arr else []
