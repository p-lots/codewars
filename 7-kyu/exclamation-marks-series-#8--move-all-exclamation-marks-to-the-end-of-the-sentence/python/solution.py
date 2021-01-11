def remove(s):
    no_exc = s.replace('!', '')
    return f"{no_exc}{'!' * (len(s) - len(no_exc))}"
