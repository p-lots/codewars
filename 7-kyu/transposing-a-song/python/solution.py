def transpose(song, interval):
    SHARPS = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    FLATS = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
    ret = []
    for note in song:
        if 'b' in note:
            new_note_idx = (FLATS.index(note) + interval) % len(FLATS)
        else:
            new_note_idx = (SHARPS.index(note) + interval) % len(SHARPS)
        ret.append(SHARPS[new_note_idx])
    return ret
