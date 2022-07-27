def goto(level, button):
    if not isinstance(level, int) or not 0 <= level <= 3:
        return 0
    if not isinstance(button, str) or not 0 <= int(button) <= 3:
        return 0
    return int(button) - level
