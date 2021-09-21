def max_redigit(num): 
    if not 99 < num < 1000:
        return None
    result = int(''.join(sorted(str(num), reverse=True)))
    return result if result >= num else None