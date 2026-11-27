import math

def is_valid_time_signature(time_signature: str) -> bool:
    bottom_number = int(time_signature.split('/')[1])
    return bottom_number != 0 and (bottom_number & (bottom_number - 1)) == 0
    

def find_quarter_notes(time_signature: str) -> int:
    if not is_valid_time_signature(time_signature):
        return None
    top_number, bottom_number = map(int, time_signature.split('/'))
    quarter_note_count = math.floor(top_number * (4 / bottom_number))
    return quarter_note_count
