def hex_string_to_RGB(hex_string): 
    hex_string = hex_string[1:].upper()
    return {'r': int(hex_string[:2], 16), 'g': int(hex_string[2:4], 16), 'b': int(hex_string[4:], 16)}