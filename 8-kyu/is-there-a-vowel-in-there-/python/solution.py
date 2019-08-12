def is_vow(inp):
    return [chr(number) if chr(number) in 'aeiou' else number for number in inp]