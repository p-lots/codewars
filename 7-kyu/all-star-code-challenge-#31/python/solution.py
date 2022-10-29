def translate_step(instruction):
    try:
        suffix = f' ({instruction.note})'
    except AttributeError:
        suffix = ''
    return f'Pour {instruction.amount} mL of {instruction.solution} into a {instruction.instrument}{suffix}'

def help_jesse(arr):
    return [translate_step(step) for step in arr]
