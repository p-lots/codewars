def byte_to_set(byte):
    byte_str = f'{byte:b}'.zfill(8)
    return {i for i, bit in enumerate(list(byte_str)) if bit == '1'}
