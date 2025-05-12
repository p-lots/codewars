def get_note(pitch):
    for freq, note in notes_dictionary.items():
        larger, smaller = max(pitch, freq), min(pitch, freq)
        if larger % smaller == 0:
            return note