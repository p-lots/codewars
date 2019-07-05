def triangle(row):
    if len(row) == 1:
        return row
    lookup = { 'RB': 'G', 'RG': 'B', 'BR': 'G', 'BG': 'R', 'GR': 'B', 'GB': 'R' }
    while len(row) > 1:
        new_row = ''
        for i in range(len(row) - 1):
            if row[i] == row[i + 1]:
                new_row += row[i]
            else:
                to_lookup = row[i] + row[i + 1]
                new_row += lookup[to_lookup]
        row = new_row
    return new_row