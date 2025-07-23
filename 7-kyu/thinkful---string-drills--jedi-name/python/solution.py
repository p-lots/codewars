def greet_jedi(first, last):
    jedi_first = last[:3]
    jedi_last = first[:2]
    return f'Greetings, master {jedi_first.title()}{jedi_last.title()}'
    