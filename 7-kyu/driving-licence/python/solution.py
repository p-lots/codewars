month_lookup_table = {
    "Jan": "01", "Feb": "02", "Mar": "03",
    "Apr": "04", "May": "05", "Jun": "06",
    "Jul": "07", "Aug": "08", "Sep": "09",
    "Oct": "10", "Nov": "11", "Dec": "12"
}

def driver(data):
    date_of_birth = data[3][:2]
    month_to_lookup = data[3][3:6]
    month_of_birth = month_lookup_table[month_to_lookup]
    if data[4] == 'F':
        month_of_birth = '5' + month_of_birth[1:] if month_of_birth[0] == '0' else '6' + month_of_birth[1:]
    year_of_birth = data[3][-2:]
    first_initial = data[0][:1]
    middle_initial = '9' if not data[1] else data[1][:1]
    surname = data[2][:5].upper()
    while len(surname) < 5:
        surname += '9'
    return surname + year_of_birth[0] + month_of_birth + date_of_birth + year_of_birth[1] + first_initial + middle_initial + '9AA';