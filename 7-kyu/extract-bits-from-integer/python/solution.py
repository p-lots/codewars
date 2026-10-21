def extract_bits(field: int, offset: int, length: int) -> int:
    field_b = f'{field:b}'[::-1]
    if length == 0 or offset >= len(field_b):
        return 0
    return int((field_b[offset:offset + length])[::-1], 2)