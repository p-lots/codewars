def what_note(string, fret):
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    start = string.upper()
    return notes[(notes.index(start) + fret) % len(notes)]
