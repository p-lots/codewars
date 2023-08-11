def encode_cd(n):
    n_bin = f'{n:08b}'[::-1]
    encoded = 'P'
    for digit in n_bin:
        if digit == '1':
            encoded += 'L' if encoded[-1] == 'P' else 'P'
        else:
            encoded += encoded[-1]
    return encoded
