def validate_base(num: str, base: int) -> bool:
    valid_bases = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return all(valid_bases.index(digit) < base for digit in num)
