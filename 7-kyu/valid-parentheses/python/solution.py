def valid_parentheses(paren_str):
    stack = []
    for paren in paren_str:
        if paren == '(':
            stack.append(paren)
            continue
        if stack and stack[0] == '(':
            stack.pop(0)
        else:
            return False
    return len(stack) == 0
